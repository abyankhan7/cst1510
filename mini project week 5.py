

class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit
    def percent(self):
        percent = (self.value / self.limit) * 100
        return percent
    def status(self):
        # returns the status based on percentage
        percentage = self.percent()
        if percentage >= 100:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

    def is_over(self):
        if self.percent() >= 100:
            return True
        else:
            return False
r1 = Record("R-001", 87, 100)
r2 = Record("R-002", 130, 100)
print(r1.status())
print(r2.status())
def load_records(path):
    records = []
    file = open(path, "r")
    for line in file:
        label,value,limit = line.strip().split(",")
        records.append(Record(label, float(value), float(limit)))
    return records
records = load_records("records_sample.txt")
file2 = open("new_records.txt", "w")
for rec in records:
    file2.write(f"{rec.label},{rec.value},{rec.limit}\n")


over_limit_count = 0
for rec in records:
    if rec.is_over():
        over_limit_count += 1
    print("=" * 34)
    print(f"  RECORD CHECK  -  {rec.label}")
    print(f"  Value         -  {rec.value}")
    print(f"  Limit         -  {rec.limit}")
    print(f"  Status        -  {rec.status()}")
    print("=" * 34)
print(f" There are  {over_limit_count} records with status of OVER LIMIT")
