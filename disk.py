class DiskScheduler:
    def __init__(self, head=50):
        self.requests = []
        self.head = head
        self.seek_time = 0

    def add_request(self, req):
        self.requests.append(req)

    def scan(self):
        print("\n--- DISK SCAN SCHEDULING ---")

        left = sorted([r for r in self.requests if r < self.head])
        right = sorted([r for r in self.requests if r >= self.head])

        sequence = right + left[::-1]

        current = self.head
        print(f"Initial Head Position: {self.head}")

        for track in sequence:
            print(f"Move {current} → {track}")
            self.seek_time += abs(current - track)
            current = track

        print("Total Seek Time:", self.seek_time)