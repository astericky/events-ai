import os

class Paths:
    PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    DATA_DIR = os.path.join(PROJECT_DIR, "data")
    ALL_HTML = os.path.join(DATA_DIR, "all.html")