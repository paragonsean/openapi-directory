

# MarketDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**betDelay** | **Integer** |  |  [optional] |
|**bettingType** | [**BettingTypeEnum**](#BettingTypeEnum) |  |  [optional] |
|**bspMarket** | **Boolean** |  |  [optional] |
|**bspReconciled** | **Boolean** |  |  [optional] |
|**complete** | **Boolean** |  |  [optional] |
|**countryCode** | **String** |  |  [optional] |
|**crossMatching** | **Boolean** |  |  [optional] |
|**discountAllowed** | **Boolean** |  |  [optional] |
|**eachWayDivisor** | **Double** |  |  [optional] |
|**eventId** | **String** |  |  [optional] |
|**eventTypeId** | **String** | The Event Type the market is contained within. |  [optional] |
|**inPlay** | **Boolean** |  |  [optional] |
|**keyLineDefinition** | [**KeyLineDefinition**](KeyLineDefinition.md) |  |  [optional] |
|**lineInterval** | **Double** | For Handicap and Line markets, the lines available on this market will be between the range of lineMinUnit and lineMaxUnit, in increments of the lineInterval value. e.g. If unit is runs, lineMinUnit&#x3D;10, lineMaxUnit&#x3D;20 and lineInterval&#x3D;0.5, then valid lines include 10, 10.5, 11, 11.5 up to 20 runs. |  [optional] |
|**lineMaxUnit** | **Double** | For Handicap and Line markets, the maximum value for the outcome, in market units for this market (eg 100 runs). |  [optional] |
|**lineMinUnit** | **Double** | For Handicap and Line markets, the minimum value for the outcome, in market units for this market (eg 0 runs). |  [optional] |
|**marketBaseRate** | **Double** |  |  [optional] |
|**marketTime** | **OffsetDateTime** |  |  [optional] |
|**marketType** | **String** |  |  [optional] |
|**numberOfActiveRunners** | **Integer** |  |  [optional] |
|**numberOfWinners** | **Integer** |  |  [optional] |
|**openDate** | **OffsetDateTime** |  |  [optional] |
|**persistenceEnabled** | **Boolean** |  |  [optional] |
|**priceLadderDefinition** | [**PriceLadderDefinition**](PriceLadderDefinition.md) |  |  [optional] |
|**raceType** | **String** |  |  [optional] |
|**regulators** | **List&lt;String&gt;** | The market regulators. |  [optional] |
|**runners** | [**List&lt;RunnerDefinition&gt;**](RunnerDefinition.md) |  |  [optional] |
|**runnersVoidable** | **Boolean** |  |  [optional] |
|**settledTime** | **OffsetDateTime** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**suspendTime** | **OffsetDateTime** |  |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**turnInPlayEnabled** | **Boolean** |  |  [optional] |
|**venue** | **String** |  |  [optional] |
|**version** | **Long** |  |  [optional] |



## Enum: BettingTypeEnum

| Name | Value |
|---- | -----|
| ODDS | &quot;ODDS&quot; |
| LINE | &quot;LINE&quot; |
| RANGE | &quot;RANGE&quot; |
| ASIAN_HANDICAP_DOUBLE_LINE | &quot;ASIAN_HANDICAP_DOUBLE_LINE&quot; |
| ASIAN_HANDICAP_SINGLE_LINE | &quot;ASIAN_HANDICAP_SINGLE_LINE&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INACTIVE | &quot;INACTIVE&quot; |
| OPEN | &quot;OPEN&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| CLOSED | &quot;CLOSED&quot; |



