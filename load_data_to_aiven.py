# import pymysql

# timeout = 10
# connection = pymysql.connect(
#   charset="utf8mb4",
#   connect_timeout=timeout,
#   cursorclass=pymysql.cursors.DictCursor,
#   db="LyngsatDB",
#   host="lyngsat-tag-lyngsat-explorer.b.aivencloud.com",
#   password="AVNS_1eDtsH1eGxrB8ijZJoN",
#   read_timeout=timeout,
#   port=15124,
#   user="avnadmin",
#   write_timeout=timeout,
# )
  
# try:
#   cursor = connection.cursor()
#   cursor.execute("SELECT * FROM users")
#   print(cursor.fetchall())
# finally:
#   connection.close()


import mysql.connector

global current_user
global is_logged_in
is_logged_in = False
current_user = None
# Dictionary mapping language codes to full names
language_names = {
    'Ind': 'Indonesian',
    'Rus': 'Russian',
    'Eng': 'English',
    'Hin': 'Hindi',
    'None': 'Unknown',
    'Spa': 'Spanish',
    'Por': 'Portuguese',
    'Ara': 'Arabic',
    'Mon': 'Mongolian',
    'Geo': 'Georgian',
    'Ger': 'German',
    'Ukr': 'Ukrainian',
    'Tel': 'Telugu',
    'Heb': 'Hebrew',
    'Dut': 'Dutch',
    'Fre': 'French',
    'Tha': 'Thai',
    'Pol': 'Polish',
    'Prs': 'Persian',
    'Ita': 'Italian',
    'Bul': 'Bulgarian',
    'Hrv': 'Croatian',
    'Srp': 'Serbian',
    'Mal': 'Malay',
    'Tur': 'Turkish',
    'Alb': 'Albanian',
    'Kaz': 'Kazakh',
    'Lav': 'Latvian',
    'Bur': 'Burmese',
    'Kur': 'Kurdish',
    'Per': 'Persian',
    'Gre': 'Greek',
    'Dan': 'Danish',
    'Urd': 'Urdu',
    'Amh': 'Amharic',
    'Tam': 'Tamil',
    'Chi': 'Chinese',
    'Tgl': 'Tagalog',
    'Kor': 'Korean',
    'Mar': 'Marathi',
    'Pan': 'Punjabi',
    'Sin': 'Sinhala',
    'Cze': 'Czech',
    'Rum': 'Romanian',
    'Ben': 'Bengali',
    'Kan': 'Kannada',
    'Khm': 'Khmer',
    'Nep': 'Nepali',
    'Orm': 'Oromo',
    'Guj': 'Gujarati',
    'Hau': 'Hausa',
    'Yor': 'Yoruba',
    'Swa': 'Swahili',
    'Ibo': 'Igbo',
    'Asm': 'Assamese',
    'Ori': 'Oriya',
    'Kir': 'Kyrgyz',
    'Bos': 'Bosnian',
    'Mac': 'Macedonian',
    'Tuk': 'Turkmen',
    'Hun': 'Hungarian',
    'Qaa': 'Qaa',
    'Vie': 'Vietnamese',
    'Jpn': 'Japanese',
    'Ber': 'Berber',
    'Aze': 'Azerbaijani',
    'Slo': 'Slovak',
    'Arm': 'Armenian',
    'Slv': 'Slovenian',
    'Som': 'Somali',
    'Tir': 'Tigrinya',
    'Div': 'Divehi',
    'Syr': 'Syriac',
    'Yue': 'Cantonese',
    'May': 'Malay',
    'Hok': 'Hokkien',
    'Swe': 'Swedish',
    'Nor': 'Norwegian',
    'Bho': 'Bhojpuri',
    'Tgk': 'Tajik',
    'Lit': 'Lithuanian',
    'Wel': 'Welsh',
    'Pus': 'Pashto',
    'Uzb': 'Uzbek',
    'Bel': 'Belarusian',
    'Ltz': 'Luxembourgish',
    'Lao': 'Lao',
    'Jav': 'Javanese',
    'Tib': 'Tibetan',
    'Uig': 'Uighur',
    'Gle': 'Irish',
    'Fin': 'Finnish',
    'Est': 'Estonian',
    'Baq': 'Basque',
    'Tet': 'Tetum',
    'Afr': 'Afrikaans',
    'Run': 'Rundi',
    'Nbl': 'Zulu',
    'Sot': 'Sotho',
    'Ssw': 'Swati',
    'F': 'F',
    'Nya': 'Chichewa',
    'Zul': 'Zulu',
    'Tsn': 'Tswana',
    'Tso': 'Tsonga',
    'Ewe': 'Ewe',
    'Ven': 'Venda',
    'Glg': 'Galician',
    'Roh': 'Romansh',
    'Lug': 'Luganda',
    'Ice': 'Icelandic',
    'Ful': 'Fulah',
    'Man': 'Mandarin',
    'Cat': 'Catalan',
    'Lah': 'Lahnda',
    'Nso': 'Northern Sotho',
    'Sp': 'Spanish',
    'Xho': 'Xhosa'
}



def connect_to_database():
    try:
        # Establish connection
        mydb = mysql.connector.connect(
            host="lyngsat-tag-lyngsat-explorer.b.aivencloud.com",
            user="avnadmin",
            password="AVNS_1eDtsH1eGxrB8ijZJoN",
            database="LyngsatDB",
            port=15124
        )
        return mydb
    except mysql.connector.Error as e:
        print("Error connecting to database:", e)
        return None
def execute_query(query, data=None):
    result = []
    try:
        mydb = connect_to_database()
        if mydb:
            with mydb.cursor() as myCursor:
                myCursor.execute(query, data)
                result = myCursor.fetchall()
    except mysql.connector.Error as e:
        print("Error executing query:", e)
    finally:
        if mydb:
            mydb.close()
    return result


connect_to_database()
print(execute_query("SELECT * FROM users"))
