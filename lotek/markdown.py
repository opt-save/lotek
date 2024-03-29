from markdown import Markdown


class MarkdownParser:

    def __init__(self, config):
        pass

    def parse(self, content):
        md = Markdown(extensions = ['meta'])
        lines = content.split('\n')
        for prep in md.preprocessors:
            lines = prep.run(lines)
        return md.Meta, '\n'.join(lines)

    def convert(self, content):
        md = Markdown(extensions = ['meta'])
        html = md.convert(content)
        d = md.Meta.copy()
        d["content"] = html
        return d
