from os import environ

DEBUG: bool = True if environ.get("DEBUG") == "true" else False

LINE_CHANNEL_SECRET: str = environ.get(
    "LINE_CHANNEL_SECRET", "LINE_CHANNEL_SECRET"
)
LINE_CHANNEL_TOKEN: str = environ.get(
    "LINE_CHANNEL_TOKEN", "LINE_CHANNEL_TOKEN"
)

group = {
    "Ub9a35d8d104346abe6d7d88b8d0e587b": 1,
    "Ua6f729e7b736ff096f385e5441091257": 1,
    "Ufbe7ffaa45015be8dff0c6be67438fe8": 1,
    "Ubd42741617886b9beb0a0c5f6f258e0b": 2,
    "U530fe5cda1022b06c1119a3535ad4c3c": 2,
    "U42116a1849870dfe5bcef92d1ced04f7": 3,
    "U65ab393ef9f0c30c90fcc583c67cad4d": 3,
    "U45623de858046146f67d95e30d0c19d7": 4,
    "Uf3b65fbf5e2b786f7c44149a23a38241": 4,
    "Uf059925dbe8701ef27ef4c7828b9565e": 4,
    "U7c69934c8edddff0b4ef039c85965e1c": 5,
    "U1ff04ba052272478110d45572a9f44c4": 6,
    "Uaf7e5953d20f3452bfa674b65d1ac18b": 6,
    "Uf1921c3d8ba480cd61af06c7b12660c9": 6,
    "U25c5e7b6ccb183b6e8e69d763b021c6d": 7,
    "Uffd172c984d01beae3555ec6cd951f5e": 7,
    "U99af3297894284c14a22f38af5ab4402": 8,
    "Ue70ae03be881e06fcb8c4b6bfbd074ca": 8,
}

lows = [
    "Ub9a35d8d104346abe6d7d88b8d0e587b",
    "Ua6f729e7b736ff096f385e5441091257",
    "Ufbe7ffaa45015be8dff0c6be67438fe8",
    "Ubd42741617886b9beb0a0c5f6f258e0b",
    "U530fe5cda1022b06c1119a3535ad4c3c",
    "U42116a1849870dfe5bcef92d1ced04f7",
    "U65ab393ef9f0c30c90fcc583c67cad4d",
]
mids = [
    "U45623de858046146f67d95e30d0c19d7",
    "Uf3b65fbf5e2b786f7c44149a23a38241",
    "Uf059925dbe8701ef27ef4c7828b9565e",
    "U7c69934c8edddff0b4ef039c85965e1c",
    "U1ff04ba052272478110d45572a9f44c4",
    "Uaf7e5953d20f3452bfa674b65d1ac18b",
    "Uf1921c3d8ba480cd61af06c7b12660c9",
]
highs = [
    "U25c5e7b6ccb183b6e8e69d763b021c6d",
    "Uffd172c984d01beae3555ec6cd951f5e",
    "U99af3297894284c14a22f38af5ab4402",
    "Ue70ae03be881e06fcb8c4b6bfbd074ca",
]
