

# DestinyHistoricalStatsDefinitionsDestinyHistoricalStatsDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **Integer** | Category for the stat. |  [optional] |
|**group** | **Integer** | Statistic group |  [optional] |
|**iconImage** | **String** | Optional URI to an icon for the statistic |  [optional] |
|**medalTierHash** | **Integer** | The tier associated with this medal - be it implicitly or explicitly. |  [optional] |
|**mergeMethod** | [**MergeMethodEnum**](#MergeMethodEnum) | Optional icon for the statistic |  [optional] |
|**modes** | **List&lt;Integer&gt;** | Game modes where this statistic can be reported. |  [optional] |
|**periodTypes** | **List&lt;Integer&gt;** | Time periods the statistic covers |  [optional] |
|**statDescription** | **String** | Description of a stat if applicable. |  [optional] |
|**statId** | **String** | Unique programmer friendly ID for this stat |  [optional] |
|**statName** | **String** | Display name |  [optional] |
|**statNameAbbr** | **String** | Display name abbreviated |  [optional] |
|**unitLabel** | **String** | Localized Unit Name for the stat. |  [optional] |
|**unitType** | **Integer** | Unit, if any, for the statistic |  [optional] |
|**weight** | **Integer** | Weight assigned to this stat indicating its relative impressiveness. |  [optional] |



## Enum: MergeMethodEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



