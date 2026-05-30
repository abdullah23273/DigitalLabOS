class FileSystem:
    def __init__(self):
        self.fs = {"root": {}}

    def create_file(self, folder, name, content):
        if folder not in self.fs:
            self.fs[folder] = {}

        self.fs[folder][name] = content
        print(f"File {name} created in {folder}")

    def read_file(self, folder, name):
        return self.fs[folder].get(name, "File not found")

    def delete_file(self, folder, name):
        if name in self.fs.get(folder, {}):
            del self.fs[folder][name]
            print(f"{name} deleted")