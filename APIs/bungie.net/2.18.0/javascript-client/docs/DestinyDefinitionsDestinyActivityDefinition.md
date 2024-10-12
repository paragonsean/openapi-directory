# BungieNetApi.DestinyDefinitionsDestinyActivityDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityGraphList** | [**[DestinyDefinitionsDestinyActivityGraphListEntryDefinition]**](DestinyDefinitionsDestinyActivityGraphListEntryDefinition.md) | Unfortunately, in practice this is almost never populated. In theory, this is supposed to tell which Activity Graph to show if you bring up the director while in this activity. | [optional] 
**activityLightLevel** | **Number** | The recommended light level for this activity. | [optional] 
**activityLocationMappings** | [**[DestinyConstantsDestinyEnvironmentLocationMapping]**](DestinyConstantsDestinyEnvironmentLocationMapping.md) | A list of location mappings that are affected by this activity. Pulled out of DestinyLocationDefinitions for our/your lookup convenience. | [optional] 
**activityModeHashes** | **[Number]** | The hash identifiers for Activity Modes relevant to this activity.  Note that if this is a playlist, the specific playlist entry chosen will determine the actual activity modes that end up being relevant. | [optional] 
**activityModeTypes** | **[Number]** | The activity modes - if any - in enum form. Because we can&#39;t seem to escape the enums. | [optional] 
**activityTypeHash** | **Number** | The hash identifier for the Activity Type of this Activity. You may use it to look up the DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists and many PVP Map Activities will map to generic Activity Types. You&#39;ll have to use your knowledge of the Activity Mode being played to get more specific information about what the user is playing. | [optional] 
**challenges** | [**[DestinyDefinitionsDestinyActivityChallengeDefinition]**](DestinyDefinitionsDestinyActivityChallengeDefinition.md) | An activity can have many Challenges, of which any subset of them may be active for play at any given period of time. This gives the information about the challenges and data that we use to understand when they&#39;re active and what rewards they provide. Sadly, at the moment there&#39;s no central definition for challenges: much like \&quot;Skulls\&quot; were in Destiny 1, these are defined on individual activities and there can be many duplicates/near duplicates across the Destiny 2 ecosystem. I have it in mind to centralize these in a future revision of the API, but we are out of time. | [optional] 
**destinationHash** | **Number** | The hash identifier for the Destination on which this Activity is played. Use it to look up the DestinyDestinationDefinition for human readable info about the destination. A Destination can be thought of as a more specific location than a \&quot;Place\&quot;. For instance, if the \&quot;Place\&quot; is Earth, the \&quot;Destination\&quot; would be a specific city or region on Earth. | [optional] 
**directActivityModeHash** | **Number** | If this activity had an activity mode directly defined on it, this will be the hash of that mode. | [optional] 
**directActivityModeType** | **Number** | If the activity had an activity mode directly defined on it, this will be the enum value of that mode. | [optional] 
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | The title, subtitle, and icon for the activity. We do a little post-processing on this to try and account for Activities where the designers have left this data too minimal to determine what activity is actually being played. | [optional] 
**guidedGame** | [**DestinyDefinitionsDestinyActivityGuidedBlockDefinition**](DestinyDefinitionsDestinyActivityGuidedBlockDefinition.md) | This block of data, if it exists, provides information about the guided game experience and restrictions for this activity. If it doesn&#39;t exist, the game is not able to be played as a guided game. | [optional] 
**hash** | **Number** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **Number** | The index of the entity as it was found in the investment tables. | [optional] 
**insertionPoints** | [**[DestinyDefinitionsDestinyActivityInsertionPointDefinition]**](DestinyDefinitionsDestinyActivityInsertionPointDefinition.md) | The list of phases or points of entry into an activity, along with information we can use to determine their gating and availability. | [optional] 
**isPlaylist** | **Boolean** | If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and Activity Modes. For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes (specific PvP gameplay modes). If this is true, refer to the playlistItems property for the specific entries in the playlist. | [optional] 
**isPvP** | **Boolean** | If true, this activity is a PVP activity or playlist. | [optional] 
**loadouts** | [**[DestinyDefinitionsDestinyActivityLoadoutRequirementSet]**](DestinyDefinitionsDestinyActivityLoadoutRequirementSet.md) | The set of all possible loadout requirements that could be active for this activity. Only one will be active at any given time, and you can discover which one through activity-associated data such as Milestones that have activity info on them. | [optional] 
**matchmaking** | [**DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition**](DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition.md) | This block of data provides information about the Activity&#39;s matchmaking attributes: how many people can join and such. | [optional] 
**modifiers** | [**[DestinyDefinitionsDestinyActivityModifierReferenceDefinition]**](DestinyDefinitionsDestinyActivityModifierReferenceDefinition.md) | Activities can have Modifiers, as defined in DestinyActivityModifierDefinition. These are references to the modifiers that *can* be applied to that activity, along with data that we use to determine if that modifier is actually active at any given point in time. | [optional] 
**optionalUnlockStrings** | [**[DestinyDefinitionsDestinyActivityUnlockStringDefinition]**](DestinyDefinitionsDestinyActivityUnlockStringDefinition.md) | If there are status strings related to the activity and based on internal state of the game, account, or character, then this will be the definition of those strings and the states needed in order for the strings to be shown. | [optional] 
**originalDisplayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | The unadulterated form of the display properties, as they ought to be shown in the Director (if the activity appears in the director). | [optional] 
**pgcrImage** | **String** | When Activities are completed, we generate a \&quot;Post-Game Carnage Report\&quot;, or PGCR, with details about what happened in that activity (how many kills someone got, which team won, etc...) We use this image as the background when displaying PGCR information, and often use it when we refer to the Activity in general. | [optional] 
**placeHash** | **Number** | The hash identifier for the \&quot;Place\&quot; on which this Activity is played. Use it to look up the DestinyPlaceDefinition for human readable info about the Place. A Place is the largest-scoped concept for location information. For instance, if the \&quot;Place\&quot; is Earth, the \&quot;Destination\&quot; would be a specific city or region on Earth. | [optional] 
**playlistItems** | [**[DestinyDefinitionsDestinyActivityPlaylistItemDefinition]**](DestinyDefinitionsDestinyActivityPlaylistItemDefinition.md) | Represents all of the possible activities that could be played in the Playlist, along with information that we can use to determine if they are active at the present time. | [optional] 
**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 
**releaseIcon** | **String** | If the activity has an icon associated with a specific release (such as a DLC), this is the path to that release&#39;s icon. | [optional] 
**releaseTime** | **Number** | If the activity will not be visible until a specific and known time, this will be the seconds since the Epoch when it will become visible. | [optional] 
**rewards** | [**[DestinyDefinitionsDestinyActivityRewardDefinition]**](DestinyDefinitionsDestinyActivityRewardDefinition.md) | The expected possible rewards for the activity. These rewards may or may not be accessible for an individual player based on their character state, the account state, and even the game&#39;s state overall. But it is a useful reference for possible rewards you can earn in the activity. These match up to rewards displayed when you hover over the Activity in the in-game Director, and often refer to Placeholder or \&quot;Dummy\&quot; items: items that tell you what you can earn in vague terms rather than what you&#39;ll specifically be earning (partly because the game doesn&#39;t even know what you&#39;ll earn specifically until you roll for it at the end) | [optional] 
**selectionScreenDisplayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | The title, subtitle, and icon for the activity as determined by Selection Screen data, if there is any for this activity. There won&#39;t be data in this field if the activity is never shown in a selection/options screen. | [optional] 
**tier** | **Number** | The difficulty tier of the activity. | [optional] 



## Enum: DirectActivityModeTypeEnum


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




