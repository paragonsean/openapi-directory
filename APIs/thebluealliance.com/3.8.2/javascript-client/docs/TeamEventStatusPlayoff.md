# TheBlueAllianceApiV3.TeamEventStatusPlayoff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentLevelRecord** | [**WLTRecord**](WLTRecord.md) |  | [optional] 
**level** | **String** | The highest playoff level the team reached. | [optional] 
**playoffAverage** | **Number** | The average match score during playoffs. Year specific. May be null if not relevant for a given year. | [optional] 
**record** | [**WLTRecord**](WLTRecord.md) |  | [optional] 
**status** | **String** | Current competition status for the playoffs. | [optional] 



## Enum: LevelEnum


* `qm` (value: `"qm"`)

* `ef` (value: `"ef"`)

* `qf` (value: `"qf"`)

* `sf` (value: `"sf"`)

* `f` (value: `"f"`)





## Enum: StatusEnum


* `won` (value: `"won"`)

* `eliminated` (value: `"eliminated"`)

* `playing` (value: `"playing"`)




