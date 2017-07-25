import json
from color import UnicodeColors

class Board:
    def load_catalog(board):
        r = requests.get("https://27chan.org/{0}/catalog.json".format(board))
        data = json.loads(r.content.decode("utf-8"))
        return data


class StartPage:
    def __init__(self):
        self.header = None
        self.color = UnicodeColors()

    def chan_logo(self):

        logo = """{0}{1}
 #####   ######   #####  ##  ##   ####   ##   ##
     ##      ##  ##      ##  ##  ##  ##  ###  ##
  ####     ##    ##      ######  ######  ## # ##
 ##        ##    ##      ##  ##  ##  ##  ##  ###
 ######    ##     #####  ##  ##  ##  ##  ##   ##\n{2}{3}""".format(self.color.bold,
                                                                   self.color.warning,
                                                                   self.color.header,
                                                                   self.color.endc)
        return logo

    def get_version_and_author(self):
        with open('version.json') as data_json:
            data = json.load(data_json)
        version = """
    {0}Version:{1} {2}         {0}Author:{1} {3}
 ===============================================\n""".format(self.color.bold,
                                                             self.color.endc,
                                                             data['version'],
                                                             data['author'])
        return version

    def available_boards(self):
        boards = """
                      {0}Boards{1}

   {2}[ {3}b{2} / {3}mod{2} / {3}pol{2} ] [ {3}enter{2} / {3}N64{2} / {3}mu{2} / {3}2d{2} ]
              [ {3}sala{2} / {3}conf{2} / {3}build{2} ]
                     [ {3}pr0n{2} ]{3}{4}\n""".format(self.color.bold,
                                                      self.color.endc,
                                                      self.color.okgreen,
                                                      self.color.header,
                                                      self.color.endc)
        return boards

    def build_header(self):
        s = StartPage()
        self.header = s.chan_logo()
        self.header += s.get_version_and_author()
        self.header += s.available_boards()

        return self.header
