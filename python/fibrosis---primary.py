# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"Hyu5000","system":"readv2"},{"code":"H563200","system":"readv2"},{"code":"63174.0","system":"readv2"},{"code":"2680.0","system":"readv2"},{"code":"28229.0","system":"readv2"},{"code":"7994.0","system":"readv2"},{"code":"6051.0","system":"readv2"},{"code":"65060.0","system":"readv2"},{"code":"40953.0","system":"readv2"},{"code":"7791.0","system":"readv2"},{"code":"6837.0","system":"readv2"},{"code":"103753.0","system":"readv2"},{"code":"5519.0","system":"readv2"},{"code":"103559.0","system":"readv2"},{"code":"103472.0","system":"readv2"},{"code":"J84.1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-interstitial-pulmonary-diseases-with-fibrosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fibrosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fibrosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fibrosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
