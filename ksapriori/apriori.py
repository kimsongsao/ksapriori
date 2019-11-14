from ksapriori.generate_candidate import create_c1,create_ck
from ksapriori.scan_dataset import scan_dataset

def apriori(dataset,min_support):
    # start from size 1
    candidate_set1 = list(create_c1(dataset))
    data = list(map(set, dataset))
    candidate_list1, support_data = scan_dataset(data, candidate_set1, min_support)
    #=================================
    candidate_list = [candidate_list1]
    k = 2
    while(len(candidate_list[k-2]) > 0):
        print ('Level : ', len(candidate_list[k-2]))
        candidate_sets =   create_ck(candidate_list[k-2], k)
        candidate_list_k, support_data_k = scan_dataset(data, candidate_sets, min_support)
        support_data.update(support_data_k)
        candidate_list.append(candidate_list_k)
        k += 1
    return candidate_list, support_data
