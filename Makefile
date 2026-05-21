FILENAME = code/GameTheory.g4
PREFIX   = $(basename $(notdir $(FILENAME)))

all:
	mkdir -p gen/
	cd code && java -jar /usr/local/lib/antlr-4.13.1-complete.jar \
		-Dlanguage=Python3 -visitor GameTheory.g4 -o ../gen/

clean:
	rm -f gen/$(PREFIX)*.py gen/$(PREFIX)*.tokens gen/$(PREFIX)*.interp
