'''
Created on Jan 8, 2020

@author: slane
'''
'''
Recurses dictionary entries for the specified value and returns the number of
entries in the recursed paths.
'''
def total_orbital_paths(anydict, key):
    count = 1
    someset = anydict.get(key,set())
    for v in someset:
        count += total_orbital_paths(anydict,v)
    return count


'''
Recurse path for a given planet and capture all nodes on the path.
'''
def orbital_paths(anydict,start,end):
    path = set()
    path.add(start)
    nextnode = anydict.get(start,set())
    while len(nextnode) > 0 and start != end:
        start = next(iter(nextnode))
        path.add(start)
        nextnode = anydict.get(start,set())
    return path
        
inputFile = open("input_part1.txt","r")
orbits = []
galaxy = {}
for line in inputFile.readlines():
    orbits.append(line.rstrip().split(')'))
inputFile.close()

for orbit in orbits:
    orbited = orbit[0]
    orbiter = orbit[1]
    print(orbiter," orbits ",orbited)
    direct_orbits = galaxy.get(orbiter,set())
    if orbited not in direct_orbits:
        direct_orbits.add(orbited)
        galaxy[orbiter] = direct_orbits

orbit_counts = {} 
count = 0       
for key in galaxy.keys():
    subtotal = total_orbital_paths(galaxy,key) - 1
    print("Orbits for",key," is ",subtotal)
    count += subtotal
print ("Done. Here is a view of the galaxy: ",galaxy)
print ("Total orbits (direct and indirect): ",count)

'''
Onto Part 2!
'''
my_orbits = orbital_paths(galaxy,'YOU','COM')
santa_orbits = orbital_paths(galaxy,'SAN','COM')
print("My Orbits (",len(my_orbits),"): ",my_orbits)
print ("Santa's Orbits (",len(santa_orbits),"): ",santa_orbits)
incommon = my_orbits & santa_orbits
print("Nodes in both orbits (",len(incommon),"): ",incommon)

'''
Now go through the intersecting paths and find the distance to those intersections from 
YOU and SAN. The one with with the lowest sum is the solution!
'''
mindist = len(my_orbits) + len(santa_orbits)
for planet in incommon:
    sanlen = len(orbital_paths(galaxy, 'SAN', planet)) - 1
    youlen = len(orbital_paths(galaxy, 'YOU', planet)) - 1
    print ("To ", planet, "SAN distance: ", sanlen," YOU distance: ",youlen)
    currdist = (sanlen + youlen) - 2
    if currdist < mindist:
        mindist = currdist

print ("DONE DONE! Minimum distance is: ",mindist)