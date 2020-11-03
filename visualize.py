# -*- encoding: utf-8 -*-

import argparse
import os
import stl
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def main(infilename, save=False):
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    # Load the STL files
    m = mesh.Mesh.from_file(infilename)
    # Save numpy-ascii
    if save:
        m.save(f"numpy-ascii-{os.path.basename(infilename)}", mode=stl.Mode.ASCII)
    
    # Add the vectors to the plot
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(m.vectors))

    # Auto scale to the mesh size
    scale = m.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.show()

if __name__ == '__main__':
    program_args = argparse.ArgumentParser(description='STL Visualizer')
    program_args.add_argument('-i', '--inputfile' , required=True,  help="Input file path")
    program_args.add_argument('-s', '--save' ,type=bool, required=False,  help="Save numpy-ASCII Format")

    args = program_args.parse_args()

    if args.inputfile:
        infilename = args.inputfile
        assert ".stl" in infilename.lower(), 'unsupported file : "it supports .STL File Format"'
        
    main(infilename, args.save)