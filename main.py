import math
import pandas as pd

my_data = pd.read_csv('smallest.txt', sep="  ", engine='python', header=None)
# print(my_data)

my_list = my_data.values.tolist()


# print(my_list)


# for i in range(len(my_list)):  # num row
#     for j in range(len(my_list[i])):  # length of the list in the list
#         print(my_list[i][j], end=" ")
#     print()


def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correctly_classified = 0
    indices_to_check = current_set.copy()
    indices_to_check.append(feature_to_add)
    print("Indices to check:", indices_to_check)
    for record in data:
        object_to_classify = record[1:len(record)]  # get col 1 to end of list
        label_of_object_to_classify = record[0]
        nearest_neighbor_distance = math.inf
        nearest_neighbor_record = math.inf
        # print()
        for other_record in data:
            if record != other_record:
                # print("Asking if", other_record, "is nearest neighbor to", record)
                distance = 0
                for x in range(0, len(record) - 1):
                    if x in indices_to_check:
                        distance += pow(object_to_classify[x] - other_record[x + 1], 2)
                distance = math.sqrt(distance)
                # print(distance)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_record = other_record
                    nearest_neighbor_label = other_record[0]
        if label_of_object_to_classify == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1
        # print("Record", record, "is class", record[0])
        # print("Its nearest neighbor is", nearest_neighbor_record, "which is in class", nearest_neighbor_record[0])
        # print("Record is class", label_of_object_to_classify)
        # print("Nearest record is class", nearest_neighbor_label)
    accuracy = number_correctly_classified / len(data)
    # print(accuracy)
    return accuracy


def feature_search_demo(data):
    current_set_of_features = []
    for i in range(1, len(my_list[0])):
        print("Level", i, "of the search tree.")
        # feature_to_add_this_level = []
        best_so_far_accuracy = 0
        for j in range(1, len(my_list[i])):
            print("Testing feature", j)
            print("Set:", current_set_of_features)
            if j not in current_set_of_features:
                temp_accuracy = leave_one_out_cross_validation(data, current_set_of_features, j)
                print("Using feature(s)", current_set_of_features, j, "accuracy is", temp_accuracy)
                if temp_accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = temp_accuracy
                    feature_to_add_this_level = j
        current_set_of_features.append(feature_to_add_this_level)
        print("Feature", feature_to_add_this_level, "was the best with an accuracy of", best_so_far_accuracy)


feature_search_demo(my_list)

# for i in len(my_data.index):
#     obj = my_data.loc[i, 1:len(my_data.columns)]
#     label = my_data.loc[i, 0]
#     print(i, "is of type", label)
#     for k in range(0, len(my_data.index)):
#         print("Ask if", i, "is nearest to", k)


# def leave_one_out_cross_validation(data, current_set, feature_to_add):
#     number_correctly_classified = 0
#     for i in range(1, len(data.index)):
#         nearest_neighbor_distance = math.inf
#         nearest_neighbor_location = math.inf
#         label_of_object_to_classify = data.loc[i, 0]
#         object_to_classify = data.loc[i, 1:6]
#         for k in range(1, len(data.index)):
#             if k != i:
#                 distance = math.sqrt(sum(pow(object_to_classify - data.loc[k, 1:6], 2)))
#                 print("obj", object_to_classify)
#                 print()
#                 print("data", data.loc[k, 1:6])
#                 print()
#                 print("Distance = ", distance)
#                 if distance < nearest_neighbor_distance:
#                     nearest_neighbor_distance = distance
#                     nearest_neighbor_location = k
#                     nearest_neighbor_label = data.loc[nearest_neighbor_location, 0]
#         #print("Label of object is", label_of_object_to_classify)
#         #print("It's nearest neighbor is", nearest_neighbor_label)
#         if label_of_object_to_classify == nearest_neighbor_label:
#             number_correctly_classified = number_correctly_classified + 1
#     #print("Num correct", number_correctly_classified)
#     #print("length", len(data.index))
#     return number_correctly_classified / len(data.index)
#
#
# leave_one_out_cross_validation(my_data, [], [])

# def feature_search_demo(data):
#     current_set_of_features = []
#
#     for i in range(1, len(data.columns)):
#         print("Level", i, "of the search tree")
#         feature_to_add_at_this_level = []
#         best_so_far_accuracy = 0
#
#         for k in range(1, len(data.columns)):
#             if k not in current_set_of_features:
#                 print("  Considering adding feature", k)
#                 temp_accuracy = leave_one_out_cross_validation(data, current_set_of_features, k + 1)
#                 print("Using feature", k, "accuracy is", temp_accuracy)
#                 if temp_accuracy > best_so_far_accuracy:
#                     best_so_far_accuracy = temp_accuracy
#                     feature_to_add_at_this_level = k
#         current_set_of_features.append(feature_to_add_at_this_level)
#         print("On level", i, "I added feature", feature_to_add_at_this_level, "to the current set")
#         print("Feature", feature_to_add_at_this_level, "had an accuracy of",best_so_far_accuracy)
#         print("Current accuracy :", )
#
#
# feature_search_demo(my_data)
