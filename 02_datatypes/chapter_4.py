#boolean

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"total_actions: {total_actions}")

milk_present = None #no milk
print(f"is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

#and, or, not

can_serve = water_hot and tea_added
print(f"can serve chai? {can_serve}")


