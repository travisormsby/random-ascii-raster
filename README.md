Generate a random ASCII format raster image. Useful for generating rasters for understanding how GIS tools work. Unlike tools built in to GIS software for generating random rasters, a small text file allows you easily manually alter cell values. This is impractical for large rasters, but useful for tweaking toy datasets.

usage: python random-ascii-raster.py filepath width height
example: python random-ascii-raster.py images/raster.asc 10 10
This will create a file called raster.asc in the images directory with a width of 10 cells and a height of 10 cells

The cell size is 1 meter, the positioning is at 0,0. The raster does not have a projection defined.
