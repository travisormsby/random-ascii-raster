import random
from sys import argv

def row_values(numcols):
    """
    Generate random values for a row in a raster
    """
    col_list = [str(random.randint(0, 255)) for i in range(numcols)]
    return " ".join(col_list)

def rows(numcols, numrows):
    """
    Generate rows of random values for a raster
    """
    row_list = [row_values(numcols) for i in range(numrows)]
    return "\n".join(row_list)

def write_raster(raster, numcols, numrows):
    """"
    Write data to file, including metadata
    """
    with open(raster, "w", encoding="utf-8") as f:
        f.write(f"NCOLS {numcols}\n")
        f.write(f"NROWS {numrows}\n")
        f.write("XLLCORRER 0\n")
        f.write("YLLCORNER 0\n")
        f.write("CELLSIZE 1\n")
        f.write("NODATA_VALUE -999999\n")
        f.write(rows(numcols, numrows))

if __name__ == "__main__":
    filepath, width, height = argv[1], int(argv[2]), int(argv[3])
    write_raster(filepath, width, height)        
