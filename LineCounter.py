'''
Created on Jun 14, 2016

@author: atorr
'''
import os

class Counter():
    IGNORED_FOLDERS = [".git"]
    IGNORED_FILES = [".gitignore", ".gitattributes", ".project", ".pydevproject"]
    
    def __init__(self):
        self.counter = 0
        
    def countLines(self, filepath, filename):
        if (filename in self.IGNORED_FILES):
            return 0
        lines = 0
        print(filename)
        try:
            with open(filepath) as f:
                lines += len(f.readlines())
        except Exception as e:
            print("Not a Text File")
            return 0
        print(lines)
        return lines
        
    def goThroughDirectories(self, path):
        for item in os.listdir(path):
            if not item in self.IGNORED_FOLDERS:
                dir = os.path.join(path, item)
                if (os.path.isdir(dir)):
                    self.goThroughDirectories(dir)
                else:
                    self.counter += self.countLines(dir, item)
    
    def getCount(self):
        return self.counter
    
if __name__ == "__main__":
    print("Note: The directory should be the source code folder to avoid confusion with other files")
    
    directory = input("Enter the project directory you wish to count:")
    counter = Counter()
    print()
    counter.goThroughDirectories(directory)
    lines = counter.getCount()
    print("\nThere are "+str(lines)+" lines in this project.\n")
    input("Press any key to exit...")