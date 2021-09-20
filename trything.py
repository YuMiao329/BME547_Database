oed = {"day": "when the sun is up", "night":"when the moon is out"}
print(oed)
print(oed["day"])
print(oed["night"])
print(oed.keys())
print(oed.values())
oed["lunch"] = "what I will eat after class"
print(oed)
oed["pi"] = 3.1415
print(oed)
area = oed["pi"] * 2 * (5)**2
print(area)
oed["prime numbers"] = [1,2,3,5,7,11]
print(oed)
for x in oed["prime numbers"]:
    print(x)
oed.get("dinner")
print(oed.get("dinner"))
print(oed.get("lunch"))
oed["nil"] = None
print(oed)
x = "lunch"
print(oed[x])
# if got iterate the dictionary, it will iterate keys
for i in oed:
    print(i)
for i in oed:
    print("the key is {}. The value is {}".format(i, oed[i]))