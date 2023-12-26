from pathlib import Path
from singletion import singleton
import re


@singleton
class RenameFiles:
    def __init__(self, path: str):
        self.path = Path(path)
        self.compiled_pattern = None


    @property
    def finefile(self):
        yield from self.path.rglob("**/*")


    def compile_regex_pattern(self, pattern_string):
        pattern_string = re.escape(pattern_string)
        self.compiled_pattern = re.compile(pattern_string)


    def replacestring(self):
        if not self.compiled_pattern:
            raise ValueError("Please call the compile_regex_pattern method first")

        for filename in self.finefile:
            if filename.is_file():
                if self.compiled_pattern.search(filename.name):
                    newname = self.compiled_pattern.sub('', filename.name)
                    newpath = filename.with_name(newname)
                    filename.rename(newpath)
                    print(f"[+] {filename.name} renamed to ==> {newname}")


