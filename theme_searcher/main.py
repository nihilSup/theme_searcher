import logging
import argparse

from .web import app

def main():
    args = parse_args()
    logging.basicConfig(filename=args.log, level=args.loglevel,
                        format='[%(asctime)s] %(levelname).1s %(message)s',
                        datefmt='%Y.%m.%d %H:%M:%S')
    logging.info("started with args {}".format(args))

    app.run(host="0.0.0.0", port=8000)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--host", type=str, default='localhost',
                        help='hostname to listen')
    parser.add_argument("-p", "--port", type=int, default=8000,
                        help='tcp port to listen')
    parser.add_argument("-l", "--log", action="store", default=None,
                        help='path to log file')
    parser.add_argument('-v', '--verbose', action='store_const',
                        dest='loglevel', const=logging.INFO,
                        help='set logging level INFO', default=logging.INFO)
    parser.add_argument('-d', '--debug', action='store_const',
                        dest='loglevel', const=logging.DEBUG,
                        help='set logging level DEBUG')
    return parser.parse_args()


if __name__ == '__main__':
    main()
