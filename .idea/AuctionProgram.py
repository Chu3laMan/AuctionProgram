
val = input("What is your name?");
key = input("What is your bidders?");

new_auctionary = {};

def add_auction_toDictionary(key, val):
    new_auctionary[key] = val;

should_continue = True;

while should_continue:
    add_auction_toDictionary(val, key);
    result = input("Type 'Yes' to start over again, Otherwise 'No'.\n");
    if result == "No":
        should_continue = False;
    else:
        val = input("What is your name?");
        key = input("What is your bidders?");
        add_auction_toDictionary(val, key);

print("The winner of this game is ", max(new_auctionary.values()));


