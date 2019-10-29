import argparse


parse = argparse.ArgumentParser()

parse.add_argument('--data', help='ścieżka do pliku z tekstem')
args = parse.parse_args()
