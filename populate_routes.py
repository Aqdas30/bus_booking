from bus_booking.models import BusRoute  # Replace 'yourapp' with your actual Django app name

# List of routes with prices
routes = [
    # Bosnia and Herzegovina (KM)
    {"destination": "Orasje - Sarajevo", "price_one_way": 38, "price_round_trip": 57},
    {"destination": "Orasje - Tuzla", "price_one_way": 11, "price_round_trip": 16.50},
    {"destination": "Orasje - Mostar", "price_one_way": 70, "price_round_trip": 85},

    # Croatia (EUR)
    {"destination": "Zagreb", "price_one_way": 54, "price_round_trip": 78},
    {"destination": "Rijeka", "price_one_way": 91, "price_round_trip": 134},
    {"destination": "Pula", "price_one_way": 113.50, "price_round_trip": 165.50},

    # Slovenia (EUR)
    {"destination": "Maribor", "price_one_way": 41, "price_round_trip": 61},
    {"destination": "Ljubljana", "price_one_way": 35, "price_round_trip": 55},

    # Austria (EUR)
    {"destination": "Graz", "price_one_way": 35, "price_round_trip": 55},
    {"destination": "Vienna", "price_one_way": 40, "price_round_trip": 60},
    {"destination": "Salzburg", "price_one_way": 56, "price_round_trip": 76},
    {"destination": "Villach", "price_one_way": 50, "price_round_trip": 70},
    {"destination": "Klagenfurt", "price_one_way": 50, "price_round_trip": 70},

    # Switzerland (EUR)
    {"destination": "Bern", "price_one_way": 116, "price_round_trip": 170},
    {"destination": "Basel", "price_one_way": 116, "price_round_trip": 170},
    {"destination": "Lucerne", "price_one_way": 116, "price_round_trip": 170},
    {"destination": "Zurich", "price_one_way": 116, "price_round_trip": 170},

    # Netherlands & Belgium (EUR)
    {"destination": "Amsterdam", "price_one_way": 90, "price_round_trip": 0},
    {"destination": "Rotterdam", "price_one_way": 90, "price_round_trip": 0},
    {"destination": "Brussels", "price_one_way": 90, "price_round_trip": 0},

    # Germany (EUR)
    {"destination": "München", "price_one_way": 68, "price_round_trip": 101},
    {"destination": "Ulm", "price_one_way": 75, "price_round_trip": 110},
    {"destination": "Stuttgart", "price_one_way": 79, "price_round_trip": 117},
    {"destination": "Pforzheim", "price_one_way": 82, "price_round_trip": 120},
    {"destination": "Karlsruhe", "price_one_way": 84, "price_round_trip": 122},
    {"destination": "Mannheim", "price_one_way": 87, "price_round_trip": 128},
    {"destination": "Frankfurt", "price_one_way": 92, "price_round_trip": 134},
    {"destination": "Köln", "price_one_way": 100, "price_round_trip": 145},
    {"destination": "Düsseldorf", "price_one_way": 104, "price_round_trip": 150},
    {"destination": "Duisburg", "price_one_way": 105, "price_round_trip": 152},
    {"destination": "Essen", "price_one_way": 106, "price_round_trip": 153},
    {"destination": "Dortmund", "price_one_way": 108, "price_round_trip": 156},
    {"destination": "Freilassing", "price_one_way": 55, "price_round_trip": 85},
    {"destination": "Rosenheim", "price_one_way": 55, "price_round_trip": 85},
    {"destination": "Ingolstadt", "price_one_way": 80, "price_round_trip": 112},
    {"destination": "Nürnberg", "price_one_way": 85, "price_round_trip": 119},
    {"destination": "Kassel", "price_one_way": 102, "price_round_trip": 144},
    {"destination": "Göttingen", "price_one_way": 105, "price_round_trip": 148},
    {"destination": "Hannover", "price_one_way": 113, "price_round_trip": 159},
    {"destination": "Hamburg", "price_one_way": 121, "price_round_trip": 171},
    {"destination": "Passau", "price_one_way": 75, "price_round_trip": 110},
    {"destination": "Regensburg", "price_one_way": 75, "price_round_trip": 110},
    {"destination": "Berlin", "price_one_way": 95, "price_round_trip": 140},
]

# Populate the database
for route in routes:
    obj, created = BusRoute.objects.get_or_create(
        destination=route["destination"],
        defaults={
            "price_one_way": route["price_one_way"],
            "price_round_trip": route["price_round_trip"],
            "is_active": True,
        },
    )
    if created:
        print(f"Added route: {route['destination']} at {route['price_one_way']}/{route['price_round_trip']} EUR")
    else:
        print(f"Route already exists: {route['destination']}")
