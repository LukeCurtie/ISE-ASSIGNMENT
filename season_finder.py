from PIL import Image

# Dictionary mapping country names to seasons
country_seasons = {
    "australia": {
        "december": "Summer",
        "january": "Summer",
        "february": "Summer",
        "march": "Autumn",
        "april": "Autumn",
        "may": "Autumn",
        "june": "Winter",
        "july": "Winter",
        "august": "Winter",
        "september": "Spring",
        "october": "Spring",
        "november": "Spring"
    },
    "noongar": {
        "birak": "Summer",
        "bunuru": "Summer",
        "djeran": "Autumn",
        "makuru": "Winter",
        "djilba": "Winter",
        "kambarang": "Spring"
    },

    "spain": {
        "december": "Winter",
        "january": "Winter",
        "february": "Winter",
        "march": "Spring",
        "april": "Spring",
        "may": "Spring",
        "june": "Summer",
        "july": "Summer",
        "august": "Summer",
        "september": "Autumn",
        "october": "Autumn" ,
        "november": "Autumn" ,
    
     }, 

      "japan": {
        "december": "Winter",
        "january": "Winter",
        "february": "Winter",
        "march": "Spring",
        "april": "Spring",
        "may": "Spring",
        "june": "Summer",
        "july": "Summer",
        "august": "Summer",
        "september": "Autumn",
        "october": "Autumn" ,
        "november": "Autumn" ,

     },

    "mauritius": {
        "december": "Summer",
        "january": "Summer",
        "february": "Summer",
        "march": "Summer",
        "april": "Summer",
        "may": "Autumn",
        "june": "Winter",
        "july": "Winter",
        "august": "Winter",
        "september": "Winter",
        "october": "Spring",
        "november": "Summer"
    },

    "malaysia": {
       "december": "Northeast Monsoon",
        "january": "Northeast Monsoon",
        "february": "Northeast Monsoon",
        "march": "Inter-Monsoon",
        "april": "Inter-Monsoon",
        "may": "Southeast Monsoon",
        "june":"Southeast Monsoon",
        "july":"Southeast Monsoon",
        "august":"Southeast Monsoon",
        "september":"Southeast Monsoon",
        "october": "Inter-Monsoon",
        "november": "Inter-Monsoon",
   },
   
    "sri lanka": {
       "december": "Northeast Monsoon",
        "january": "Northeast Monsoon",
        "february": "Northeast Monsoon",
        "march": "Inter-Monsoon",
        "april": "Inter-Monsoon",
        "may": "Southeast Monsoon",
        "june": "Southeast Monsoon",
        "july": "Southeast Monsoon",
        "august": "Southeast Monsoon",
        "september": "Southeast-Monsoon",
        "october": "Inter-Monsoon",
        "november": "Inter-Monsoon",
   }
    # Add more countries and seasons as needed
}

# Dictionary mapping seasons to image filenames and symbols
season_info = {
    "Summer": {
        "image": "summer.png",
        "symbol": "☀️"
    },
    "Autumn": {
        "image": "autumn.png",
        "symbol": "🍂"
    },
    "Winter": {
        "image": "winter.png",
        "symbol": "❄️"
    },
    "Spring": {
        "image": "spring.png",
        "symbol": "🌸"
    },
    "Birak": {
        "image": "birak.png",
        "symbol": "🔴"
    },
    "Bunuru": {
        "image": "bunuru.png",
        "symbol": "🔵"
    },
    "Djeran": {
        "image": "djeran.png",
        "symbol": "🟢"
    },
    "Makuru": {
        "image": "makuru.png",
        "symbol": "🟡"
    },
    "Djilba": {
        "image": "djilba.png",
        "symbol": "🟣"
    },
    "Kambarang": {
        "image": "kambarang.png",
        "symbol": "🟠"
    },

    "Inter-Monsoon": {
        "image": "monsoon.png",
        "symbol": "⛅"
    },
    "Northeast Monsoon": {
        "image": "monsoon.png",
        "symbol": "🌧️"
    },
    "Southeast Monsoon": {
        "image": "monsoon.png",
        "symbol": "🌧️"
    },

    # Add more seasons and corresponding information as needed
}

def find_season(country, month):
    # Convert the country name and month to lowercase for case-insensitive matching
    country = country.lower()
    month = month.lower()

    if country in country_seasons:
        if month in country_seasons[country]:
            season = country_seasons[country][month]
            season_info_entry = season_info.get(season)
            if season_info_entry:
                image_filename = season_info_entry["image"]
                symbol = season_info_entry["symbol"]
                image_path = "/home//" + image_filename
                image = Image.open(image_path)
                image.show()  # Display the image
                return f"{season} {symbol}"
    return "Unknown"