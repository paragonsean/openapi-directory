# BungieNetApi.DestinyEntitiesCharactersDestinyCharacterActivitiesComponent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableActivities** | [**[DestinyDestinyActivity]**](DestinyDestinyActivity.md) | The list of activities that the user can play. | [optional] 
**currentActivityHash** | **Number** | If the user is in an activity, this will be the hash of the Activity being played. Note that you must combine this info with currentActivityModeHash to get a real picture of what the user is doing right now. For instance, PVP \&quot;Activities\&quot; are just maps: it&#39;s the ActivityMode that determines what type of PVP game they&#39;re playing. | [optional] 
**currentActivityModeHash** | **Number** | If the user is in an activity, this will be the hash of the activity mode being played. Combine with currentActivityHash to give a person a full picture of what they&#39;re doing right now. | [optional] 
**currentActivityModeHashes** | **[Number]** | If the user is in an activity, this will be the hashes of the DestinyActivityModeDefinition being played. Combine with currentActivityHash to give a person a full picture of what they&#39;re doing right now. | [optional] 
**currentActivityModeType** | **Number** | And the current activity&#39;s most specific mode type, if it can be found. | [optional] 
**currentActivityModeTypes** | **[Number]** | All Activity Modes that apply to the current activity being played, in enum form. | [optional] 
**currentPlaylistActivityHash** | **Number** | If the user is in a playlist, this is the hash identifier for the playlist that they chose. | [optional] 
**dateActivityStarted** | **Date** | The last date that the user started playing an activity. | [optional] 
**lastCompletedStoryHash** | **Number** | This will have the activity hash of the last completed story/campaign mission, in case you care about that. | [optional] 



## Enum: CurrentActivityModeTypeEnum


* `0` (value: `0`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)

* `6` (value: `6`)

* `7` (value: `7`)

* `9` (value: `9`)

* `10` (value: `10`)

* `11` (value: `11`)

* `12` (value: `12`)

* `13` (value: `13`)

* `15` (value: `15`)

* `16` (value: `16`)

* `17` (value: `17`)

* `18` (value: `18`)

* `19` (value: `19`)

* `20` (value: `20`)

* `21` (value: `21`)

* `22` (value: `22`)

* `24` (value: `24`)

* `25` (value: `25`)

* `26` (value: `26`)

* `27` (value: `27`)

* `28` (value: `28`)

* `29` (value: `29`)

* `30` (value: `30`)

* `31` (value: `31`)

* `32` (value: `32`)

* `37` (value: `37`)

* `38` (value: `38`)

* `39` (value: `39`)

* `40` (value: `40`)

* `41` (value: `41`)

* `42` (value: `42`)

* `43` (value: `43`)

* `44` (value: `44`)

* `45` (value: `45`)

* `46` (value: `46`)

* `47` (value: `47`)

* `48` (value: `48`)

* `49` (value: `49`)

* `50` (value: `50`)

* `51` (value: `51`)

* `52` (value: `52`)

* `53` (value: `53`)

* `54` (value: `54`)

* `55` (value: `55`)

* `56` (value: `56`)

* `57` (value: `57`)

* `58` (value: `58`)

* `59` (value: `59`)

* `60` (value: `60`)

* `61` (value: `61`)

* `62` (value: `62`)

* `63` (value: `63`)

* `64` (value: `64`)

* `65` (value: `65`)

* `66` (value: `66`)

* `67` (value: `67`)

* `68` (value: `68`)

* `69` (value: `69`)

* `70` (value: `70`)

* `71` (value: `71`)

* `72` (value: `72`)

* `73` (value: `73`)

* `74` (value: `74`)

* `75` (value: `75`)

* `76` (value: `76`)

* `77` (value: `77`)

* `78` (value: `78`)

* `79` (value: `79`)

* `80` (value: `80`)

* `81` (value: `81`)

* `82` (value: `82`)

* `83` (value: `83`)

* `84` (value: `84`)

* `85` (value: `85`)

* `86` (value: `86`)

* `87` (value: `87`)

* `88` (value: `88`)

* `89` (value: `89`)

* `90` (value: `90`)

* `91` (value: `91`)




