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

# connection to localhost
# def connect_to_database():
#     try:
#         # Establish connection
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Sharara@1234",
#             database="lyngsat"
#         )
#         return mydb
#     except mysql.connector.Error as e:
#         print("Error connecting to database:", e)
#         return None

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

def register_new_user(email, username, gender, birth_date, location, region):
    try:
        mydb = connect_to_database()
        if mydb:
            with mydb.cursor() as myCursor:
                query = "INSERT INTO users (email, username, gender, birth_date, location, region) VALUES (%s, %s, %s, %s, %s, %s)"
                user_data = (email, username, gender, birth_date, location, region)
                myCursor.execute(query, user_data)
                mydb.commit()
                print("User registered successfully!")
    except mysql.connector.Error as e:
        print("Error registering user:", e)
    finally:
        if mydb:
            mydb.close()

def get_all_channels():
    query = "SELECT * FROM channels"
    channels = execute_query(query)
    return channels


def view_channels_by_filter(region=None, satellite=None, quality=None,lang=None):
    query = "select channel_SID, c.Channel_name, c.frequency, channel_url, video_format, vpid, apid, lang, audio_text, channel_encryption, package from channels as c inner join satellite_frequency_channel as sfc on sfc.channel_name = c.Channel_name inner join satellites as s on s.satellite_name = sfc.satellite_name where "
    data = []
    if region:
        query += f"continent = '{region}' AND "
        data.append(region)
    if satellite:
        query += f"s.satellite_name = '{satellite}' AND "
        data.append(satellite)
    if quality:
        query += f"c.video_format like '%{quality}%' AND "
        data.append(quality)
    if lang:
        query += f"c.lang = '{lang}' AND "
        data.append(lang)
    if not data:
        query = query[:-6] # Remove the trailing " Where" to select all channels
    query = query[:-5] # Remove the trailing " AND" from the query
    print(query)
    channels = []
    try:
        mydb = connect_to_database()
        if mydb:
            with mydb.cursor() as myCursor:
                myCursor.execute(query)
                channels = myCursor.fetchall()
    except mysql.connector.Error as e:
        print("Error querying channels:", e)
    finally:
        if mydb:
            mydb.close()
    return channels

def validate_user_exists(email):
    global current_user, is_logged_in
    try:
        mydb = connect_to_database()
        if mydb:
            with mydb.cursor() as myCursor:
                query = "SELECT * FROM users WHERE email = %s"
                user_data = (email,)
                myCursor.execute(query, user_data)
                result = myCursor.fetchone()
                if result:
                    print(result)
                    current_user = result
                    is_logged_in = True
                    return True
                else:
                    return False
    except mysql.connector.Error as e:
        print("Error validating user:", e)
        return False
    finally:
        if mydb:
            mydb.close()

def view_channels_by_location(position):
    pass
    # query = "SELECT channel_name FROM channels WHERE location = %s"
    # data = (location,)
    # channels = execute_query(query, data)
    # return channels

def create_user_favorite_list(user_email, selected_channels):
    global current_user, is_logged_in
    # selected_channels: ['!nsert|12603 V', '& TV|4040 H']

    # Construct the query string with multiple value sets
    query = "INSERT INTO User_Channel (user_email, channel_name, frequency) VALUES "
    values = []
    for channel in selected_channels:
        channel = channel.split('|')
        values.append((user_email, channel[0], channel[1]))
    
    # Add placeholders for each value set in the query string
    query += ",".join(["(%s, %s, %s)" for _ in range(len(values))])

    try:
        mydb = connect_to_database()
        if mydb:
            with mydb.cursor() as myCursor:
                print(query)
                myCursor.execute(query, [value for sublist in values for value in sublist])
                mydb.commit()
    except mysql.connector.Error as e:
        print("Error creating favorite list:", e)
    finally:
        if mydb:
            mydb.close()


def get_current_user(email):
    try:
        mydb = connect_to_database()
        if mydb:
            with mydb.cursor() as myCursor:
                query = "SELECT * FROM users WHERE email = %s"
                user_data = (email,)
                myCursor.execute(query, user_data)
                result = myCursor.fetchone()
                if result:
                    print(result)
                    return result
                else:
                    return None
    except mysql.connector.Error as e:
        print("Error validating user:", e)
        return None
    finally:
        if mydb:
            mydb.close()
def get_user_favorite_list(user_email):
    query = "select channel_SID, c.Channel_name, c.frequency, channel_url, video_format, vpid, apid, lang, audio_text, channel_encryption, package from  User_Channel as uc inner join channels as c where uc.user_email = %s and uc.channel_name = c.Channel_name and uc.frequency = c.frequency;"
    data = (user_email,)
    favorite_list = execute_query(query, data)
    return favorite_list

def get_top_five_rockets():
    query = "select  rocketName, count(satellite_name) as 'number of satellites' from satellites group by  rocketName order by count(satellite_name) desc limit 5;"
    top_five_rockets = execute_query(query)
    return top_five_rockets

def get_top_five_channels_per_lang():
    query = "select  lang, sfc.channel_name, count(satellite_name) from channels as c inner join satellite_frequency_channel as sfc on sfc.channel_name = c.Channel_name and sfc.frequency = c.frequency where lang != \"None\" group by lang, sfc.channel_name order by lang, count(satellite_name) desc;"
    top_channels = execute_query(query)
    lang_channels = {}
    for channel in top_channels:
        lang = channel[0]
        if lang not in lang_channels:
            lang_channels[lang] = []
        lang_channels[lang].append(channel[1:])  # Exclude the language from the tuple
        # Limit the channels to only the top five
        lang_channels[lang] = lang_channels[lang][:5]

    html_output = ""
    for lang, channels in lang_channels.items():
        html_output += f"<h2>{lang}: {language_names[lang]}</h2>"
        html_output += "<ul>"
        for channel in channels:
            html_output += f"<li>{channel[0]} - {channel[1]}</li>"
        html_output += "</ul>"
    return html_output

def get_top_five_satellites():
    query = "select s.satellite_name, s.launch_date, sum(DATEDIFF(CURRENT_DATE(), s.launch_date)) AS 'Days since launch', count(sfc.channel_name) as 'Number of Channels',  count(sfc.channel_name) / sum(DATEDIFF(CURRENT_DATE(), s.launch_date)) as 'Growth Rate' from satellites s inner join satellite_frequency_channel as sfc on s.satellite_name = sfc.satellite_name group by satellite_name order by count(sfc.channel_name) / sum(DATEDIFF(CURRENT_DATE(), s.launch_date)) desc limit 5;"
    top_five_satellites = execute_query(query)
    return top_five_satellites

def get_top_packages():
    query = "SELECT  c.package, COUNT(c.Channel_name) AS 'Number of Channels', AVG(sub_q.satellites_per_channel) AS 'Average Satellites per Package' FROM  channels c INNER JOIN ( SELECT  c.Channel_name AS 'Channel_name',  COUNT(s.satellite_name) AS 'satellites_per_channel' FROM  channels c INNER JOIN satellite_frequency_channel AS sfc ON sfc.channel_name = c.Channel_name AND c.frequency = sfc.frequency INNER JOIN satellites s ON s.satellite_name = sfc.satellite_name GROUP BY c.Channel_name) AS sub_q ON c.Channel_name = sub_q.Channel_name WHERE c.package != 'None' GROUP BY c.package ORDER BY COUNT(c.Channel_name) DESC, AVG(sub_q.satellites_per_channel) DESC LIMIT 5;"
    top_packages = execute_query(query)
    return top_packages

# precompute the channels location map
def get_channels_location_map(): 
    query = "select c.Channel_name , sfc.position from channels as c inner join satellite_frequency_channel as sfc on sfc.channel_name = c.Channel_name and sfc.frequency = c.frequency;"
    channels_position = execute_query(query)
    channels_longitude_direction = []
    for channel in channels_position:
        long = channel[1].split(' ')[0]
        direct = channel[1].split(' ')[1]
        channels_longitude_direction.append([channel[0], float(long), direct])
    with open('channels_location.csv', 'w') as f:
        f.write("Channel Name, Longitude, Direction\n")
        for channel in channels_longitude_direction:
            f.write(f"{channel[0]}, {channel[1]}, {channel[2]}\n")

def get_channels_per_location(longitude, direction):
    longitude = float(longitude)
    # read all channels with their locations
    with open('channels_location.csv', 'r') as f:
        lines = f.readlines()
        channels_longitude_direction = []
        for line in lines[1:]:
            channel = line.strip().split(',')
            channels_longitude_direction.append(channel)
    # filter channels based on location
    viewable_channels = []
    viewable_positions = []
    for channel_info in channels_longitude_direction:
        channel_longitude = float(channel_info[1])
        channel_direction = channel_info[2].strip()  # Remove any whitespace
        # print(f"channel longitude: {channel_longitude}, channel direction: {channel_direction}")
        # Check if the channel is within +/- 10 degrees of the given longitude
        if (channel_longitude >= (float(longitude) - 10) and channel_longitude <= (float(longitude) + 10)) and channel_direction == direction:
        # print(f"channel longitude: {channel_longitude}, channel direction: {channel_direction}")
            viewable_channels.append(channel_info[0])  # Append the channel name and location
            viewable_positions.append(str(channel_longitude) + ' ' + channel_direction)

    unique_channels = list(set(viewable_channels))
    unique_positions = list(set(viewable_positions))
    for i in range(0, len(unique_channels)):
        unique_channels[i] = unique_channels[i].replace("'", " ")
        
    # unique_channels = unique_channels[:100]  # Limit the number of channels to 5
    # unique_positions = unique_positions[:100]  # Limit the number of channels to 5
    query = "SELECT DISTINCT c.Channel_name, sfc.satellite_name, sfc.position FROM channels AS c INNER JOIN satellite_frequency_channel AS sfc ON sfc.channel_name = c.Channel_name WHERE c.Channel_name IN ("
    query += ",".join(["'" + channel + "'" for channel in unique_channels])  # Add viewable channel names to the query
    query += ") And sfc.position IN("
    query+= ",".join(["'" + pos + "'" for pos in unique_positions])  # Add viewable channel names to the query
    query+= ") order by sfc.position;"
    print(query)
    result = execute_query(query)
    # for r in result:
    #     print(r)
    return result

def get_fav_channels_by_coninent(continent, encryption):
    should_ignore_encryption = False
    if encryption == "both":
        should_ignore_encryption = True
    query = "select c.Channel_name, c.frequency, c.video_format, c.lang, c.audio_text, c.channel_encryption, c.package from channels as c inner join satellite_frequency_channel as sfc on sfc.channel_name = c.Channel_name inner join satellites as s on s.satellite_name = sfc.satellite_name where s.continent = %s;"
    data = (continent,)
    channels = execute_query(query, data)
    return channels

def get_fav_available_channels(user_email,continent, encryption):
    query  = "select uc.channel_name, uc.frequency, c.channel_encryption, sfc.satellite_name, sfc.position, s.continent from user_channel as uc inner join channels c on uc.user_email  = %s and uc.channel_name = c.Channel_name and uc.frequency = c.frequency inner join satellite_frequency_channel as sfc on sfc.channel_name = uc.channel_name and uc.frequency = sfc.frequency inner join satellites as s on s.satellite_name = sfc.satellite_name where s.continent = %s"
    if encryption == "free":
        query+=" and c.channel_encryption = \"None\";"
    elif encryption == "both":
        pass
    else:
        query+=" and c.channel_encryption != \"None\";"
        
    return execute_query(query, data=(user_email, continent))

    
def main():
    # print(view_channels_by_location(1))
    # print(execute_query("SELECT satellite_name FROM satellites"))
    # result = view_channels_by_filter( region="Asia", lang="kor", quality="HD")
    # for r in result:
    #     print(r)
    # validate_user_exists("alo@gmail.com")
    # print(current_user[1]) # current_user[0] -> email, current_user[1] -> the name
    # create_user_favorite_list("alo@gmail.com", ['!nsert|12603 V'])
    # top_channels = get_top_five_channels_per_lang()
    # get_channels_per_location(75, 'E')

    # get_fav_available_channels("alo@gmail.com", "asia", "both")
    print(get_top_packages())
        
    
if __name__ == "__main__":
    main()
