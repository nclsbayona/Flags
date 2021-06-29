# Convert date to different timezones
# -*- coding: UTF-8 -*-
from pytz import timezone
import datetime as dt
from re import split

try:
    toConvert = input(
        "Ingrese la fecha con formato \"dd/mm/yyyy HH:MM:SS\" (La hora debe ser en formato militar, es decir de 0 a 23): ")
    toConvert = list(map(int, split('/| |:', toConvert)))
except:
    print("Mal ingresado")
try:
    toConvert[5]
except:
    toConvert.append(0)
toConvert = dt.datetime(year=toConvert[2], month=toConvert[1], day=toConvert[0],
                        hour=toConvert[3], minute=toConvert[4], second=toConvert[5])
flags = {
    "America/Mexico_City": "🇲🇽",
    "America/Bogota": "🇨🇴",
    "America/Lima": "🇵🇪",
    "America/Santiago": "🇨🇱",
    "America/Buenos_Aires": "🇦🇷",
    "Europe/Madrid": "🇪🇸",
    "America/Montevideo": "🇺🇾",
    "America/Guayaquil": "🇪🇨",
    "America/Guatemala": "🇬🇹",
    "America/El_Salvador": "🇸🇻",
    "America/La_Paz": "🇧🇴",
    "America/Asuncion": "🇵🇾",
    "America/Santo_Domingo": "🇩🇴",
    "America/Panama": "🇵🇦",
    "America/Costa_Rica": "🇨🇷",
    "America/Tegucigalpa": "🇭🇳",
    "America/Caracas": "🇻🇪",
    "America/Managua": "🇳🇮",
    "Cuba": "🇨🇺",
    "US/Pacific": "🇺🇸",
    "US/Eastern": "🇺🇸",
    "America/Sao_Paulo": "🇧🇷"
}
optimized = dict()
corresponding_times = dict()
for tz in (flags):
    inTZ = toConvert.astimezone(timezone(tz))
    city = str(tz.split('/')[1]).replace('_',
                                         ' ') if tz != "Cuba" and not tz.startswith("US") else tz
    time = str(inTZ.time())
    add = (city, flags[tz], time)
    corresponding_times[tz] = add
    try:
        optimized[time].append(add[1])
    except:
        optimized[time] = list()

for key in corresponding_times:
    print(key, corresponding_times[key])

for key in optimized:
    print(key, optimized[key])
