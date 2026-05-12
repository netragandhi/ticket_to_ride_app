SEGMENT_SIZE = (0.026, 0.016)

BOARD_CORNERS = [
    (0.0139, 0.0362),
    (0.9874, 0.0073),
    (0.9967, 0.9936),
    (0.0072, 0.9862),
]

HUE_RANGES = {
    "red":    [(0, 10), (170, 179)],  # red wraps around
    "yellow": [(10, 30)],
    "green":  [(30, 50)],
    "blue":   [(50, 130)]
}

ROUTE_SCORING_TABLE = {
    1: 1,
    2: 2,
    3: 4,
    4: 7,
    5: 10,
    6: 15,
    7: 18,
    8: 21
}

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
        "riodejaneiro_luanda": {
        "cities": ("riodejaneiro", "luanda"),
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
        "riodejaneiro_capetown_black": {
        "cities": ("riodejaneiro", "capetown"),
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
        "riodejaneiro_capetown_white": {
        "cities": ("riodejaneiro", "capetown"),
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
        "riodejaneiro_capetown_white": {
        "cities": ("riodejaneiro", "capetown"),
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
        "buenosaires_capetown_purple": {
        "cities": ("buenosaires", "capetown"),
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
        "buenosaires_capetown_yellow": {
        "cities": ("buenosaires", "capetown"),
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
    },
        "mexico_caracas_purple": {
        "cities": ("mexico", "caracas"),
        "length": 3,
        "segments": [
            {"center": (0.1238, 0.5397), "angle": 17},
            {"center": (0.1488, 0.5543), "angle": 17},
            {"center": (0.1737, 0.5690), "angle": 17}
        ]        
    },
        "mexico_caracas_red": {
        "cities": ("mexico", "caracas"),
        "length": 3,
        "segments": [
            {"center": (0.1215, 0.5571), "angle": 17},
            {"center": (0.1462, 0.5708), "angle": 17},
            {"center": (0.1714, 0.5846), "angle": 17}
        ]        
    },
        "lima_caracas_yellow": {
        "cities": ("lima", "caracas"),
        "length": 2,
        "segments": [
            {"center": (0.1734, 0.6731), "angle": -70},
            {"center": (0.1835, 0.6286), "angle": -70}
        ]        
    },
        "lima_caracas_white": {
        "cities": ("lima", "caracas"),
        "length": 2,
        "segments": [
            {"center": (0.1814, 0.6795), "angle": -70},
            {"center": (0.1919, 0.6364), "angle": -70}
        ]        
    },
        "losangeles_mexico_yellow": {
        "cities": ("losangeles", "mexico"),
        "length": 2,
        "segments": [
            {"center": (0.0707, 0.4558), "angle": 55},
            {"center": (0.0856, 0.4934), "angle": 55}
        ]        
    },
        "losangeles_mexico_white": {
        "cities": ("losangeles", "mexico"),
        "length": 2,
        "segments": [
            {"center": (0.0619, 0.4654), "angle": 55},
            {"center": (0.0773, 0.5044), "angle": 55}
        ]        
    },
        "buenosaires_riodejaneiro_white": {
        "cities": ("buenosaires", "riodejaneiro"),
        "length": 1,
        "segments": [
            {"center": (0.2536, 0.8134), "angle": -55}
        ]        
    },
        "buenosaires_riodejaneiro_red": {
        "cities": ("buenosaires", "riodejaneiro"),
        "length": 1,
        "segments": [
            {"center": (0.2616, 0.8244), "angle": -55}
        ]        
    },
        "honolulu_lima": {
        "cities": ("honolulu", "lima"),
        "length": 6,
        "segments": [
            {"center": (0.0275, 0.5786), "angle": 30},
            {"center": (0.0506, 0.6002), "angle": 30},
            {"center": (0.0740, 0.6254), "angle": 30},
            {"center": (0.0974, 0.6474), "angle": 30},
            {"center": (0.1208, 0.6708), "angle": 30},
            {"center": (0.1449, 0.6946), "angle": 30}
        ]        
    },
        "christchurch_valparaiso": {
        "cities": ("christchurch", "valparaiso"),
        "length": 7,
        "segments": [
            {"center": (0.9692, 0.8926), "angle": -8},
            {"center": (0.0280, 0.8890), "angle": -8},
            {"center": (0.0563, 0.8835), "angle": -8},
            {"center": (0.0817, 0.8785), "angle": -8},
            {"center": (0.1089, 0.8721), "angle": -8},
            {"center": (0.1359, 0.8675), "angle": -8},
            {"center": (0.1629, 0.8615), "angle": -8}
        ]        
    },
        "edinburgh_marseille_white": {
        "cities": ("edinburgh", "marseille"),
        "length": 1,
        "segments": [
            {"center": (0.4018, 0.3095), "angle": 66}
        ]        
    },
        "edinburgh_marseille_green": {
        "cities": ("edinburgh", "marseille"),
        "length": 1,
        "segments": [
            {"center": (0.4104, 0.3040), "angle": 66}
        ]        
    },
        "marseille_casablanca": {
        "cities": ("marseille", "casablanca"),
        "length": 1,
        "segments": [
            {"center": (0.4029, 0.3906), "angle": -55}
        ]        
    },
        "marseille_hamburg_purple": {
        "cities": ("marseille", "hamburg"),
        "length": 1,
        "segments": [
            {"center": (0.4350, 0.3150), "angle": -55}
        ]        
    },
        "marseille_hamburg_red": {
        "cities": ("marseille", "hamburg"),
        "length": 1,
        "segments": [
            {"center": (0.4417, 0.3255), "angle": -55}
        ]        
    },
        "hamburg_moskva_white": {
        "cities": ("hamburg", "moskva"),
        "length": 2,
        "segments": [
            {"center": (0.4756, 0.2623), "angle": -10},
            {"center": (0.5013, 0.2536), "angle": -10}
        ]        
    },
        "hamburg_moskva_black": {
        "cities": ("hamburg", "moskva"),
        "length": 2,
        "segments": [
            {"center": (0.4784, 0.2815), "angle": -10},
            {"center": (0.5036, 0.2719), "angle": -10}
        ]        
    },
        "moskva_novosibirsk_green": {
        "cities": ("moskva", "novosibirsk"),
        "length": 4,
        "segments": [
            {"center": (0.5524, 0.2494), "angle": 0},
            {"center": (0.5786, 0.2485), "angle": 0},
            {"center": (0.6069, 0.2490), "angle": 0},
            {"center": (0.6336, 0.2481), "angle": 0}
        ]        
    },
        "moskva_novosibirsk_yellow": {
        "cities": ("moskva", "novosibirsk"),
        "length": 4,
        "segments": [
            {"center": (0.5529, 0.2651), "angle": 0},
            {"center": (0.5789, 0.2651), "angle": 0},
            {"center": (0.6059, 0.2664), "angle": 0},
            {"center": (0.6349, 0.2669), "angle": 0}
        ]        
    },
        "novosibirsk_beijing_red": {
        "cities": ("novosibirsk", "beijing"),
        "length": 3,
        "segments": [
            {"center": (0.6878, 0.2801), "angle": 27},
            {"center": (0.7109, 0.3017), "angle": 27},
            {"center": (0.7359, 0.3246), "angle": 27}
        ]        
    },
        "novosibirsk_beijing_black": {
        "cities": ("novosibirsk", "beijing"),
        "length": 3,
        "segments": [
            {"center": (0.6827, 0.2952), "angle": 27},
            {"center": (0.7076, 0.3191), "angle": 27},
            {"center": (0.7312, 0.3411), "angle": 27}
        ]
    },
        "novosibirsk_yakutsk": {
        "cities": ("novosibirsk", "yakutsk"),
        "length": 3,
        "segments": [
            {"center": (0.6883, 0.2412), "angle": -28},
            {"center": (0.7145, 0.2197), "angle": -28},
            {"center": (0.7387, 0.1985), "angle": -28}
        ]
    },
        "novosibirsk_tiksi": {
        "cities": ("novosibirsk", "tiksi"),
        "length": 3,
        "segments": [
            {"center": (0.6770, 0.2178), "angle": -58},
            {"center": (0.6924, 0.1765), "angle": -58},
            {"center": (0.7071, 0.1357), "angle": -58}
        ]
    },
        "novosibirsk_lahore": {
        "cities": ("novosibirsk", "lahore"),
        "length": 2,
        "segments": [
            {"center": (0.6536, 0.3132), "angle": -84},
            {"center": (0.6503, 0.3590), "angle": -84}
        ]
    },
        "lahore_beijing": {
        "cities": ("lahore", "beijing"),
        "length": 3,
        "segments": [
            {"center": (0.6732, 0.4003), "angle": -13},
            {"center": (0.7007, 0.3902), "angle": -13},
            {"center": (0.7279, 0.3783), "angle": -13}
        ]
    },
        "tehran_lahore": {
        "cities": ("tehran", "lahore"),
        "length": 2,
        "segments": [
            {"center": (0.5917, 0.4120), "angle": -2},
            {"center": (0.6195, 0.4091), "angle": -2}
        ]
    },
        "lahore_mumbai_green": {
        "cities": ("lahore", "mumbai"),
        "length": 1,
        "segments": [
            {"center": (0.6411, 0.4534), "angle": 95}
        ]
    },
        "lahore_mumbai_black": {
        "cities": ("lahore", "mumbai"),
        "length": 1,
        "segments": [
            {"center": (0.6508, 0.4543), "angle": 95}
        ]
    },
        "yakutsk_beijing": {
        "cities": ("yakutsk", "beijing"),
        "length": 3,
        "segments": [
            {"center": (0.7626, 0.2150), "angle": 90},
            {"center": (0.7631, 0.2650), "angle": 90},
            {"center": (0.7634, 0.3113), "angle": 90}
        ]
    },
        "tiksi_yakutsk": {
        "cities": ("tiksi", "yakutsk"),
        "length": 1,
        "segments": [
            {"center": (0.7443, 0.1394), "angle": 45}
        ]
    },
        "murmansk_tiksi": {
        "cities": ("murmansk", "tiksi"),
        "length": 7,
        "segments": [
            {"center": (0.5218, 0.1343), "angle": -5},
            {"center": (0.5486, 0.1302), "angle": -5},
            {"center": (0.5747, 0.1251), "angle": -5},
            {"center": (0.6023, 0.1201), "angle": -5},
            {"center": (0.6295, 0.1142), "angle": -5},
            {"center": (0.6570, 0.1100), "angle": -5},
            {"center": (0.6843, 0.1050), "angle": -5}
        ]
    },
        "yakutsk_petropavlovsk": {
        "cities": ("yakutsk", "petropavlovsk"),
        "length": 3,
        "segments": [
            {"center": (0.7870, 0.1912), "angle": 28},
            {"center": (0.8119, 0.2132), "angle": 28},
            {"center": (0.8368, 0.2348), "angle": 28}
        ]
    },
        "beijing_hongkong_white": {
        "cities": ("beijing", "hongkong"),
        "length": 2,
        "segments": [
            {"center": (0.7577, 0.3971), "angle": 84},
            {"center": (0.7616, 0.4461), "angle": 84}
        ]
    },
        "beijing_hongkong_green": {
        "cities": ("beijing", "hongkong"),
        "length": 2,
        "segments": [
            {"center": (0.7685, 0.3948), "angle": 84},
            {"center": (0.7718, 0.4443), "angle": 84}
        ]
    },
        "murmansk_moskva": {
        "cities": ("murmansk", "moskva"),
        "length": 2,
        "segments": [
            {"center": (0.5028, 0.1784), "angle": 60},
            {"center": (0.5157, 0.2173), "angle": 60}
        ]
    },
        "moskva_tehran": {
        "cities": ("moskva", "tehran"),
        "length": 3,
        "segments": [
            {"center": (0.5352, 0.2957), "angle": 65},
            {"center": (0.5462, 0.3398), "angle": 65},
            {"center": (0.5568, 0.3829), "angle": 65}
        ]
    },
        "alzahira_tehran_yellow": {
        "cities": ("alzahira", "tehran"),
        "length": 1,
        "segments": [
            {"center": (0.5406, 0.4301), "angle": -20}
        ]
    },
        "alzahira_tehran_black": {
        "cities": ("alzahira", "tehran"),
        "length": 1,
        "segments": [
            {"center": (0.5455, 0.4475), "angle": -20}
        ]
    },
        "capetown_daressalaam_green": {
        "cities": ("capetown", "daressalaam"),
        "length": 3,
        "segments": [
            {"center": (0.4850, 0.7818), "angle": -54},
            {"center": (0.5008, 0.7454), "angle": -54},
            {"center": (0.5170, 0.7074), "angle": -54}
        ]
    },
        "capetown_daressalaam_purple": {
        "cities": ("capetown", "daressalaam"),
        "length": 3,
        "segments": [
            {"center": (0.4918, 0.7932), "angle": -54},
            {"center": (0.5088, 0.7543), "angle": -54},
            {"center": (0.5255, 0.7153), "angle": -54}
        ]
    },
        "alzahira_djibouti_red": {
        "cities": ("alzahira", "djibouti"),
        "length": 2,
        "segments": [
            {"center": (0.5221, 0.4975), "angle": 65},
            {"center": (0.5331, 0.5401), "angle": 65}
        ]
    },
        "alzahira_djibouti_white": {
        "cities": ("alzahira", "djibouti"),
        "length": 2,
        "segments": [
            {"center": (0.5303, 0.4897), "angle": 65},
            {"center": (0.5414, 0.5328), "angle": 65}
        ]
    },
        "luanda_daressalaam": {
        "cities": ("luanda", "daressalaam"),
        "length": 2,
        "segments": [
            {"center": (0.4846, 0.6777), "angle": -9},
            {"center": (0.5108, 0.6712), "angle": -9}        
        ]
    },
        "capetown_null_red": {
        "cities": ("capetown", "null"),
        "length": 5,
        "segments": [
            {"center": (0.5013, 0.8510), "angle": 14},
            {"center": (0.5272, 0.8606), "angle": 14},
            {"center": (0.5537, 0.8717), "angle": 14},
            {"center": (0.5809, 0.8840), "angle": 14},
            {"center": (0.6074, 0.8964), "angle": 14}
        ]
    },
        "capetown_null_green": {
        "cities": ("capetown", "null"),
        "length": 5,
        "segments": [
            {"center": (0.4987, 0.8670), "angle": 14},
            {"center": (0.5262, 0.8789), "angle": 14},
            {"center": (0.5516, 0.8895), "angle": 14},
            {"center": (0.5789, 0.9023), "angle": 14},
            {"center": (0.6064, 0.9143), "angle": 14}
        ]
    },
        "null_perth_white": {
        "cities": ("null", "perth"),
        "length": 5,
        "segments": [
            {"center": (0.6557, 0.8945), "angle": -20},
            {"center": (0.6817, 0.8776), "angle": -20},
            {"center": (0.7073, 0.8611), "angle": -20},
            {"center": (0.7346, 0.8423), "angle": -20},
            {"center": (0.7600, 0.8258), "angle": -20}
        ]
    },
        "null_perth_purple": {
        "cities": ("null", "perth"),
        "length": 5,
        "segments": [
            {"center": (0.6596, 0.9129), "angle": -20},
            {"center": (0.6868, 0.8936), "angle": -20},
            {"center": (0.7122, 0.8772), "angle": -20},
            {"center": (0.7384, 0.8597), "angle": -20},
            {"center": (0.7641, 0.8427), "angle": -20}
        ]
    },
        "perth_sydney_white": {
        "cities": ("perth", "sydney"),
        "length": 2,
        "segments": [
            {"center": (0.8245, 0.8221), "angle": 8},
            {"center": (0.8517, 0.8299), "angle": 8}
        ]
    },
        "perth_sydney_yellow": {
        "cities": ("perth", "sydney"),
        "length": 2,
        "segments": [
            {"center": (0.8227, 0.8414), "angle": 8},
            {"center": (0.8502, 0.8478), "angle": 8}
        ]
    },
        "perth_darwin": {
        "cities": ("perth", "darwin"),
        "length": 2,
        "segments": [
            {"center": (0.8088, 0.7744), "angle": -52},
            {"center": (0.8248, 0.7382), "angle": -52}
        ]
    },
        "darwin_sydney": {
        "cities": ("darwin", "sydney"),
        "length": 2,
        "segments": [
            {"center": (0.8607, 0.7464), "angle": 70},
            {"center": (0.8708, 0.7937), "angle": 70}
        ]
    },
        "darwin_portmoresby": {
        "cities": ("darwin", "portmoresby"),
        "length": 1,
        "segments": [
            {"center": (0.8702, 0.6804), "angle": -16}
        ]
    },
        "darwin_jakarta": {
        "cities": ("darwin", "jakarta"),
        "length": 2,
        "segments": [
            {"center": (0.7878, 0.6657), "angle": 13},
            {"center": (0.8153, 0.6758), "angle": 13}
        ]
    },
        "jakarta_manila": {
        "cities": ("jakarta", "manila"),
        "length": 2,
        "segments": [
            {"center": (0.7801, 0.6236), "angle": -52},
            {"center": (0.7980, 0.5837), "angle": -52}
        ]
    },
        "manila_tokyo": {
        "cities": ("manila", "tokyo"),
        "length": 2,
        "segments": [
            {"center": (0.8142, 0.4883), "angle": -70},
            {"center": (0.8240, 0.4425), "angle": -70}
        ]
    },
        "bangkok_hongkong_purple": {
        "cities": ("bangkok", "hongkong"),
        "length": 1,
        "segments": [
            {"center": (0.7523, 0.5139), "angle": -45}
        ]
    },
        "bangkok_hongkong_black": {
        "cities": ("bangkok", "hongkong"),
        "length": 1,
        "segments": [
            {"center": (0.7595, 0.5263), "angle": -45}
        ]
    },
        "daressalaam_jakarta_purple": {
        "cities": ("daressalaam", "jakarta"),
        "length": 7,
        "segments": [
            {"center": (0.5639, 0.6557), "angle": 0},
            {"center": (0.5912, 0.6557), "angle": 0},
            {"center": (0.6182, 0.6561), "angle": 0},
            {"center": (0.6452, 0.6557), "angle": 0},
            {"center": (0.6734, 0.6557), "angle": 0},
            {"center": (0.7017, 0.6566), "angle": 0},
            {"center": (0.7297, 0.6566), "angle": 0}
        ]
    },
        "daressalaam_jakarta_green": {
        "cities": ("daressalaam", "jakarta"),
        "length": 7,
        "segments": [
            {"center": (0.5637, 0.6740), "angle": 0},
            {"center": (0.5917, 0.6744), "angle": 0},
            {"center": (0.6192, 0.6735), "angle": 0},
            {"center": (0.6462, 0.6740), "angle": 0},
            {"center": (0.6739, 0.6745), "angle": 0},
            {"center": (0.7022, 0.6745), "angle": 0},
            {"center": (0.7302, 0.6740), "angle": 0}
        ]
    },
        "sydney_christchurch_white": {
        "cities": ("sydney", "christchurch"),
        "length": 1,
        "segments": [
            {"center": (0.9180, 0.8680), "angle": 27}
        ]
    },
        "sydney_christchurch_red": {
        "cities": ("sydney", "christchurch"),
        "length": 1,
        "segments": [
            {"center": (0.9124, 0.8845), "angle": 27}
        ]
    },
        "hongkong_manila": {
        "cities": ("hongkong", "manila"),
        "length": 1,
        "segments": [
            {"center": (0.7893, 0.5208), "angle": 40}
        ]
    },
        "daressalaam_toamasina": {
        "cities": ("daressalaam", "toamasina"),
        "length": 1,
        "segments": [
            {"center": (0.5524, 0.7057), "angle": 55}
        ]
    },
        "capetown_toamasina": {
        "cities": ("capetown", "toamasina"),
        "length": 3,
        "segments": [
            {"center": (0.4989, 0.8190), "angle": -30},
            {"center": (0.5226, 0.7950), "angle": -30},
            {"center": (0.5465, 0.7717), "angle": -30}
        ]
    },
        "lagos_luanda_purple": {
        "cities": ("lagos", "luanda"),
        "length": 3,
        "segments": [
            {"center": (0.4391, 0.6470), "angle": 57}
        ]
    },
        "lagos_luanda_yellow": {
        "cities": ("lagos", "luanda"),
        "length": 3,
        "segments": [
            {"center": (0.4473, 0.6369), "angle": 57}
        ]
    },
        "luanda_capetown": {
        "cities": ("luanda", "capetown"),
        "length": 2,
        "segments": [
            {"center": (0.4576, 0.7309), "angle": 85},
            {"center": (0.4602, 0.7781), "angle": 85}
        ]
    },
        "vancouver_losangeles_green": {
        "cities": ("vancouver", "losangeles"),
        "length": 1,
        "segments": [
            {"center": (0.0427, 0.3696), "angle": 87}
        ]
    },
        "vancouver_losangeles_red": {
        "cities": ("vancouver", "losangeles"),
        "length": 1,
        "segments": [
            {"center": (0.0509, 0.3700), "angle": 87}
        ]
    },
        "lima_valparaiso_left": {
        "cities": ("lima", "valparaiso"),
        "length": 2,
        "segments": [
            {"center": (0.1703, 0.7662), "angle": 75},
            {"center": (0.1773, 0.8138), "angle": 75}
        ]
    },
        "lima_valparaiso_right": {
        "cities": ("lima", "valparaiso"),
        "length": 2,
        "segments": [
            {"center": (0.1796, 0.7616), "angle": 75},
            {"center": (0.1870, 0.8093), "angle": 75}
        ]
    },
        "lima_sydney_purple": {
        "cities": ("lima", "sydney"),
        "length": 8,
        "segments": [
            {"center": (0.9049, 0.8197), "angle": -40},
            {"center": (0.9260, 0.7904), "angle": -40},
            {"center": (0.9484, 0.7592), "angle": -40},
            {"center": (0.0344, 0.7689), "angle": -15},
            {"center": (0.0606, 0.7588), "angle": -15},
            {"center": (0.0861, 0.7492), "angle": -15},
            {"center": (0.1128, 0.7377), "angle": -15},
            {"center": (0.1390, 0.7267), "angle": -15},
        ]
    },
        "lima_sydney_black": {
        "cities": ("lima", "sydney"),
        "length": 8,
        "segments": [
            {"center": (0.9101, 0.8336), "angle": -40},
            {"center": (0.9329, 0.8038), "angle": -40},
            {"center": (0.9548, 0.7717), "angle": -40},
            {"center": (0.0360, 0.7863), "angle": -15},
            {"center": (0.0609, 0.7763), "angle": -15},
            {"center": (0.0884, 0.7657), "angle": -15},
            {"center": (0.1149, 0.7556), "angle": -15},
            {"center": (0.1408, 0.7432), "angle": -15}
        ]
    },   
        "miami_newyork": {
        "cities": ("miami", "newyork"),
        "length": 2,
        "segments": [
            {"center": (0.1616, 0.4553), "angle": -80},
            {"center": (0.1770, 0.4114), "angle": -35}
        ]
    },   
        "reykjavik_edinburgh": {
        "cities": ("reykjavik", "edinburgh"),
        "length": 2,
        "segments": [
            {"center": (0.3826, 0.1898), "angle": 6},
            {"center": (0.3993, 0.2192), "angle": 85}
        ]
    },   
        "reykjavik_murmansk": {
        "cities": ("reykjavik", "murmansk"),
        "length": 2,
        "segments": [
            {"center": (0.3795, 0.1568), "angle": -30},
            {"center": (0.4052, 0.1388), "angle": -15},
            {"center": (0.4322, 0.1301), "angle": -5},
            {"center": (0.4604, 0.1323), "angle": 6}
        ]
    },   
        "hamburg_athina": {
        "cities": ("hamburg", "athina"),
        "length": 2,
        "segments": [
            {"center": (0.4687, 0.3086), "angle": 35},
            {"center": (0.4838, 0.3485), "angle": 75}
        ]
    },   
        "marseille_athina": {
        "cities": ("marseille", "athina"),
        "length": 2,
        "segments": [
            {"center": (0.4347, 0.3779), "angle": 45},
            {"center": (0.4597, 0.3957), "angle": 0}
        ]
    },   
        "athina_tehran": {
        "cities": ("athina", "tehran"),
        "length": 2,
        "segments": [
            {"center": (0.5097, 0.3916), "angle": 0},
            {"center": (0.5375, 0.3975), "angle": 15}
        ]
    },   
        "casablanca_alzahira": {
        "cities": ("casablanca", "alzahira"),
        "length": 3,
        "segments": [
            {"center": (0.4257, 0.4415), "angle": 10},
            {"center": (0.4527, 0.4484), "angle": 4},
            {"center": (0.4797, 0.4507), "angle": 0}
        ]
    },   
        "casablanca_lagos": {
        "cities": ("casablanca", "lagos"),
        "length": 4,
        "segments": [
            {"center": (0.3785, 0.4732), "angle": -60},
            {"center": (0.3679, 0.5204), "angle": -75},
            {"center": (0.3785, 0.5650), "angle": 30},
            {"center": (0.4042, 0.5850), "angle": 15}
        ]
    },   
        "winnipeg_cambridgebay": {
        "cities": ("winnipeg", "cambridgebay"),
        "length": 4,
        "segments": [
            {"center": (0.1388, 0.2728), "angle": -55},
            {"center": (0.1544, 0.2325), "angle": -60},
            {"center": (0.1660, 0.1853), "angle": -65},
            {"center": (0.1752, 0.1398), "angle": -75}
        ]
    },   
        "caracas_riodejaneiro_green": {
        "cities": ("caracas", "riodejaneiro"),
        "length": 4,
        "segments": [
            {"center": (0.2258, 0.6121), "angle": 25},
            {"center": (0.2503, 0.6355), "angle": 35},
            {"center": (0.2685, 0.6745), "angle": 55},
            {"center": (0.2798, 0.7221), "angle": 75}
        ]
    },   
        "caracas_riodejaneiro_black": {
        "cities": ("caracas", "riodejaneiro"),
        "length": 4,
        "segments": [
            {"center": (0.2169, 0.6286), "angle": 23},
            {"center": (0.2428, 0.6497), "angle": 35},
            {"center": (0.2616, 0.6878), "angle": 57},
            {"center": (0.2713, 0.7364), "angle": 75}
        ]
    },   
        "valparaiso_buenosaires": {
        "cities": ("valparaiso", "buenosaires"),
        "length": 3,
        "segments": [
            {"center": (0.1937, 0.9010), "angle": 70},
            {"center": (0.2138, 0.9266), "angle": 0},
            {"center": (0.2341, 0.8991), "angle": -70}
        ]
    },   
        "daressalaam_mumbai": {
        "cities": ("daressalaam", "mumbai"),
        "length": 4,
        "segments": [
            {"center": (0.5680, 0.6337), "angle": -12},
            {"center": (0.5938, 0.6231), "angle": -12},
            {"center": (0.6172, 0.6011), "angle": -45},
            {"center": (0.6321, 0.5621), "angle": -70}
        ]
    },   
        "tehran_mumbai_white": {
        "cities": ("tehran", "mumbai"),
        "length": 3,
        "segments": [
            {"center": (0.5743, 0.4576), "angle": 72},
            {"center": (0.5897, 0.4979), "angle": 37},
            {"center": (0.6172, 0.5089), "angle": -3}
        ]
    },   
        "tehran_mumbai_purple": {
        "cities": ("tehran", "mumbai"),
        "length": 3,
        "segments": [
            {"center": (0.5660, 0.4733), "angle": 72},
            {"center": (0.5848, 0.5144), "angle": 37},
            {"center": (0.6120, 0.5282), "angle": -3}
        ]
    },   
        "mumbai_bangkok_red": {
        "cities": ("mumbai", "bangkok"),
        "length": 3,
        "segments": [
            {"center": (0.6686, 0.4801), "angle": -25},
            {"center": (0.6989, 0.4764), "angle": 20},
            {"center": (0.7238, 0.5076), "angle": 50}
        ]
    },   
        "mumbai_bangkok_yellow": {
        "cities": ("mumbai", "bangkok"),
        "length": 3,
        "segments": [
            {"center": (0.6662, 0.5016), "angle": -25},
            {"center": (0.6955, 0.4934), "angle": 20},
            {"center": (0.7174, 0.5246), "angle": 50}
        ]
    },   
        "bangkok_jakarta": {
        "cities": ("bangkok", "jakarta"),
        "length": 2,
        "segments": [
            {"center": (0.7286, 0.5880), "angle": -75},
            {"center": (0.7382, 0.6269), "angle": 30}
        ]
    },   
        "jakarta_perth": {
        "cities": ("jakarta", "perth"),
        "length": 3,
        "segments": [
            {"center": (0.7528, 0.7021), "angle": -85},
            {"center": (0.7569, 0.7519), "angle": 70},
            {"center": (0.7729, 0.7905), "angle": 35}
        ]
    },   
        "bangkok_manila": {
        "cities": ("bangkok", "manila"),
        "length": 2,
        "segments": [
            {"center": (0.7613, 0.5745), "angle": 15},
            {"center": (0.7885, 0.5658), "angle": -35}
        ]
    },   
        "manila_honolulu": {
        "cities": ("manila", "honolulu"),
        "length": 5,
        "segments": [
            {"center": (0.8332, 0.5608), "angle": 20},
            {"center": (0.8605, 0.5736), "angle": 10},
            {"center": (0.8880, 0.5773), "angle": -1},
            {"center": (0.9153, 0.5709), "angle": -13},
            {"center": (0.9414, 0.5562), "angle": -25}
        ]
    },   
        "portmoresby_honolulu": {
        "cities": ("portmoresby", "honolulu"),
        "length": 3,
        "segments": [
            {"center": (0.9239, 0.6570), "angle": -20},
            {"center": (0.9460, 0.6272), "angle": -50},
            {"center": (0.9579, 0.5828), "angle": -80}
        ]
    },   
        "hongkong_tokyo": {
        "cities": ("hongkong", "tokyo"),
        "length": 3,
        "segments": [
            {"center": (0.7873, 0.4365), "angle": -85},
            {"center": (0.7962, 0.3920), "angle": -60},
            {"center": (0.8183, 0.3751), "angle": 15}
        ]
    },   
        "tokyo_petropavlovsk": {
        "cities": ("hongkong", "tokyo"),
        "length": 3,
        "segments": [
            {"center": (0.8412, 0.3443), "angle": 89},
            {"center": (0.8474, 0.2971), "angle": -65}
        ]
    },   
        "petropavlovsk_anchorage": {
        "cities": ("petropavlovsk", "anchorage"),
        "length": 3,
        "segments": [
            {"center": (0.8869, 0.2746), "angle": 15},
            {"center": (0.9144, 0.2751), "angle": -15},
            {"center": (0.9368, 0.2494), "angle": -45}
        ]
    },   
        "tiksi_anchorage": {
        "cities": ("tiksi", "anchorage"),
        "length": 8,
        "segments": [
            {"center": (0.7531, 0.0899), "angle": 5},
            {"center": (0.7803, 0.0935), "angle": 5},
            {"center": (0.8070, 0.0990), "angle": 5},
            {"center": (0.8358, 0.1022), "angle": 5},
            {"center": (0.8625, 0.1097), "angle": 10},
            {"center": (0.8885, 0.1238), "angle": 25},
            {"center": (0.9142, 0.1453), "angle": 30},
            {"center": (0.9381, 0.1724), "angle": 40}
        ]
    },   
        "tokyo_vancouver": {
        "cities": ("tokyo", "vancouver"),
        "length": 6,
        "segments": [
            {"center": (0.8687, 0.3701), "angle": -40},
            {"center": (0.8913, 0.3426), "angle": -35},
            {"center": (0.9162, 0.3223), "angle": -20},
            {"center": (0.9422, 0.3077), "angle": -15},
            {"center": (0.9699, 0.2990), "angle": -8},
            {"center": (0.0254, 0.3183), "angle": 10}
        ]
    },   
        "tiksi_petropavlovsk": {
        "cities": ("tiksi", "petropavlovsk"),
        "length": 7,
        "segments": [
            {"center": (0.7533, 0.1082), "angle": 5},
            {"center": (0.7811, 0.1119), "angle": 5},
            {"center": (0.8078, 0.1165), "angle": 5},
            {"center": (0.8350, 0.1220), "angle": 10},
            {"center": (0.8610, 0.1389), "angle": 30},
            {"center": (0.8769, 0.1751), "angle": 85},
            {"center": (0.8731, 0.2205), "angle": -70}
        ]
    },   
        "tokyo_losangeles_black": {
        "cities": ("tokyo", "losangeles"),
        "length": 7,
        "segments": [
            {"center": (0.8602, 0.4237), "angle": 70},
            {"center": (0.8749, 0.4645), "angle": 50},
            {"center": (0.8975, 0.4911), "angle": 15},
            {"center": (0.9245, 0.4915), "angle": -15},
            {"center": (0.9504, 0.4709), "angle": -35},
            {"center": (0.9692, 0.4366), "angle": -45},
            {"center": (0.0244, 0.4214), "angle": -15}
        ]
    },   
        "tokyo_losangeles_green": {
        "cities": ("tokyo", "losangeles"),
        "length": 7,
        "segments": [
            {"center": (0.8510, 0.4310), "angle": 70},
            {"center": (0.8669, 0.4782), "angle": 50},
            {"center": (0.8954, 0.5076), "angle": 15},
            {"center": (0.9271, 0.5085), "angle": -15},
            {"center": (0.9561, 0.4869), "angle": -35},
            {"center": (0.9782, 0.4484), "angle": -45},
            {"center": (0.0267, 0.4397), "angle": -15}
        ]
    },   
        "tokyo_honolulu": {
        "cities": ("tokyo", "honolulu"),
        "length": 5,
        "segments": [
            {"center": (0.8404, 0.4370), "angle": 70},
            {"center": (0.8541, 0.4823), "angle": 50},
            {"center": (0.8754, 0.5140), "angle": 30},
            {"center": (0.9001, 0.5296), "angle": 13},
            {"center": (0.9278, 0.5351), "angle": 0}
        ]
    },   
        "portmoresby_sydney": {
        "cities": ("portmoresby", "sydney"),
        "length": 3,
        "segments": [
            {"center": (0.9060, 0.7084), "angle": 65},
            {"center": (0.9095, 0.7552), "angle": -80},
            {"center": (0.8985, 0.7983), "angle": -45}
        ]
    },   
        "anchorage_vancouver": {
        "cities": ("anchorage", "vancouver"),
        "length": 2,
        "segments": [
            {"center": (0.0288, 0.2472), "angle": 5},
            {"center": (0.0467, 0.2788), "angle": 85}
        ]
    }
}
