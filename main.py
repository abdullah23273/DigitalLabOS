from memory import MemoryManager
from disk import DiskScheduler
from filesystem import FileSystem
from security import Security
from logger import Logger

mem = MemoryManager()
disk = DiskScheduler()
fs = FileSystem()
sec = Security()
log = Logger()

# ---------------- MEMORY TEST ----------------
pages = [1,2,3,1,4,5]
for p in pages:
    mem.access(p)
mem.report()

# ---------------- FILE SYSTEM ----------------
fs.create_file("root", "a.txt", "Hello OS")

# ---------------- SECURITY TEST ----------------
if sec.check("guest", "delete"):
    fs.delete_file("root", "a.txt")
else:
    log.log("Guest attempted unauthorized delete")

# ---------------- DISK ----------------
disk.add_request(55)
disk.add_request(58)
disk.add_request(10)
disk.add_request(20)
disk.scan()

# ---------------- LOG ----------------
log.log("System execution completed")