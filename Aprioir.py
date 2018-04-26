from apyori import apriori

transactions = [
    ['I1','I2','I5'],
    ['I2','I4'],
    ['I2','I3'],
    ['I1','I2','I4'],
    ['I1','I3'],
    ['I2','I3'],
    ['I1','I3'],
    ['I1','I2','I3','I5'],
    ['I1','I2','I3']
]

results = list(apriori(transactions,min_support=0.2,min_confidence=0.7))
print(results)