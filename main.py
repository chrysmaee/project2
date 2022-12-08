import math
import pandas as pd

my_data = pd.read_csv('CS170_Small_Data__88.txt', sep="  ", engine='python', header=None)
# print(my_data)

my_list = my_data.values.tolist()


# def leave_one_out_cross_validation(data, current_set, feature_to_add):
#     number_correctly_classified = 0
#     indices_to_check = current_set.copy()
#     indices_to_check.append(feature_to_add)
#     for record in data:
#         object_to_classify = record[1:len(record)]  # get col 1 to end of list
#         label_of_object_to_classify = record[0]
#         nearest_neighbor_distance = math.inf
#         nearest_neighbor_record = math.inf
#         for other_record in data:
#             if other_record != record:
#                 distance = 0
#                 for x in range(0, len(object_to_classify)):
#                     if x in indices_to_check:
#                         distance += pow(object_to_classify[x] - other_record[x + 1], 2)
#                 distance = math.sqrt(distance)
#                 if distance < nearest_neighbor_distance:
#                     nearest_neighbor_distance = distance
#                     nearest_neighbor_record = other_record
#                     nearest_neighbor_label = other_record[0]
#         if label_of_object_to_classify == nearest_neighbor_label:
#             number_correctly_classified = number_correctly_classified + 1
#     print("Num correct = ", number_correctly_classified, "length of data = ", len(data))
#     accuracy = number_correctly_classified / len(data)
#     return accuracy
#
#
# def feature_search_demo(data):
#     print("There are", len(my_list[0])-1, "features.")
#     print("There are", len(my_list), "records.")
#     current_set_of_features = []
#     list_of_accuracies = []
#     for i in range(1, len(my_list[0])):
#         print("Level", i, "of the search tree.")
#         best_so_far_accuracy = 0
#         for j in range(1, len(my_list[i])):
#             if j not in current_set_of_features:
#                 temp_accuracy = leave_one_out_cross_validation(data, current_set_of_features, j)
#                 print("Using feature(s)", current_set_of_features, j, "accuracy is", temp_accuracy)
#                 if temp_accuracy > best_so_far_accuracy:
#                     best_so_far_accuracy = temp_accuracy
#                     feature_to_add_this_level = j
#         current_set_of_features.append(feature_to_add_this_level)
#         list_of_accuracies.append(best_so_far_accuracy)
#         print("Adding feature", feature_to_add_this_level, "results in an accuracy of", best_so_far_accuracy)
#     highest_accuracy = list_of_accuracies[0]
#     for i in range(0, len(list_of_accuracies)):
#         if list_of_accuracies[i] > highest_accuracy:
#             highest_accuracy = list_of_accuracies[i]
#     print("The best feature subset is", current_set_of_features[0:list_of_accuracies.index(highest_accuracy)+1])
#     print("This subset has an accuracy of", highest_accuracy)


#feature_search_demo(my_list)


def leave_one_out_cross_validation(data, current_set, feature_to_add):
    number_correctly_classified = 0
    indices_to_check = current_set.copy()
    indices_to_check.append(feature_to_add)
    print("Check index", indices_to_check)
    for i in range(1, len(data.index)):
        nearest_neighbor_distance = math.inf
        nearest_neighbor_location = math.inf
        nearest_neighbor_label = 0
        label_of_object_to_classify = data.loc[i, 0]
        object_to_classify = data.loc[i, indices_to_check]
        for k in range(1, len(data.index)):
            if k != i:
                distance = math.sqrt(sum(pow(object_to_classify - data.loc[k, indices_to_check], 2)))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
                    nearest_neighbor_label = data.loc[nearest_neighbor_location, 0]
        if label_of_object_to_classify == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1
    return number_correctly_classified / len(data.index)


def feature_search_demo(data):
    current_set_of_features = []
    set_of_accuracies = []

    for i in range(1, len(data.columns)):
        print("Level", i, "of the search tree")
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0

        for k in range(1, len(data.columns)):
            if k not in current_set_of_features:
                print("  Considering adding feature", k)
                temp_accuracy = leave_one_out_cross_validation(data, current_set_of_features, k)
                print("Using feature", k, "accuracy is", temp_accuracy)
                if temp_accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = temp_accuracy
                    feature_to_add_at_this_level = k
        current_set_of_features.append(feature_to_add_at_this_level)
        set_of_accuracies.append(best_so_far_accuracy)
        print("On level", i, "I added feature", feature_to_add_at_this_level, "to the current set")
        print("Feature", feature_to_add_at_this_level, "had an accuracy of",best_so_far_accuracy)
        print("Current accuracy :", )
    highest_acc = set_of_accuracies[0]
    for i in range(0,len(set_of_accuracies)):
        if highest_acc < set_of_accuracies[i]:
            highest_acc = set_of_accuracies[i]
    print("Highest acc : ", highest_acc)
    print("Using feature subset : ", current_set_of_features[0:set_of_accuracies.index(highest_acc)+1])


feature_search_demo(my_data)

