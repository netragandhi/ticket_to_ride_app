SEGMENT_SIZE = (0.026, 0.016)
ROUTES = { #maybe implement it so i can change the empty image
    "miami_caracas": {
        "length": 2,
        "segments": [
            {"center": (0.1832, 0.5099), "angle": 9},
            {"center": (0.1976, 0.5433), "angle": 85}  # positive = CCW
        ]
    },
        "daressalaam_djibouti": {
        "length": 1,
        "segments": [
            {"center": (0.5462, 0.6217), "angle": 100}  # positive = CCW
        ]
    },
        "edinburgh_hamburg": {
        "length": 1,
        "segments": [
            {"center": (0.4257, 0.2568), "angle": 9}  # positive = CCW
        ]
    }
}
