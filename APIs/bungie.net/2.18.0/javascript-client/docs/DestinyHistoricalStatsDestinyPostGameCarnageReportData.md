# BungieNetApi.DestinyHistoricalStatsDestinyPostGameCarnageReportData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityDetails** | [**DestinyHistoricalStatsDestinyHistoricalStatsActivity**](DestinyHistoricalStatsDestinyHistoricalStatsActivity.md) | Details about the activity. | [optional] 
**activityWasStartedFromBeginning** | **Boolean** | True if the activity was started from the beginning, if that information is available and the activity was played post Witch Queen release. | [optional] 
**entries** | [**[DestinyHistoricalStatsDestinyPostGameCarnageReportEntry]**](DestinyHistoricalStatsDestinyPostGameCarnageReportEntry.md) | Collection of players and their data for this activity. | [optional] 
**period** | **Date** | Date and time for the activity. | [optional] 
**startingPhaseIndex** | **Number** | If this activity has \&quot;phases\&quot;, this is the phase at which the activity was started. This value is only valid for activities before the Beyond Light expansion shipped. Subsequent activities will not have a valid value here. | [optional] 
**teams** | [**[DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry]**](DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry.md) | Collection of stats for the player in this activity. | [optional] 


