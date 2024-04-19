from app_backend import *


# sats = execute_query("SELECT satellite_name FROM satellites")
# for sat in sats:
#     sat = str(sat)
#     sat = sat.replace('(\'', '').replace('\',)', '')
#     print(f'<option value="{sat}">{sat}</option>')

langs = execute_query("SELECT distinct lang FROM channels")
for lang in langs:
    lang = str(lang)
    lang = lang.replace('(\'', '').replace('\',)', '')
    print(f'<option value="{lang}">{lang}</option>')