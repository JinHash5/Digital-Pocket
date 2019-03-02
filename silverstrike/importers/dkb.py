import csv
import datetime

from silverstrike.importers.import_statement import ImportStatement


def import_transactions(csv_path):
    lines = []
    with open(csv_path, encoding='latin-1') as csv_file:
        for line in csv.reader(csv_file, delimiter=','):
            print(line)
            # print(len(line))
            if len(line) < 5:
                continue
            try:
                lines.append(ImportStatement(
                    book_date=datetime.datetime.strptime(line[1], '%d.%m.%Y').date(),
                    transaction_date=datetime.datetime.strptime(line[0], '%d.%m.%Y').date(),
                    account=line[3],
                    notes=line[4],
                    title = line[6],
                    iban=line[5],
                    amount=float(line[7].replace('.', '').replace(',', '.'))

                    
                    )
                    
                    )
                # print("Lines")
                # print(lines)
            except Exception as e:
                # first line contains headers
                print("---")
                print(e)
                pass
    return lines
