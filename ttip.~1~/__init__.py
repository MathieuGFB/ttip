"""Tree Tools in Python"""
# ttip/__init__.py

__app_name__ = "ttip"
__version__ = "0.0.3"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    ID_ERROR
) = range(4)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    ID_ERROR: "ttip id error"
}