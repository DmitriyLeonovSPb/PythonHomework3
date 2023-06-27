CampingBook = {'Pavel': ('AK47', 'knife', 'water'), 'Oleg': ('navigator', 'AK47', 'compas'), 'Ivan': ('tent', 'AK47', 'sault')}
CampStuff = list(CampingBook.values())
CommonThing = set(CampStuff[0])
for items in CampStuff:
    CommonThing = CommonThing.intersection(set(items))
print("Общая вещь: ", CommonThing)
IndividualStuff = {}
for name, items in CampingBook.items():
    IndividualStuff[name] = set(items).difference(CommonThing)
print("Список уникальных вещей: ", IndividualStuff)