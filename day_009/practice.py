programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as \
      expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#  retrieve an item from a dictionary
print(programming_dictionary["Bug"])

#  adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over \
  again."
print(programming_dictionary)

#  create an empty dictionary
empty_dictionary = {}

#  wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#  edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#  loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#######################################

#  Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#  Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#  Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
             },
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
              "total_visits": 5
              },
}

#  Nesting Dictionaries in Lists

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
        },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
        },
]
