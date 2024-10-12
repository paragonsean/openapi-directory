

# TeamEventStatusPlayoff

Playoff status for this team, may be null if the team did not make playoffs, or playoffs have not begun.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentLevelRecord** | [**WLTRecord**](WLTRecord.md) |  |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | The highest playoff level the team reached. |  [optional] |
|**playoffAverage** | **Integer** | The average match score during playoffs. Year specific. May be null if not relevant for a given year. |  [optional] |
|**record** | [**WLTRecord**](WLTRecord.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current competition status for the playoffs. |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| QM | &quot;qm&quot; |
| EF | &quot;ef&quot; |
| QF | &quot;qf&quot; |
| SF | &quot;sf&quot; |
| F | &quot;f&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| WON | &quot;won&quot; |
| ELIMINATED | &quot;eliminated&quot; |
| PLAYING | &quot;playing&quot; |



