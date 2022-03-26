import argparse

from pytube import YouTube


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "url",
        help="YouTube video's url to download"
    )

    args = parser.parse_args()

    try:
        yt = YouTube(args.url)
        yt.streams
        ... .filter(progressive=True, file_extension='mp4')
        ... .order_by('resolution')
        ... .desc()
        ... .first()
        ... .download()
    except:
        print("Some Error!")
    print('Task Completed!')


if __name__ == "__main__":
    main()
