try:
    import django
    print("Django imported successfully")
except ImportError as e:
    print(f"Failed to import Django: {e}")

try:
    from osgeo import gdal
    print("GDAL imported successfully")
except ImportError as e:
    print(f"Failed to import GDAL: {e}")

try:
    from pyproj import Proj
    print("PyProj imported successfully")
except ImportError as e:
    print(f"Failed to import PyProj: {e}")

try:
    import psycopg2
    print("Psycopg2 imported successfully")
except ImportError as e:
    print(f"Failed to import Psycopg2: {e}")