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
    }

}
