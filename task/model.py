data = list(map(float, open("data/numbers.txt")))

print("Data loaded")

avg = sum(data) / len(data) + 0.01

fmodel = open("result/model.txt", "w")
print(avg, file=fmodel)
fmodel.close()

error = sum(map(lambda x: (x-avg)**2, data)) / len(data)

fmetrics = open("metrics.txt", "w")
print(error, file=fmetrics)
fmetrics.close()

print("Done")
