from typing import List


def find_maximum_distance(number_of_cities: int, cities_with_train_station: List[int] ) -> int:
    max = 0
    if len(cities_with_train_station) > 1:
        for a in range((len(cities_with_train_station) - 1)):
            if a != len(cities_with_train_station):
                b = a + 1
                distance = cities_with_train_station[b] - cities_with_train_station[a]
                if distance <= max:
                    continue
                max = distance
        if number_of_cities - cities_with_train_station[-1] > max:
            max = number_of_cities - cities_with_train_station[-1]
        if cities_with_train_station[0] - 0 > max:
            max = cities_with_train_station[0] - 0
    elif len(cities_with_train_station) == 1:
        if (number_of_cities - 1) - cities_with_train_station[0] > cities_with_train_station[0]:
            max = (number_of_cities - 1) - cities_with_train_station[0]
        else: max = cities_with_train_station[0]
    else: max = number_of_cities
    return print(max)

# if __name__ == "__main__":
#     # These are some of test cases. When evaluating the task, more will be added:
#     assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
#     assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
#     assert (
#         find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
#     )
#     print("ALL TESTS PASSED")

find_maximum_distance(3, [1])
find_maximum_distance(4,[3])
find_maximum_distance(5,[0, 4])