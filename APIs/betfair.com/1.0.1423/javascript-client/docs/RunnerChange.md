# BetfairExchangeStreamingApi.RunnerChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atb** | **[[Number]]** | Available To Back - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**atl** | **[[Number]]** | Available To Lay - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**batb** | **[[Number]]** | Best Available To Back - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 
**batl** | **[[Number]]** | Best Available To Lay - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 
**bdatb** | **[[Number]]** | Best Display Available To Back (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 
**bdatl** | **[[Number]]** | Best Display Available To Lay (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) | [optional] 
**hc** | **Number** | Handicap - the handicap of the runner (selection) (null if not applicable) | [optional] 
**id** | **Number** | Selection Id - the id of the runner (selection) | [optional] 
**ltp** | **Number** | Last Traded Price - The last traded price (or null if un-changed) | [optional] 
**spb** | **[[Number]]** | Starting Price Back - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**spf** | **Number** | Starting Price Far - The far starting price (or null if un-changed) | [optional] 
**spl** | **[[Number]]** | Starting Price Lay - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**spn** | **Number** | Starting Price Near - The far starting price (or null if un-changed) | [optional] 
**trd** | **[[Number]]** | Traded - PriceVol tuple delta of price changes (0 vol is remove) | [optional] 
**tv** | **Number** | The total amount matched. This value is truncated at 2dp. | [optional] 


