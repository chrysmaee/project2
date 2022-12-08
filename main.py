import math
import pandas as pd
import time


def leave_one_out_cross_validation(data, current_set, feature_to_add, forward_or_backward):
    number_correctly_classified = 0
    indices_to_check = current_set.copy()
    if forward_or_backward == "forward":
        indices_to_check.append(feature_to_add)
    if forward_or_backward == "backward":
        indices_to_check.remove(feature_to_add)
    for record in data:
        object_to_classify = record[0:len(record)]
        label_of_object_to_classify = record[0]
        nearest_neighbor_distance = math.inf
        for other_record in data:
            if other_record != record:
                distance = 0
                for x in range(0, len(object_to_classify)):
                    if x in indices_to_check:
                        distance += pow(object_to_classify[x] - other_record[x], 2)
                distance = math.sqrt(distance)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_label = other_record[0]
        if label_of_object_to_classify == nearest_neighbor_label:
            number_correctly_classified = number_correctly_classified + 1
    accuracy = number_correctly_classified / len(data)
    return accuracy


def feature_search_demo():
    text_choice = input("Correctly enter text file name please.")
    start = time.time()
    my_data = pd.read_csv(text_choice, sep="  ", engine='python', header=None)
    data = my_data.values.tolist()
    print("There are", len(data[0]) - 1, "features.")
    print("There are", len(data), "records.")
    user_choice = input("Enter 1 for forward selection\nEnter 2 for backward elimination\n")
    if user_choice == "1":
        current_set_of_features = []
        list_of_accuracies = []
        for i in range(1, len(data[0])):
            print()
            print("--Level", i, "of the search tree.")
            best_so_far_accuracy = 0
            for j in range(1, len(data[0])):
                if j not in current_set_of_features:
                    temp_accuracy = leave_one_out_cross_validation(data, current_set_of_features, j, "forward")
                    print("Using feature(s)", current_set_of_features, "and", j, "accuracy is", temp_accuracy)
                    if temp_accuracy > best_so_far_accuracy:
                        best_so_far_accuracy = temp_accuracy
                        feature_to_add_this_level = j
            current_set_of_features.append(feature_to_add_this_level)
            list_of_accuracies.append(best_so_far_accuracy)
            print("Adding feature", feature_to_add_this_level, "results in an accuracy of", best_so_far_accuracy)
        highest_accuracy = list_of_accuracies[0]
        for i in range(0, len(list_of_accuracies)):
            if list_of_accuracies[i] > highest_accuracy:
                highest_accuracy = list_of_accuracies[i]
        print()
        print("The best feature subset is", current_set_of_features[0:list_of_accuracies.index(highest_accuracy) + 1])
        print("This subset has an accuracy of", highest_accuracy)
    if user_choice == "2":
        current_set_of_features = []
        for i in range(1, len(data[0])):
            current_set_of_features.append(i)
        list_of_accuracies = []
        list_of_sets = []
        for i in reversed(range(1, len(data[0]))):
            print()
            print("--Level", i, "of the search tree.")
            best_so_far_accuracy = 0
            feature_to_remove_this_level = 0
            for j in reversed(range(1, len(data[0]))):
                if j in current_set_of_features:
                    temp_accuracy = leave_one_out_cross_validation(data, current_set_of_features, j, "backward")
                    print("Using feature(s)", current_set_of_features, "without", j, "accuracy is", temp_accuracy)
                    if temp_accuracy > best_so_far_accuracy:
                        best_so_far_accuracy = temp_accuracy
                        feature_to_remove_this_level = j
            current_set_of_features.remove(feature_to_remove_this_level)
            list_of_accuracies.insert(0, best_so_far_accuracy)
            list_of_sets.insert(0, feature_to_remove_this_level)
            print("Removing feature", feature_to_remove_this_level, "results in an accuracy of", best_so_far_accuracy)
        highest_accuracy = list_of_accuracies[0]
        for i in range(0, len(list_of_accuracies)):
            if list_of_accuracies[i] > highest_accuracy:
                highest_accuracy = list_of_accuracies[i]
        print()
        print("The best feature subset is", list_of_sets[0:list_of_accuracies.index(highest_accuracy)])
        print("This subset has an accuracy of", highest_accuracy)
    end = time.time()
    total_time = end - start
    print()
    print("Execution time in seconds:", round(total_time))


feature_search_demo()

