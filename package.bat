mkdir clickfu
mkdir clickfu\i18n
xcopy *.py clickfu
xcopy *.ui clickfu
xcopy README.md clickfu
xcopy LICENSE clickfu
xcopy metadata.txt clickfu
xcopy i18n\clickfu_ru.ts clickfu\i18n\clickfu_ru.ts
lrelease clickfu\i18n\clickfu_ru.ts
del clickfu\i18n\clickfu_ru.ts
zip -r clickfu.zip clickfu
del /s /q clickfu
rmdir /s /q clickfu