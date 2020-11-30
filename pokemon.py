def pokemon_name(file):
    pokeFile = file.read()
    pokeRe = re.compile(r'\w+')
    pokeList = pokeRe.findall(pokeFile)

    current = []
    longest = []

    def firstletter(lastletter, namelist):
        for index, name in enumerate(namelist):
            if name.startswith(lastletter):
                return index
        return False

    for name in pokeList:
        currentName = name
        current.append(currentname)
        pokelist = pokeList[:]
        pokelist.pop(pokeList.index(currentname))
        index = firstletter(currentName[-1],pokelist)

        while index is not False:
            currentname = pokelist[index]
            current.append(currentname)
            pokelist.pop(index)
            index = firstletter(currentname[-1],pokelist)

        if len(current) > len(longest):
            longest = current

if __name__ == "__main__":
    print(pokemon_name("pokemonnames"))
        
