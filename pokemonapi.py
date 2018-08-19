import requests
import webbrowser


class PokemonAPI:
    def __init__(self, pokemon):
        self.pokeapiurl = "http://pokeapi.co/api/v2/"
        self.pokemon = pokemon
        poke_url = "{purl}pokemon/{pn}".format(purl=self.pokeapiurl,
                                               pn=self.pokemon)
        response = requests.get(poke_url)
        self.data = response.json()
        print("You have chosen {}! Inspired choice!!".format(self.data['name']))

    def pokemon_stats(self):
        print("{p} is {h} feet tall and weighs {w} pounds".format(p=self.data['name'],
                                                                  h=self.data["height"],
                                                                  w=self.data["weight"]))

    def pokemon_games(self):
        games_in = list()
        for game in self.data["game_indices"]:
            games_in.append(game["version"]["name"])
        game_list = "".join(["{}\n".format(g) for g in games_in])
        print("{p} has appear in the following games:\n{gl}".format(p=self.pokemon, gl=game_list))

    def pokemon_type(self):
        p_type = list()
        for _type in self.data["types"]:
            p_type.append(_type["type"]["name"])
        type_str = "".join(["{}\n".format(p) for p in p_type])
        print("{p} is categorized as the following Pokemon type:\n{tl}".format(p=self.pokemon, tl=type_str))

    def pokemon_pic(self):
        urlp = self.data["sprites"]["front_default"]
        webbrowser.open(urlp)


# import pokemonapi
# butterfree = pokemonapi.PokemonAPI("butterfree")
# butterfree.pokemon_stats()
# butterfree.pokemon_games()
# butterfree.pokemon_type()
# butterfree.pokemon_pic()
