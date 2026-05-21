FILENAME = code/GameTheory.g4
# notdir quita la carpeta, basename quita la extensión
PREFIX = $(basename $(notdir $(FILENAME)))

all:
	java -jar /usr/local/lib/antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor $(FILENAME) -o gen/

clean:
	rm -f gen/$(PREFIX)*.py gen/$(PREFIX)*.tokens gen/$(PREFIX)*.interp
