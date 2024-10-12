# BetfairExchangeStreamingApi.MarketDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**betDelay** | **Number** |  | [optional] 
**bettingType** | **String** |  | [optional] 
**bspMarket** | **Boolean** |  | [optional] 
**bspReconciled** | **Boolean** |  | [optional] 
**complete** | **Boolean** |  | [optional] 
**countryCode** | **String** |  | [optional] 
**crossMatching** | **Boolean** |  | [optional] 
**discountAllowed** | **Boolean** |  | [optional] 
**eachWayDivisor** | **Number** |  | [optional] 
**eventId** | **String** |  | [optional] 
**eventTypeId** | **String** | The Event Type the market is contained within. | [optional] 
**inPlay** | **Boolean** |  | [optional] 
**keyLineDefinition** | [**KeyLineDefinition**](KeyLineDefinition.md) |  | [optional] 
**lineInterval** | **Number** | For Handicap and Line markets, the lines available on this market will be between the range of lineMinUnit and lineMaxUnit, in increments of the lineInterval value. e.g. If unit is runs, lineMinUnit&#x3D;10, lineMaxUnit&#x3D;20 and lineInterval&#x3D;0.5, then valid lines include 10, 10.5, 11, 11.5 up to 20 runs. | [optional] 
**lineMaxUnit** | **Number** | For Handicap and Line markets, the maximum value for the outcome, in market units for this market (eg 100 runs). | [optional] 
**lineMinUnit** | **Number** | For Handicap and Line markets, the minimum value for the outcome, in market units for this market (eg 0 runs). | [optional] 
**marketBaseRate** | **Number** |  | [optional] 
**marketTime** | **Date** |  | [optional] 
**marketType** | **String** |  | [optional] 
**numberOfActiveRunners** | **Number** |  | [optional] 
**numberOfWinners** | **Number** |  | [optional] 
**openDate** | **Date** |  | [optional] 
**persistenceEnabled** | **Boolean** |  | [optional] 
**priceLadderDefinition** | [**PriceLadderDefinition**](PriceLadderDefinition.md) |  | [optional] 
**raceType** | **String** |  | [optional] 
**regulators** | **[String]** | The market regulators. | [optional] 
**runners** | [**[RunnerDefinition]**](RunnerDefinition.md) |  | [optional] 
**runnersVoidable** | **Boolean** |  | [optional] 
**settledTime** | **Date** |  | [optional] 
**status** | **String** |  | [optional] 
**suspendTime** | **Date** |  | [optional] 
**timezone** | **String** |  | [optional] 
**turnInPlayEnabled** | **Boolean** |  | [optional] 
**venue** | **String** |  | [optional] 
**version** | **Number** |  | [optional] 



## Enum: BettingTypeEnum


* `ODDS` (value: `"ODDS"`)

* `LINE` (value: `"LINE"`)

* `RANGE` (value: `"RANGE"`)

* `ASIAN_HANDICAP_DOUBLE_LINE` (value: `"ASIAN_HANDICAP_DOUBLE_LINE"`)

* `ASIAN_HANDICAP_SINGLE_LINE` (value: `"ASIAN_HANDICAP_SINGLE_LINE"`)





## Enum: StatusEnum


* `INACTIVE` (value: `"INACTIVE"`)

* `OPEN` (value: `"OPEN"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `CLOSED` (value: `"CLOSED"`)




