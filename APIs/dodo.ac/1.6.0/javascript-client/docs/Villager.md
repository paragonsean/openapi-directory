# Nookipedia.Villager

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altName** | **String** | A previous name for the villager. A very small number of villagers changed names between earlier games, such as Sally being known as Hazel in the original game. | [optional] 
**appearances** | **[String]** | List of official media the villager appeared in. &#x60;DNM&#x60; is *Doubutsu no Mori* for the Nintendo 64 (Japan-exclusive); &#x60;AC&#x60; is *Animal Crossing* for GameCube; &#x60;E_PLUS&#x60; is *Doubutsu no Mori e+* for GameCube (expanded port of AC, Japan-exclusive); &#x60;WW&#x60; is *Wild World* for the DS; &#x60;CF&#x60; is *City Folk* for Wii; &#x60;NL&#x60; is *New Leaf* for 3DS; &#x60;WA&#x60; is *Welcome amiibo*, the *New Leaf* expansion; &#x60;NH&#x60; is *New Horizons* for Switch; &#x60;FILM&#x60; is the *Doubutsu no Mori* Japan-exclusive film; &#x60;HHD&#x60; is *Happy Home Designer* for the Wii; and &#x60;PC&#x60; is *Pocket Camp* for mobile. | [optional] 
**birthdayDay** | **String** | Birthday day of the villager. Note that villager birthdays were not introduced until *Wild World*. For villagers who didn&#39;t appear in *Wild World* or any later games, this field will be an empty string. | [optional] 
**birthdayMonth** | **String** | Birthday month of the villager. Note that villager birthdays were not introduced until *Wild World*. For villagers who didn&#39;t appear in *Wild World* or any later games, this field will be an empty string. | [optional] 
**clothing** | **String** | The villager&#39;s default clothing. This will be the clothing from the latest game (i.e. if the villager had varying phrases between *Wild World* and *New Horizons*, this will be the *New Horizons* clothing). | [optional] 
**debut** | **String** | The first *Animal Crossing* game the villager appeared in. &#x60;DNM&#x60; is *Doubutsu no Mori* for the Nintendo 64 (Japan-exclusive); &#x60;AC&#x60; is *Animal Crossing* for GameCube; &#x60;E_PLUS&#x60; is *Doubutsu no Mori e+* for GameCube (expanded port of AC, Japan-exclusive); &#x60;WW&#x60; is *Wild World* for the DS; &#x60;CF&#x60; is *City Folk* for Wii; &#x60;NL&#x60; is *New Leaf* for 3DS; &#x60;WA&#x60; is *Welcome amiibo*, the *New Leaf* expansion; &#x60;NH&#x60; is *New Horizons* for Switch; &#x60;FILM&#x60; is the *Doubutsu no Mori* Japan-exclusive film; &#x60;HHD&#x60; is *Happy Home Designer* for the Wii; and &#x60;PC&#x60; is *Pocket Camp* for mobile. | [optional] 
**gender** | **String** | Gender of the villager. In *Animal Crossing*, only male and female are used. | [optional] 
**id** | **String** | The game&#39;s internal identifier for the villager. Not all villagers have IDs; villagers who appeared in any game including or after *Wild World* have a consistent ID between games. | [optional] 
**imageUrl** | **String** | Image of the villager from the latest game the villager appeared in. | [optional] 
**islander** | **Boolean** | Whether the villager was an island in *Animal Crossing* for GameCube. Only a small number of villagers (36) were islanders. | [optional] 
**name** | **String** | Name of the villager. | [optional] 
**nhDetails** | [**VillagerNhDetails**](VillagerNhDetails.md) |  | [optional] 
**personality** | **String** | The villager&#39;s personality. Note that there are no official in-game personality names; these are names that are commonly used by the community. In the case of &#39;sisterly&#39;, other common names include &#39;big sis&#39; and &#39;uchi&#39;. | [optional] 
**phrase** | **String** | The villager&#39;s default phrase they use throughout conversation. This will be the phrase from the latest game (i.e. if the villager had varying phrases between *Wild World* and *New Horizons*, this will be the *New Horizons* quote). | [optional] 
**prevPhrases** | **[String]** | Any phrases used in previous *Animal Crossing* installations. May be empty. | [optional] 
**quote** | **String** | The villager&#39;s quote as it appears on the back of their in-game portrait item. This will be the quote from the latest game (i.e. if the villager had varying quotes between *Wild World* and *New Horizons*, this will be the *New Horizons* quote). For villagers from older games that do not have a quote, this field will be an empty string. | [optional] 
**sign** | **String** | The villager&#39;s astrological star sign. | [optional] 
**species** | **String** | The villager&#39;s species. | [optional] 
**textColor** | **String** | The HTML color code of the text of the villager&#39;s name badge that appears above their dialogue box when spoken to in-game. Note that to date, only *New Horizons* villagers have this field populated. | [optional] 
**titleColor** | **String** | The HTML color code of the background of the villager&#39;s name badge that appears above their dialogue box when spoken to in-game. Note that to date, only *New Horizons* villagers have this field populated. This field may be useful for styling, such as the accent color for a Discord embed. | [optional] 
**url** | **String** | Link to the respective Nookipedia article. | [optional] 



## Enum: [AppearancesEnum]


* `DNM` (value: `"DNM"`)

* `AC` (value: `"AC"`)

* `E_PLUS` (value: `"E_PLUS"`)

* `WW` (value: `"WW"`)

* `CF` (value: `"CF"`)

* `NL` (value: `"NL"`)

* `WA` (value: `"WA"`)

* `NH` (value: `"NH"`)

* `FILM` (value: `"FILM"`)

* `HHD` (value: `"HHD"`)

* `PC` (value: `"PC"`)





## Enum: DebutEnum


* `DNM` (value: `"DNM"`)

* `AC` (value: `"AC"`)

* `E_PLUS` (value: `"E_PLUS"`)

* `WW` (value: `"WW"`)

* `CF` (value: `"CF"`)

* `NL` (value: `"NL"`)

* `WA` (value: `"WA"`)

* `NH` (value: `"NH"`)

* `FILM` (value: `"FILM"`)

* `HHD` (value: `"HHD"`)

* `PC` (value: `"PC"`)





## Enum: GenderEnum


* `Male` (value: `"Male"`)

* `Female` (value: `"Female"`)





## Enum: PersonalityEnum


* `Big sister` (value: `"Big sister"`)

* `Cranky` (value: `"Cranky"`)

* `Jock` (value: `"Jock"`)

* `Lazy` (value: `"Lazy"`)

* `Normal` (value: `"Normal"`)

* `Peppy` (value: `"Peppy"`)

* `Smug` (value: `"Smug"`)

* `Snooty` (value: `"Snooty"`)





## Enum: SignEnum


* `Aries` (value: `"Aries"`)

* `Taurus` (value: `"Taurus"`)

* `Gemini` (value: `"Gemini"`)

* `Cancer` (value: `"Cancer"`)

* `Leo` (value: `"Leo"`)

* `Virgo` (value: `"Virgo"`)

* `Libra` (value: `"Libra"`)

* `Scorpio` (value: `"Scorpio"`)

* `Sagittarius` (value: `"Sagittarius"`)

* `Capricorn` (value: `"Capricorn"`)

* `Aquarius` (value: `"Aquarius"`)

* `Pisces` (value: `"Pisces"`)





## Enum: SpeciesEnum


* `Alligator` (value: `"Alligator"`)

* `Anteater` (value: `"Anteater"`)

* `Bear` (value: `"Bear"`)

* `Bear cub` (value: `"Bear cub"`)

* `Bird` (value: `"Bird"`)

* `Bull` (value: `"Bull"`)

* `Cat` (value: `"Cat"`)

* `Chicken` (value: `"Chicken"`)

* `Cow` (value: `"Cow"`)

* `Deer` (value: `"Deer"`)

* `Dog` (value: `"Dog"`)

* `Duck` (value: `"Duck"`)

* `Eagle` (value: `"Eagle"`)

* `Elephant` (value: `"Elephant"`)

* `Frog` (value: `"Frog"`)

* `Goat` (value: `"Goat"`)

* `Gorilla` (value: `"Gorilla"`)

* `Hamster` (value: `"Hamster"`)

* `Hippo` (value: `"Hippo"`)

* `Horse` (value: `"Horse"`)

* `Koala` (value: `"Koala"`)

* `Kangaroo` (value: `"Kangaroo"`)

* `Lion` (value: `"Lion"`)

* `Monkey` (value: `"Monkey"`)

* `Mouse` (value: `"Mouse"`)

* `Octopus` (value: `"Octopus"`)

* `Ostrich` (value: `"Ostrich"`)

* `Penguin` (value: `"Penguin"`)

* `Pig` (value: `"Pig"`)

* `Rabbit` (value: `"Rabbit"`)

* `Rhinoceros` (value: `"Rhinoceros"`)

* `Sheep` (value: `"Sheep"`)

* `Squirrel` (value: `"Squirrel"`)

* `Tiger` (value: `"Tiger"`)

* `Wolf` (value: `"Wolf"`)




