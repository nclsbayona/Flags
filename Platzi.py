# -*- coding: UTF-8 -*-
# ๐ Sin lo de arriba no se puede poner emojis
import pytz
import datetime

# Mi script asume la hora de tu PC
date_to_convert = "2020-11-17 21:00:00"
# Recuerda: Es la hora de tu PC

date_to_convert = datetime.datetime.strptime(
    date_to_convert, "%Y-%m-%d %H:%M:%S")

print(date_to_convert)
print("Generando bloque de banderas:")
print("")

# En orden de tamaรฑo de mercado/prioridad
zones = [
    ["๐ฒ๐ฝ", "America/Mexico_City"],
    ["๐จ๐ด", "America/Bogota"],
    ["๐ต๐ช", "America/Lima"],
    ["๐จ๐ฑ", "America/Santiago"],
    ["๐ฆ๐ท", "America/Buenos_Aires"],
    ["๐ช๐ธ", "Europe/Madrid"],
    ["๐บ๐พ", "America/Montevideo"],
    ["๐ช๐จ", "America/Guayaquil"],
    ["๐ฌ๐น", "America/Guatemala"],
    ["๐ธ๐ป", "America/El_Salvador"],
    ["๐ง๐ด", "America/La_Paz"],
    ["๐ต๐พ", "America/Asuncion"],
    ["๐ฉ๐ด", "America/Santo_Domingo"],
    ["๐ต๐ฆ", "America/Panama"],
    ["๐จ๐ท", "America/Costa_Rica"],
    ["๐ญ๐ณ", "America/Tegucigalpa"],
    ["๐ป๐ช", "America/Caracas"],
    ["๐ณ๐ฎ", "America/Managua"],
    ["๐จ๐บ", "Cuba"],
    ["๐บ๐ธ", "US/Pacific"]
]

# Inicializamos el diccionario
times = {"00pm": "X"}

# If you need Brazil:
# ["๐ง๐ท","America/Sao_Paulo"]

# Los timezones no estรกn derivados de paรญses, sino de ciudades.
# Aunque la prioridad es por paรญs

for country in zones:
    dtc = date_to_convert.astimezone(pytz.timezone(country[1]))
    if country[1] == "Europe/Madrid":
        # Imprime la hora en formato de 24 horas y una "H" al final
        dtc = dtc.strftime("%-HH")
    else:
        # Imprime la hora en formato de 12 horas PM/AM
        dtc = dtc.strftime("%-I%p")
    try:
        times[dtc] = times[dtc] + country[0]
    except KeyError:
        times[dtc] = country[0]

    # Si el paรญs es USA en Pacific, agregar el "PT" frente a bandera de US
    if country[1] == "US/Pacific":
        times[dtc] = times[dtc] + " PT"

    times[dtc] = times[dtc] + " "

for time, flag in times.items():
    if flag != "X":
        print(time.lower(), flag.strip())
