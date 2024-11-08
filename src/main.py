import bencodepy

def main():
    with open('../torrentTest/puppy.torrent', 'rb') as file:
        torrent = bencodepy.decode(file.read())
        print(torrent[b'announce'].decode('utf-8'))

if __name__ == "__main__":
    main()
