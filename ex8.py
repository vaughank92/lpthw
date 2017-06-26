#set up the format of the string
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
#just replicates formatter as a string across
print formatter % (formatter, formatter, formatter, formatter)

#But it didn't sing will be in double quotes because
# of the ' in didn't
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
