#!/usr/bin/python3
import argparse
import urllib.request
import os


def read_lines_from(filename):
    if not filename:
        return []
    with open(filename, "r") as f:
        lines = f.readlines()
    return [l.strip() for l in lines]


def download_files(urls, location):
    targets = [l for l in filter(lambda url: url.find(location) != -1, urls)]
    # download the files in a nice little folder
    try:
        os.mkdir('data')
    except Exception:
        pass
    downloaded = []
    count = 0
    for url in targets:
        print(count, len(targets), ':', url)
        # e.g. url
        # http://data.insideairbnb.com/united-states/ca/los-angeles/2015-09-02/data/reviews.csv.gz
        pos = url.find(location)
        tokens = url[pos + len(location):].split('/')
        filename = 'data/' + '_'.join(tokens)
        local_filename, headers = urllib.request.urlretrieve(url, filename)
        downloaded.append(local_filename)
        count += 1
    return downloaded


def process_args(args):
    lines = read_lines_from(args.filename)
    files = download_files(lines, args.location)


def main():
    parser = argparse.ArgumentParser(description='script')
    parser.add_argument('--filename', default='url-list.txt')
    parser.add_argument('--location', default='united-states/ca')
    args = parser.parse_args()
    process_args(args)


if __name__ == "__main__":
    main()
