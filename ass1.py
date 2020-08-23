def most_frequent(test):
    all_freq={}

    for i in test:
        if i in all_freq:
            all_freq[i]+=1
        else:
            all_freq[i]=1
    print(str(all_freq))


most_frequent("AAKRUTI") 
