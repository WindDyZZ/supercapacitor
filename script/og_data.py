from ui.models import Data
import csv

def run():
    with open('.\Heteroatomdopedgraphene.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Data.objects.all().delete()

        for row in reader:
            print(row)
            if row[0] == "1":
                electrolyte_class = 'salt'
            elif row[1] == "1":
                electrolyte_class = 'base'
            elif row[2] == "1":
                electrolyte_class = 'acid'
            else:
                electrolyte_class = 'none'

            for i in range(3, len(row)):  # Start at index 3
                if row[i] == "":
                    row[i] = "0.00"
                row[i] = float(row[i])  # Convert to float

            data = Data(
                elec_class=electrolyte_class,
                ssa=row[3],
                id_ig_ratio=row[4],
                nitrogen=row[5],
                oxygen=row[6],
                sulphur=row[7],
                density=row[8],
                predicted_value=row[9]
            )

            data.save()
