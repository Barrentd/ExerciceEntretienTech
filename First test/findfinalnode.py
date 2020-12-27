#import sys
#import math

"""Function for finding the endpoint of a network"""

def find_network_endpoint(start_node_id, from_ids, to_ids):

    """[summary]
    """

    res = 0
    for index, val1 in enumerate(from_ids):
        print("Enter", start_node_id)
        if val1 == start_node_id:
            for idx_next, val2 in enumerate(to_ids):
                if index == idx_next:
                    print("idxnext", idx_next, "val", val2)
                    res = val2
                find_network_endpoint(res, from_ids, to_ids)
    return 0

def main():

    """[summary]
    """

    start_node_id = 6
    from_ids = [4, 9, 6, 1]
    to_ids = [9, 5, 1, 4]
    endpoint = find_network_endpoint(start_node_id, from_ids, to_ids)
    print(endpoint)

if __name__ == "__main__":
    main()
