Batches = {"PPA":18500,"LB":18700,"PYTHON":18900,"LSP":19100,"C#":19300,"ANGULAR":19500}

print(Batches)

print(type(Batches))
print(len(Batches))

print(Batches["PYTHON"])

for value in Batches:
    print("Batch Name : ",value)
    print("Batch Fees : ",Batches[value])
    print()

   