# NAME: Drew Inman DATE: 10/14/19 PROJECT: ICS 352 Assignment 1
#
# DESCRIPTION: We're implementing Naive Bayes Classifier. One version where we
# can't use scikit-learn and one version where we use scikit-learn. Then, we
# compare the accuracy of both versions! My prediction has scikit-learn's
# version being more accurate, but I guess we'll find out!
#
import sys

print("processing training data...")

# data creation
# [outlook, temp, humid, wind]
#
# outlook ||  sunny = 0, overcast = 1, rain = 2
#    temp ||   cold = 0,     mild = 1, hot = 2
#   humid || normal = 0,     high = 1
#    wind ||   weak = 0,   strong = 1
#  yes/no ||     no = 0,      yes = 1
raw_data = [0, 2, 1, 0, 0], [0, 2, 1, 1, 0], [1, 2, 1, 0, 1],\
            [2, 1, 1, 0, 1], [2, 0, 0, 0, 1], [2, 0, 0, 1, 0],\
            [1, 0, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 1],\
            [2, 1, 0, 0, 1], [0, 1, 0, 1, 1], [1, 1, 1, 1, 1],\
            [1, 2, 0, 0, 1], [2, 1, 1, 1, 0]

# This is where the data and target from raw_data will be stored
data = []
target = []

# These will store data for the yes and nos
yes_count = 0
no_count = 0
# sunny, overcast, rain
outlook_yes = [0, 0, 0]
outlook_no = [0, 0, 0]
# cold, mild, hot
temp_yes = [0, 0, 0]
temp_no = [0, 0, 0]
# normal, high
humid_yes = [0, 0]
humid_no = [0, 0]
# weak strong
wind_yes = [0, 0]
wind_no = [0, 0]

# We bouta use the list above to make data and target
for x in range(len(raw_data)):
    data.append([raw_data[x][0], raw_data[x][1], raw_data[x][2], raw_data[x][3]])
    target.append(raw_data[x][4])
    if raw_data[x][4] == 1:  # if target is yes
        yes_count += 1
        # outlook_yes
        if raw_data[x][0] == 0:
            outlook_yes[0] += 1
        if raw_data[x][0] == 1:
            outlook_yes[1] += 1
        if raw_data[x][0] == 2:
            outlook_yes[2] += 1
        # temp_yes
        if raw_data[x][1] == 0:
            temp_yes[0] += 1
        if raw_data[x][1] == 1:
            temp_yes[1] += 1
        if raw_data[x][1] == 2:
            temp_yes[2] += 1
        # humid_yes
        if raw_data[x][2] == 0:
            humid_yes[0] += 1
        if raw_data[x][2] == 1:
            humid_yes[1] += 1
        # wind_yes
        if raw_data[x][3] == 0:
            wind_yes[0] += 1
        if raw_data[x][3] == 1:
            wind_yes[1] += 1
    if raw_data[x][4] == 0:  # if target is no
        no_count += 1
        # outlook_no
        if raw_data[x][0] == 0:
            outlook_no[0] += 1
        if raw_data[x][0] == 1:
            outlook_no[1] += 1
        if raw_data[x][0] == 2:
            outlook_no[2] += 1
        # temp_no
        if raw_data[x][1] == 0:
            temp_no[0] += 1
        if raw_data[x][1] == 1:
            temp_no[1] += 1
        if raw_data[x][1] == 2:
            temp_no[2] += 1
        # humid_no
        if raw_data[x][2] == 0:
            humid_no[0] += 1
        if raw_data[x][2] == 1:
            humid_no[1] += 1
        # wind_no
        if raw_data[x][3] == 0:
            wind_no[0] += 1
        if raw_data[x][3] == 1:
            wind_no[1] += 1

print("processing complete!")
print("new instance: (outlook = sunny, temperature = cool, humidity = high, wind = strong)")
print("should we go play tennis today?")

# hardcoded in sunny, cool, high humid, strong wind
yes_percent = ((outlook_yes[0]/yes_count) * (temp_yes[0]/yes_count)
               * (humid_yes[1]/yes_count) * (wind_yes[1]/yes_count)
               * (yes_count/len(target)))
no_percent = ((outlook_no[0]/no_count) * (temp_no[0]/no_count)
              * (humid_no[1]/no_count) * (wind_no[1]/no_count)
              * (no_count/len(target)))

yes_end = yes_percent/(yes_percent+no_percent)
no_end = no_percent/(no_percent+yes_percent)

if yes_end > no_end:
    print("yes")
else:
    print("no\n")

print("train/test data split")
# we split the data here, the code earlier is for checking the new instance
# WORK ON THE SECTION BELOW
user_input = 0
print("how to split data?")
print("0 for 0%/100%, .5 for 50%/50%, .75 for 75%/25%, 1.0 for 100%/0%, etc")
while user_input == 0:
    split = float(input(">> "))
    if split > 1 or split < 0:
        split = 0
        print("invalid input. please choose from 0.0 to 1.0")
        continue
    else:
        user_input = 1

if split == 1:
    print("no testing data since split was 100%/0%")
    print("exiting...")
    sys.exit()
elif split == 0:
    print("no training data since split was 0%/100%")
    print("exiting...")
    sys.exit()
else:
    data_split = round(float(split*len(data)))

    print("splitting data...")
    print("calculating results...")
    # These will store data for the yes and nos
    yes_count = 0
    no_count = 0
    # sunny, overcast, rain
    outlook_yes = [0, 0, 0]
    outlook_no = [0, 0, 0]
    # cold, mild, hot
    temp_yes = [0, 0, 0]
    temp_no = [0, 0, 0]
    # normal, high
    humid_yes = [0, 0]
    humid_no = [0, 0]
    # weak strong
    wind_yes = [0, 0]
    wind_no = [0, 0]
    for x in range(0, data_split):
        if raw_data[x][4] == 1:  # if target is yes
            yes_count += 1
            # outlook_yes
            if raw_data[x][0] == 0:
                outlook_yes[0] += 1
            if raw_data[x][0] == 1:
                outlook_yes[1] += 1
            if raw_data[x][0] == 2:
                outlook_yes[2] += 1
            # temp_yes
            if raw_data[x][1] == 0:
                temp_yes[0] += 1
            if raw_data[x][1] == 1:
                temp_yes[1] += 1
            if raw_data[x][1] == 2:
                temp_yes[2] += 1
            # humid_yes
            if raw_data[x][2] == 0:
                humid_yes[0] += 1
            if raw_data[x][2] == 1:
                humid_yes[1] += 1
            # wind_yes
            if raw_data[x][3] == 0:
                wind_yes[0] += 1
            if raw_data[x][3] == 1:
                wind_yes[1] += 1
        if raw_data[x][4] == 0:  # if target is no
            no_count += 1
            # outlook_no
            if raw_data[x][0] == 0:
                outlook_no[0] += 1
            if raw_data[x][0] == 1:
                outlook_no[1] += 1
            if raw_data[x][0] == 2:
                outlook_no[2] += 1
            # temp_no
            if raw_data[x][1] == 0:
                temp_no[0] += 1
            if raw_data[x][1] == 1:
                temp_no[1] += 1
            if raw_data[x][1] == 2:
                temp_no[2] += 1
            # humid_no
            if raw_data[x][2] == 0:
                humid_no[0] += 1
            if raw_data[x][2] == 1:
                humid_no[1] += 1
            # wind_no
            if raw_data[x][3] == 0:
                wind_no[0] += 1
            if raw_data[x][3] == 1:
                wind_no[1] += 1

    prediction = []
    test_target = []
    for x in range(data_split, len(data)):
        test_target.append(target[x])
        outlook = data[x][0]
        temp = data[x][1]
        humid = data[x][2]
        wind = data[x][3]

        yes_percent = ((outlook_yes[outlook] / yes_count) * (temp_yes[temp] / yes_count)
                       * (humid_yes[humid] / yes_count) * (wind_yes[wind] / yes_count)
                       * (yes_count / data_split))
        no_percent = ((outlook_no[outlook] / no_count) * (temp_no[temp] / no_count)
                      * (humid_no[humid] / no_count) * (wind_no[wind] / no_count)
                      * (no_count / data_split))

        yes_end = yes_percent / (yes_percent + no_percent)
        no_end = no_percent / (no_percent + yes_percent)

        if yes_end > no_end:
            prediction.append(1)
        else:
            prediction.append(0)

    # the section below is for accuracy on my implementation
    correct_values = 0
    for x in range(len(test_target)):
        if prediction[x] == test_target[x]:
            correct_values += 1

    accuracy = (correct_values / len(test_target)) * 100

    print("accuracy:", accuracy, "%")
