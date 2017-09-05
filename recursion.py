# recursion can solve the problem of determining key location in various nested boxes

# base case VS recursive case
# recursive case is when the function calls itself
# base case is when the function does not call itself (prevents infinite loop)

# pseudocode

# Type A
# make a pile of boxes to look through
# while pile isn't empty
# grab a box
# if a key is found, you're finished
# if a box is found, add to pile of boxes
# Go back to pile

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print "found the key!"

# Type B
# go through every item in box
# if a key is found, you're finished
# if a box is found, return to step 1

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print "found the key!"

# recursion is used for when the solution is simpler
# loops can be more efficient

def countdown(i):
    print i
    # base case
    if i <= 1:
        return
    # recursive case
    else:
        countdown(i-1)
