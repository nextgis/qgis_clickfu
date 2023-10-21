UI_PATH=.
UI_SOURCES=$(wildcard $(UI_PATH)/*.ui)
UI_FILES=$(patsubst $(UI_PATH)/%.ui, $(UI_PATH)/ui_%.py, $(UI_SOURCES))
TS_FILES = i18n/*.ts

compile_ts:
	lrelease $(TS_FILES)

clean:
	rm -f $(ALL_FILES)
	rm -f *.pyc
	rm -f *.zip

package: clean compile_ts
	cd .. && rm -f *.zip && zip -r clickfu.zip qgis_clickfu -x \*.pyc \*.ts \*.qrc \*.pro \*~ \*.git\* \*.svn\* \*.idea\* \*Makefile*
	mv ../clickfu.zip .

upload:
	plugin_uploader_NG.py clickfu.zip
