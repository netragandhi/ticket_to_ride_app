SEGMENT_SIZE = (0.026, 0.016)
ROUTES = { #maybe implement it so i can change the empty image
    "caracas_miami": {
        "cities": ("caracas", "miami"),
        "length": 2,
        "segments": [
            {"center": (0.1832, 0.5099), "angle": 9},
            {"center": (0.1976, 0.5433), "angle": 85}  # positive = CCW
        ]
    },
        "daressalaam_djibouti_red": {
        "cities": ("daressalaam", "djibouti"),
        "length": 1,
        "segments": [
            {"center": (0.5462, 0.6217), "angle": 100}  # positive = CCW
        ]
    },
        "daressalaam_djibouti_black": {
        "cities": ("daressalaam", "djibouti"),
        "length": 1,
        "segments": [
            {"center": (0.5373, 0.6181), "angle": 100}  # positive = CCW
        ]
    },
        "edinburgh_hamburg_yellow": {
         "cities": ("edinburgh", "hamburg"),
        "length": 1,
        "segments": [
            {"center": (0.4257, 0.2568), "angle": 9}  # positive = CCW
        ]
    },
        "edinburgh_hamburg_black": {
        "cities": ("edinburgh", "hamburg"),
        "length": 1,
        "segments": [
            {"center": (0.4240, 0.2737), "angle": 9}  # positive = CCW
        ]
    },
        "anchorage_cambridgebay": {
        "cities": ("anchorage", "cambridgebay"),
        "length": 6,
        "segments": [
            {"center": (0.0329, 0.2112), "angle": -25},
            {"center": (0.0565, 0.1916), "angle": -25},
            {"center": (0.0817, 0.1737), "angle": -25},
            {"center": (0.1059, 0.1544), "angle": -25},
            {"center": (0.1316, 0.1341), "angle": -25},
            {"center": (0.1554, 0.1163), "angle": -25}
        ]        
    },
        "cambridgebay_reykjavik": {
        "cities": ("cambridgebay", "reykjavik"),
        "length": 6,
        "segments": [
            {"center": (0.2025, 0.1178), "angle": 16},
            {"center": (0.2284, 0.1288), "angle": 16},
            {"center": (0.2544, 0.1408), "angle": 16},
            {"center": (0.2790, 0.1522), "angle": 16},
            {"center": (0.3040, 0.1641), "angle": 16},
            {"center": (0.3314, 0.1779), "angle": 16}
        ]        
    },
        "newyork_reykjavik": {
        "cities": ("newyork", "reykjavik"),
        "length": 6,
        "segments": [
            {"center": (0.2117, 0.3365), "angle": -30},
            {"center": (0.2354, 0.3122), "angle": -30},
            {"center": (0.2582, 0.2889), "angle": -30},
            {"center": (0.2831, 0.2659), "angle": -30},
            {"center": (0.3060, 0.2421), "angle": -30},
            {"center": (0.3294, 0.2210), "angle": -30}
        ]        
    },
        "newyork_edinburgh_red": {
        "cities": ("newyork", "edinburgh"),
        "length": 7,
        "segments": [
            {"center": (0.2166, 0.3598), "angle": -17},
            {"center": (0.2425, 0.3451), "angle": -17},
            {"center": (0.2685, 0.3309), "angle": -17},
            {"center": (0.2945, 0.3185), "angle": -17},
            {"center": (0.3201, 0.3047), "angle": -17},
            {"center": (0.3461, 0.2914), "angle": -17},
            {"center": (0.3723, 0.2781), "angle": -17}
        ]        
    },
        "newyork_edinburgh_purple": {
        "cities": ("newyork", "edinburgh"),
        "length": 7,
        "segments": [
            {"center": (0.2179, 0.3764), "angle": -17},
            {"center": (0.2449, 0.3608), "angle": -17},
            {"center": (0.2703, 0.3480), "angle": -17},
            {"center": (0.2968, 0.3352), "angle": -17},
            {"center": (0.3225, 0.3214), "angle": -17},
            {"center": (0.3494, 0.3077), "angle": -17},
            {"center": (0.3746, 0.2944), "angle": -17}
        ]        
    },
        "losangeles_newyork_purple": {
        "cities": ("losangeles", "newyork"),
        "length": 4,
        "segments": [
            {"center": (0.0835, 0.4075), "angle": -12},
            {"center": (0.1087, 0.3975), "angle": -12},
            {"center": (0.1359, 0.3870), "angle": -12},
            {"center": (0.1606, 0.3792), "angle": -12}
        ]        
    },
        "losangeles_newyork_black": {
        "cities": ("losangeles", "newyork"),
        "length": 4,
        "segments": [
            {"center": (0.0838, 0.4241), "angle": -12},
            {"center": (0.1095, 0.4140), "angle": -12},
            {"center": (0.1351, 0.4049), "angle": -12},
            {"center": (0.1616, 0.3961), "angle": -12}
        ]        
    },
        "losangeles_winnipeg": {
        "cities": ("losangeles", "winnipeg"),
        "length": 3,
        "segments": [
            {"center": (0.0671, 0.3902), "angle": -40},
            {"center": (0.0881, 0.3595), "angle": -40},
            {"center": (0.1077, 0.3287), "angle": -40}
        ]        
    },
        "vancouver_winnipeg": {
        "cities": ("vancouver", "winnipeg"),
        "length": 2,
        "segments": [
            {"center": (0.0745, 0.3031), "angle": -8},
            {"center": (0.0997, 0.2976), "angle": -8}
        ]        
    },
        "winnipeg_newyork": {
        "cities": ("winnipeg", "newyork"),
        "length": 2,
        "segments": [
            {"center": (0.1454, 0.3219), "angle": 25},
            {"center": (0.1673, 0.3420), "angle": 25}
        ]        
    },
        "miami_casablanca": {
        "cities": ("miami", "casablanca"),
        "length": 7,
        "segments": [
            {"center": (0.1883, 0.4768), "angle": -6},
            {"center": (0.2145, 0.4709), "angle": -6},
            {"center": (0.2413, 0.4654), "angle": -6},
            {"center": (0.2688, 0.4594), "angle": -6},
            {"center": (0.2970, 0.4534), "angle": -6},
            {"center": (0.3237, 0.4466), "angle": -6},
            {"center": (0.3512, 0.4402), "angle": -6}
        ]        
    },
        "caracas_lagos": {
        "cities": ("caracas", "lagos"),
        "length": 7,
        "segments": [
            {"center": (0.2320, 0.5912), "angle": 4},
            {"center": (0.2587, 0.5928), "angle": 4},
            {"center": (0.2855, 0.5961), "angle": 4},
            {"center": (0.3129, 0.5979), "angle": 4},
            {"center": (0.3404, 0.5997), "angle": 4},
            {"center": (0.3669, 0.6025), "angle": 4},
            {"center": (0.3939, 0.6049), "angle": 4}
        ]        
    },
        "riodejanero_luanda": {
        "cities": ("riodejanero", "luanda"),
        "length": 6,
        "segments": [
            {"center": (0.2983, 0.7520), "angle": -13},
            {"center": (0.3253, 0.7406), "angle": -13},
            {"center": (0.3530, 0.7286), "angle": -13},
            {"center": (0.3785, 0.7195), "angle": -13},
            {"center": (0.4049, 0.7071), "angle": -13},
            {"center": (0.4322, 0.6980), "angle": -13}
        ]        
    },
        "riodejanero_capetown_black": {
        "cities": ("riodejanero", "capetown"),
        "length": 6,
        "segments": [
            {"center": (0.3019, 0.7795), "angle": 8},
            {"center": (0.3294, 0.7855), "angle": 8},
            {"center": (0.3569, 0.7928), "angle": 8},
            {"center": (0.3836, 0.7992), "angle": 8},
            {"center": (0.4101, 0.8070), "angle": 8},
            {"center": (0.4378, 0.8129), "angle": 8}
        ]        
    },
        "riodejanero_capetown_white": {
        "cities": ("riodejanero", "capetown"),
        "length": 6,
        "segments": [
            {"center": (0.3006, 0.7956), "angle": 8},
            {"center": (0.3279, 0.8025), "angle": 8},
            {"center": (0.3546, 0.8093), "angle": 8},
            {"center": (0.3818, 0.8172), "angle": 8},
            {"center": (0.4088, 0.8231), "angle": 8},
            {"center": (0.4358, 0.8310), "angle": 8}
        ]        
    },
        "riodejanero_capetown_white": {
        "cities": ("riodejanero", "capetown"),
        "length": 6,
        "segments": [
            {"center": (0.3006, 0.7956), "angle": 8},
            {"center": (0.3279, 0.8025), "angle": 8},
            {"center": (0.3546, 0.8093), "angle": 8},
            {"center": (0.3818, 0.8172), "angle": 8},
            {"center": (0.4088, 0.8231), "angle": 8},
            {"center": (0.4358, 0.8310), "angle": 8}
        ]        
    },
        "buenoaires_capetown_purple": {
        "cities": ("buenoaires", "capetown"),
        "length": 7,
        "segments": [
            {"center": (0.2739, 0.8597), "angle": -1},
            {"center": (0.3009, 0.8597), "angle": -1},
            {"center": (0.3286, 0.8579), "angle": -1},
            {"center": (0.3555, 0.8570), "angle": -1},
            {"center": (0.3818, 0.8560), "angle": -1},
            {"center": (0.4098, 0.8569), "angle": -1},
            {"center": (0.4381, 0.8563), "angle": -1}
        ]        
    },
        "buenoaires_capetown_yellow": {
        "cities": ("buenoaires", "capetown"),
        "length": 7,
        "segments": [
            {"center": (0.2729, 0.8773), "angle": -1},
            {"center": (0.3006, 0.8773), "angle": -1},
            {"center": (0.3281, 0.8768), "angle": -1},
            {"center": (0.3556, 0.8755), "angle": -1},
            {"center": (0.3828, 0.8755), "angle": -1},
            {"center": (0.4098, 0.8750), "angle": -1},
            {"center": (0.4373, 0.8744), "angle": -1}
        ]        
    }
}
