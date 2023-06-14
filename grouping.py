
import json

def knapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    res = K[n][W]
    w = W
    ans = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            ans.append(wt[i - 1])
            res -= val[i - 1]
            w -= wt[i - 1]
    return ans


def find_subgroups(data, target_sum):
    subsets = {}
    for floor, units in data.items():
        arr = list(units.values())
        arr_keys = list(units.keys())
        arr.sort(reverse=True)
        floor_subsets = []
        while sum(arr) >= target_sum:
            subset = knapSack(target_sum, arr, arr, len(arr))
            subset_keys = [arr_keys[arr.index(item)] for item in subset]
            floor_subsets.append((subset_keys, subset))
            for item in subset:
                index = arr.index(item)
                arr.pop(index)
                arr_keys.pop(index)
        if arr:
            floor_subsets.append((arr_keys, arr))
        subsets[floor] = floor_subsets
    return subsets

def startGrouping(data, target_sum = 1000):
    message = ""
    min_length = min(min(d.values()) for d in data.values())
    subgroups = find_subgroups(data, target_sum)
    totalLeftover = 0
    mixedGroup={}
    for floor, subgroups_data in subgroups.items():
        print(f"Floor: {floor}")
        message+=f"Floor: {floor}\n"
        print("Subgroups:")  
        message+="Subgroups:\n"
        for i, (keys, data) in enumerate(subgroups_data):       
            dictionary = dict(zip(keys, data))       
            leftover = target_sum - sum(data)      
            if leftover >= min_length:
                mixedGroup.update(dictionary)
            else:
                print(f"Group {i+1}:")
                message+=f"Group {i+1}:\n"
                print(dictionary, end="  ")           
                message+=str(dictionary)
                print("Leftover:", leftover)
                message+= f"\nLeftover: {leftover}\n"
                totalLeftover+=leftover
        print()
        message+="\n"
    if mixedGroup:
        merged_dict={"Mixed": mixedGroup}
        subgroups = find_subgroups(merged_dict, target_sum)
        for floor, subgroups_data in subgroups.items():
            print(f"Floor: {floor}")
            message+=f"Floor: {floor}\n"
            print("Subgroups:") 
            message+="Subgroups:\n" 
            for i, (keys, data) in enumerate(subgroups_data):       
                dictionary = dict(zip(keys, data))       
                leftover = target_sum - sum(data)      
                print(f"Group {i+1}:")
                message+=f"Group {i+1}:\n"
                print(dictionary, end="  ")
                message+=str(dictionary)
                print("Leftover:", leftover)
                message+= f"\nLeftover: {leftover}\n"
                if leftover < min_length:
                    totalLeftover+=leftover
            print()
            message+="\n"
    print(f"Total leftover: {totalLeftover}")
    message+=f"Total leftover: {totalLeftover}\n" 
    return message   