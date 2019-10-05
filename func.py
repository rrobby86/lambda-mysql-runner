import mysql.connector

def handler(event, context):
    conn = mysql.connector.connect(**event.get("connection", {}))
    cur = conn.cursor()
    cmds = event.get("commands", "")
    params = event.get("parameters", {})
    if isinstance(cmds, str):
        cur.execute(cmds.format(**params), multi=True)
    elif isinstance(cmds, (list, tuple)):
        for cmd in cmds:
            cur.execute(cmd.format(**params))
    conn.close()
