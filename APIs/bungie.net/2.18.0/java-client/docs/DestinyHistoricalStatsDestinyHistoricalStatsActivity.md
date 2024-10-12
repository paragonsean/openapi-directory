

# DestinyHistoricalStatsDestinyHistoricalStatsActivity

Summary information about the activity that was played.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**directorActivityHash** | **Integer** | The unique hash identifier of the DestinyActivityDefinition that was played. |  [optional] |
|**instanceId** | **Long** | The unique identifier for this *specific* match that was played.  This value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint. |  [optional] |
|**isPrivate** | **Boolean** | Whether or not the match was a private match. |  [optional] |
|**membershipType** | **Integer** | The Membership Type indicating the platform on which this match was played. |  [optional] |
|**mode** | **Integer** | Indicates the most specific game mode of the activity that we could find. |  [optional] |
|**modes** | **List&lt;Integer&gt;** | The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event. |  [optional] |
|**referenceId** | **Integer** | The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it&#39;d be named activityHash. Too late now. |  [optional] |



