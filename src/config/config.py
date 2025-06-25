import argparse


class Config(object):
    def __init__(self, args=None):
        self.__prog__ = "weather-dashboard"
        self.args = self._parse(args)
        print(self.args.size)

    def _parse(self, args=None):
        """
        Define command line arguments. Long options are used as variable names.
        """

        self.parser = argparse.ArgumentParser(
            prog=self.__prog__,
            description="A PyQt5 Application Displaying Weather Information",
            epilog="Please report bugs to: https://github.com/andrewsb8/weather-dashboard/issues",
        )
        self.parser.add_argument("--test", action="store_true",
                            help="Use test data instead of using weather API.")
        self.parser.add_argument(
            "-s",
            "--size",
            nargs='*',
            default=None,
            help="Input codon sequence string",
        )

        if args is None:
            return self.parser.parse_args()
        else:
            return self.parser.parse_args(args)
