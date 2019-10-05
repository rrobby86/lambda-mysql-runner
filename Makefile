.PHONY = clean

pip = python3 -m pip
pip_flags = --no-cache-dir

dist.zip: deps func.py
	cd deps && zip -r9 ../dist.zip .
	zip -g dist.zip func.py

deps: requirements.txt
	rm -rf deps
	$(pip) install $(pip_flags) --target ./deps -r requirements.txt

clean:
	rm -rf deps dist.zip
