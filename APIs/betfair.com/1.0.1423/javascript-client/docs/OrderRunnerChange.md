# BetfairExchangeStreamingApi.OrderRunnerChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullImage** | **Boolean** |  | [optional] 
**hc** | **Number** | Handicap - the handicap of the runner (selection) (null if not applicable) | [optional] 
**id** | **Number** | Selection Id - the id of the runner (selection) | [optional] 
**mb** | **[[Number]]** | Matched Backs - matched amounts by distinct matched price on the Back side for this runner (selection) | [optional] 
**ml** | **[[Number]]** | Matched Lays - matched amounts by distinct matched price on the Lay side for this runner (selection) | [optional] 
**smc** | [**{String: StrategyMatchChange}**](StrategyMatchChange.md) | Strategy Matches - Matched Backs and Matched Lays grouped by strategy reference | [optional] 
**uo** | [**[Order]**](Order.md) | Unmatched Orders - orders on this runner (selection) that are not fully matched | [optional] 


