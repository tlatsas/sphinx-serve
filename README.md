sphinx-serve
------------

Simple utility to easier preview your sphinx documentation.

After running the sphinx-serve command, it tries to detect the
sphinx build directory. It examines the current working directory
and if the build directory is not present, it tries to iterate
the parent paths. If a build directory is detected it launches
an http server.

The build directory name is configurable. It also supports serving
documentation from the html folder of the singlehtml folder.

Installation
------------

    pip install sphinx-serve

Usage
-----
Synopsis:

    usage: sphinx-serve [--help] [-v] [-h HOST] [-p PORT] [-b BUILD] [-s]

Arguments:

* `--help`: show help and exit
* `--version`, `-v`: show program version and exit
* `--host`, `-h`: listen to the given hostname (default: 0.0.0.0)
* `--port`, `-p`: listen to the given port (default: 8081)
* `--build`, `-b`: sphinx build directory name (default: "_build")
* `--single`, `-s`: serve the single-html version instead of the normal one

Run with:

    sphinx-serve

