class Logger:
    def log(self, msg):
        with open("logs.txt", "a") as f:
            f.write(msg + "\n")
        print("[LOG]", msg)