

# NextPlaybackItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstWatchedDate** | **OffsetDateTime** | Time when the item corresponding to the itemId passed in by the client was first watched by the user. Will be &#x60;undefined&#x60; if the user has never watched the item.  It can be used to identify the scenario where the user has never watched a show and we are suggesting they watch the first episode (i.e. it is missing in this scenario)  **This will only be populated when a &#x60;showId&#x60; is passed in**  |  [optional] |
|**lastWatchedDate** | **OffsetDateTime** | Time when the item corresponding to the itemId passed in by the client was last watched by the user. Will be &#x60;undefined&#x60; if the user has never watched the item.  It can be used to identify the scenario where the user has never watched a show and we are suggesting they watch the first episode (i.e. it is missing in this scenario)  **This will only be populated when a &#x60;showId&#x60; is passed in**  |  [optional] |
|**next** | [**ItemDetail**](ItemDetail.md) |  |  [optional] |
|**sourceItemId** | **String** | The id of the item used to determine the next item to play. |  |
|**suggestionType** | [**SuggestionTypeEnum**](#SuggestionTypeEnum) | Field indicating the type or reason behind the suggestion.  Id Type   | Show Watched Status| Value            | Description ----------|--------------------|------------------|--------------------------------- showId    | Unwatched          | StartWatching    | showId    | Completely watched | RestartWatching  | showId    | Partly watched     | ContinueWatching | Suggested episode partly watched showId    | Partly watched     | Sequential       | Suggested episode unwatched episodeId | Any                | Sequential       | Next episode in show  |  [optional] |



## Enum: SuggestionTypeEnum

| Name | Value |
|---- | -----|
| START_WATCHING | &quot;StartWatching&quot; |
| CONTINUE_WATCHING | &quot;ContinueWatching&quot; |
| RESTART_WATCHING | &quot;RestartWatching&quot; |
| SEQUENTIAL | &quot;Sequential&quot; |
| NONE | &quot;None&quot; |



