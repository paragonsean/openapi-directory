

# Villager


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**altName** | **String** | A previous name for the villager. A very small number of villagers changed names between earlier games, such as Sally being known as Hazel in the original game. |  [optional] |
|**appearances** | [**List&lt;AppearancesEnum&gt;**](#List&lt;AppearancesEnum&gt;) | List of official media the villager appeared in. &#x60;DNM&#x60; is *Doubutsu no Mori* for the Nintendo 64 (Japan-exclusive); &#x60;AC&#x60; is *Animal Crossing* for GameCube; &#x60;E_PLUS&#x60; is *Doubutsu no Mori e+* for GameCube (expanded port of AC, Japan-exclusive); &#x60;WW&#x60; is *Wild World* for the DS; &#x60;CF&#x60; is *City Folk* for Wii; &#x60;NL&#x60; is *New Leaf* for 3DS; &#x60;WA&#x60; is *Welcome amiibo*, the *New Leaf* expansion; &#x60;NH&#x60; is *New Horizons* for Switch; &#x60;FILM&#x60; is the *Doubutsu no Mori* Japan-exclusive film; &#x60;HHD&#x60; is *Happy Home Designer* for the Wii; and &#x60;PC&#x60; is *Pocket Camp* for mobile. |  [optional] |
|**birthdayDay** | **String** | Birthday day of the villager. Note that villager birthdays were not introduced until *Wild World*. For villagers who didn&#39;t appear in *Wild World* or any later games, this field will be an empty string. |  [optional] |
|**birthdayMonth** | **String** | Birthday month of the villager. Note that villager birthdays were not introduced until *Wild World*. For villagers who didn&#39;t appear in *Wild World* or any later games, this field will be an empty string. |  [optional] |
|**clothing** | **String** | The villager&#39;s default clothing. This will be the clothing from the latest game (i.e. if the villager had varying phrases between *Wild World* and *New Horizons*, this will be the *New Horizons* clothing). |  [optional] |
|**debut** | [**DebutEnum**](#DebutEnum) | The first *Animal Crossing* game the villager appeared in. &#x60;DNM&#x60; is *Doubutsu no Mori* for the Nintendo 64 (Japan-exclusive); &#x60;AC&#x60; is *Animal Crossing* for GameCube; &#x60;E_PLUS&#x60; is *Doubutsu no Mori e+* for GameCube (expanded port of AC, Japan-exclusive); &#x60;WW&#x60; is *Wild World* for the DS; &#x60;CF&#x60; is *City Folk* for Wii; &#x60;NL&#x60; is *New Leaf* for 3DS; &#x60;WA&#x60; is *Welcome amiibo*, the *New Leaf* expansion; &#x60;NH&#x60; is *New Horizons* for Switch; &#x60;FILM&#x60; is the *Doubutsu no Mori* Japan-exclusive film; &#x60;HHD&#x60; is *Happy Home Designer* for the Wii; and &#x60;PC&#x60; is *Pocket Camp* for mobile. |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | Gender of the villager. In *Animal Crossing*, only male and female are used. |  [optional] |
|**id** | **String** | The game&#39;s internal identifier for the villager. Not all villagers have IDs; villagers who appeared in any game including or after *Wild World* have a consistent ID between games. |  [optional] |
|**imageUrl** | **String** | Image of the villager from the latest game the villager appeared in. |  [optional] |
|**islander** | **Boolean** | Whether the villager was an island in *Animal Crossing* for GameCube. Only a small number of villagers (36) were islanders. |  [optional] |
|**name** | **String** | Name of the villager. |  [optional] |
|**nhDetails** | [**VillagerNhDetails**](VillagerNhDetails.md) |  |  [optional] |
|**personality** | [**PersonalityEnum**](#PersonalityEnum) | The villager&#39;s personality. Note that there are no official in-game personality names; these are names that are commonly used by the community. In the case of &#39;sisterly&#39;, other common names include &#39;big sis&#39; and &#39;uchi&#39;. |  [optional] |
|**phrase** | **String** | The villager&#39;s default phrase they use throughout conversation. This will be the phrase from the latest game (i.e. if the villager had varying phrases between *Wild World* and *New Horizons*, this will be the *New Horizons* quote). |  [optional] |
|**prevPhrases** | **List&lt;String&gt;** | Any phrases used in previous *Animal Crossing* installations. May be empty. |  [optional] |
|**quote** | **String** | The villager&#39;s quote as it appears on the back of their in-game portrait item. This will be the quote from the latest game (i.e. if the villager had varying quotes between *Wild World* and *New Horizons*, this will be the *New Horizons* quote). For villagers from older games that do not have a quote, this field will be an empty string. |  [optional] |
|**sign** | [**SignEnum**](#SignEnum) | The villager&#39;s astrological star sign. |  [optional] |
|**species** | [**SpeciesEnum**](#SpeciesEnum) | The villager&#39;s species. |  [optional] |
|**textColor** | **String** | The HTML color code of the text of the villager&#39;s name badge that appears above their dialogue box when spoken to in-game. Note that to date, only *New Horizons* villagers have this field populated. |  [optional] |
|**titleColor** | **String** | The HTML color code of the background of the villager&#39;s name badge that appears above their dialogue box when spoken to in-game. Note that to date, only *New Horizons* villagers have this field populated. This field may be useful for styling, such as the accent color for a Discord embed. |  [optional] |
|**url** | **String** | Link to the respective Nookipedia article. |  [optional] |



## Enum: List&lt;AppearancesEnum&gt;

| Name | Value |
|---- | -----|
| DNM | &quot;DNM&quot; |
| AC | &quot;AC&quot; |
| E_PLUS | &quot;E_PLUS&quot; |
| WW | &quot;WW&quot; |
| CF | &quot;CF&quot; |
| NL | &quot;NL&quot; |
| WA | &quot;WA&quot; |
| NH | &quot;NH&quot; |
| FILM | &quot;FILM&quot; |
| HHD | &quot;HHD&quot; |
| PC | &quot;PC&quot; |



## Enum: DebutEnum

| Name | Value |
|---- | -----|
| DNM | &quot;DNM&quot; |
| AC | &quot;AC&quot; |
| E_PLUS | &quot;E_PLUS&quot; |
| WW | &quot;WW&quot; |
| CF | &quot;CF&quot; |
| NL | &quot;NL&quot; |
| WA | &quot;WA&quot; |
| NH | &quot;NH&quot; |
| FILM | &quot;FILM&quot; |
| HHD | &quot;HHD&quot; |
| PC | &quot;PC&quot; |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;Male&quot; |
| FEMALE | &quot;Female&quot; |



## Enum: PersonalityEnum

| Name | Value |
|---- | -----|
| BIG_SISTER | &quot;Big sister&quot; |
| CRANKY | &quot;Cranky&quot; |
| JOCK | &quot;Jock&quot; |
| LAZY | &quot;Lazy&quot; |
| NORMAL | &quot;Normal&quot; |
| PEPPY | &quot;Peppy&quot; |
| SMUG | &quot;Smug&quot; |
| SNOOTY | &quot;Snooty&quot; |



## Enum: SignEnum

| Name | Value |
|---- | -----|
| ARIES | &quot;Aries&quot; |
| TAURUS | &quot;Taurus&quot; |
| GEMINI | &quot;Gemini&quot; |
| CANCER | &quot;Cancer&quot; |
| LEO | &quot;Leo&quot; |
| VIRGO | &quot;Virgo&quot; |
| LIBRA | &quot;Libra&quot; |
| SCORPIO | &quot;Scorpio&quot; |
| SAGITTARIUS | &quot;Sagittarius&quot; |
| CAPRICORN | &quot;Capricorn&quot; |
| AQUARIUS | &quot;Aquarius&quot; |
| PISCES | &quot;Pisces&quot; |



## Enum: SpeciesEnum

| Name | Value |
|---- | -----|
| ALLIGATOR | &quot;Alligator&quot; |
| ANTEATER | &quot;Anteater&quot; |
| BEAR | &quot;Bear&quot; |
| BEAR_CUB | &quot;Bear cub&quot; |
| BIRD | &quot;Bird&quot; |
| BULL | &quot;Bull&quot; |
| CAT | &quot;Cat&quot; |
| CHICKEN | &quot;Chicken&quot; |
| COW | &quot;Cow&quot; |
| DEER | &quot;Deer&quot; |
| DOG | &quot;Dog&quot; |
| DUCK | &quot;Duck&quot; |
| EAGLE | &quot;Eagle&quot; |
| ELEPHANT | &quot;Elephant&quot; |
| FROG | &quot;Frog&quot; |
| GOAT | &quot;Goat&quot; |
| GORILLA | &quot;Gorilla&quot; |
| HAMSTER | &quot;Hamster&quot; |
| HIPPO | &quot;Hippo&quot; |
| HORSE | &quot;Horse&quot; |
| KOALA | &quot;Koala&quot; |
| KANGAROO | &quot;Kangaroo&quot; |
| LION | &quot;Lion&quot; |
| MONKEY | &quot;Monkey&quot; |
| MOUSE | &quot;Mouse&quot; |
| OCTOPUS | &quot;Octopus&quot; |
| OSTRICH | &quot;Ostrich&quot; |
| PENGUIN | &quot;Penguin&quot; |
| PIG | &quot;Pig&quot; |
| RABBIT | &quot;Rabbit&quot; |
| RHINOCEROS | &quot;Rhinoceros&quot; |
| SHEEP | &quot;Sheep&quot; |
| SQUIRREL | &quot;Squirrel&quot; |
| TIGER | &quot;Tiger&quot; |
| WOLF | &quot;Wolf&quot; |



