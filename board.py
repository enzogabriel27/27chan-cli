import json
import datetime
import requests
from color import UnicodeColors


class Thread:
    def __init__(self):
        self.thread_header = None
        self.color = UnicodeColors()

    def thread_json(self, post_number):
        r = requests.get(
            "https://27chan.org/b/res/{0}.json".format(post_number))
        data = json.loads(r.content.decode("utf-8"))
        return data

    def build_thread_header(self, data):
        post_file_unix = data['posts'][0]['tim'] + data['posts'][0]['ext']
        post_file_extension = data['posts'][0]['ext']
        post_file_size = round(float(data['posts'][0]['fsize'] / 1024), 2)
        post_file_resolution = "{0}x{1}".format(data['posts'][0]['w'],
                                                data['posts'][0]['h'])
        post_filename = "{0}{1}".format(data['posts'][0]['filename'],
                                        post_file_extension)
        post_name = data['posts'][0]['name']
        post_date = datetime.datetime.fromtimestamp(
            int(data['posts'][0]['tim']) / 1000).strftime('%d-%m-%Y %H:%M:%S')
        post_number = data['posts'][0]['no']
        post_content = data['posts'][0]['com']
        self.thread_header = """
 {8}{9}{0}{10} ({1}, {2}, {8}{9}{3}{10})
 {11}{4}{10} {5} No. {6}

 {7}\n""".format(post_file_unix,
                 post_file_size,
                 post_file_resolution,
                 post_filename,
                 post_name,
                 post_date,
                 post_number,
                 post_content,
                 self.color.underline,
                 self.color.okblue,
                 self.color.endc,
                 self.color.bold)
        print(self.thread_header)
        return self.thread_header


t = Thread()
t.build_thread_header(t.thread_json('163524'))
