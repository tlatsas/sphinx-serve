import os
import argparse
from . import __version__
from . import __doc__

try:
    from http.server import HTTPServer
    from http.server import SimpleHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler


def cli():
    """Parse options from the command line"""
    parser = argparse.ArgumentParser(prog="sphinx-serve",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     conflict_handler="resolve",
                                     description=__doc__
                                     )

    parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s {0}".format(__version__)
                        )

    parser.add_argument("-h", "--host", action="store",
                        default="0.0.0.0",
                        help="Listen to the given hostname"
                        )

    parser.add_argument("-p", "--port", action="store",
                        type=int, default=8081,
                        help="Listen to given port"
                        )

    parser.add_argument("-b", "--build", action="store",
                        default="_build",
                        help="Build folder name"
                        )

    parser.add_argument("-s", "--single", action="store_true",
                        help="Serve the single-html documentation version"
                        )

    return parser.parse_args()


def find_build_dir(path, build="_build"):
    """try to guess the build folder's location"""
    path = os.path.abspath(os.path.expanduser(path))
    contents = os.listdir(path)
    filtered_contents = [directory for directory in contents
                            if os.path.isdir(os.path.join(path, directory))]

    if build in filtered_contents:
        return os.path.join(path, build)
    else:
        if path == os.path.realpath("/"):
            return None
        else:
            return find_build_dir("{0}/..".format(path), build)


def main():
    opts = cli()
    path = find_build_dir(os.getcwd(), opts.build)
    if path is None:
        print(":: Cound not find build folder \"{0}\"".format(opts.build))
        return 1

    # change to the documentation path
    if opts.single:
        document_directory = "singlehtml"
    else:
        document_directory = "html"

    path = os.path.join(path, document_directory)
    os.chdir(path)

    print(":: Found documentation at: {0}".format(path))
    print(":: Serving documentation at http://{0}:{1}".
        format(opts.host, opts.port))
    print(":: Terminate with Ctrl-C")
    try:
        httpd = HTTPServer((opts.host, opts.port), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(":: Keyboard interrupt received, exiting.")

    return 0
