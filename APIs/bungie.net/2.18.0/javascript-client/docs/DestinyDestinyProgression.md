# BungieNetApi.DestinyDestinyProgression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentProgress** | **Number** | This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned) | [optional] 
**currentResetCount** | **Number** | The number of resets of this progression you&#39;ve executed this season, if applicable to this progression. | [optional] 
**dailyLimit** | **Number** | If this progression has a daily limit, this is that limit. | [optional] 
**dailyProgress** | **Number** | The amount of progress earned today for this progression. | [optional] 
**level** | **Number** | This is the level of the progression (for instance, the Character Level). | [optional] 
**levelCap** | **Number** | This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable) | [optional] 
**nextLevelAt** | **Number** | The total amount of progression (i.e. \&quot;Experience\&quot;) needed in order to reach the next level. | [optional] 
**progressToNextLevel** | **Number** | The amount of progression (i.e. \&quot;Experience\&quot;) needed to reach the next level of this Progression. Jeez, progression is such an overloaded word. | [optional] 
**progressionHash** | **Number** | The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data. | [optional] 
**rewardItemStates** | **[Number]** | Information about historical rewards for this progression, if there is any data for it. | [optional] 
**seasonResets** | [**[DestinyDestinyProgressionResetEntry]**](DestinyDestinyProgressionResetEntry.md) | Information about historical resets of this progression, if there is any data for it. | [optional] 
**stepIndex** | **Number** | Progressions define their levels in \&quot;steps\&quot;. Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the \&quot;steps\&quot; property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.) | [optional] 
**weeklyLimit** | **Number** | If this progression has a weekly limit, this is that limit. | [optional] 
**weeklyProgress** | **Number** | The amount of progress earned toward this progression in the current week. | [optional] 


