class MemoryManager:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.frames = []
        self.page_faults = 0
        self.hits = 0

    def access(self, page):
        if page in self.frames:
            self.hits += 1
            self.frames.remove(page)
            self.frames.append(page)
            print(f"Page {page} -> HIT | Frames: {self.frames}")
        else:
            self.page_faults += 1
            print(f"Page {page} -> FAULT")

            if len(self.frames) >= self.capacity:
                evicted = self.frames.pop(0)
                print(f"Evicted Page: {evicted}")

            self.frames.append(page)

    def report(self):
        total = self.hits + self.page_faults
        fault_rate = (self.page_faults / total) * 100 if total else 0

        print("\n--- MEMORY REPORT ---")
        print("Hits:", self.hits)
        print("Faults:", self.page_faults)
        print("Fault Rate:", round(fault_rate, 2), "%")