#import sys
#import math

"""Function for finding the endpoint of a network"""

def find_network_endpoint(start_node_id, from_ids, to_ids):

    """Browse the array to find the final node"""

    for index, val1 in enumerate(from_ids):
        #print(start_node_id)
        if val1 == start_node_id:
            for idx_next, val2 in enumerate(to_ids):
                if index == idx_next:
                    #print("idxnext", idx_next, "val", val2)
                    start_node_id = val2
                    break
            break

    check_number = 0

    for index, val1 in enumerate(from_ids):
        if val1 == start_node_id:
            check_number = 1
    
    if check_number == 1:
        start_node_id = find_network_endpoint(start_node_id, from_ids, to_ids)

    return start_node_id


def main():

    """Main function"""

    start_node_id = 6
    from_ids = [4, 9, 6, 1]
    to_ids = [9, 5, 1, 4]
    endpoint = find_network_endpoint(start_node_id, from_ids, to_ids)
    print(endpoint)
    endpoint2 = find_network_endpoint(start_node_id, to_ids, from_ids)
    print(endpoint2)

if __name__ == "__main__":
    main()
