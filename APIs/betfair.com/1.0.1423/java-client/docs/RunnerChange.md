

# RunnerChange


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atb** | **List&lt;List&lt;Double&gt;&gt;** | Available To Back - PriceVol tuple delta of price changes (0 vol is remove) |  [optional] |
|**atl** | **List&lt;List&lt;Double&gt;&gt;** | Available To Lay - PriceVol tuple delta of price changes (0 vol is remove) |  [optional] |
|**batb** | **List&lt;List&lt;Double&gt;&gt;** | Best Available To Back - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) |  [optional] |
|**batl** | **List&lt;List&lt;Double&gt;&gt;** | Best Available To Lay - LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) |  [optional] |
|**bdatb** | **List&lt;List&lt;Double&gt;&gt;** | Best Display Available To Back (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) |  [optional] |
|**bdatl** | **List&lt;List&lt;Double&gt;&gt;** | Best Display Available To Lay (includes virtual prices)- LevelPriceVol triple delta of price changes, keyed by level (0 vol is remove) |  [optional] |
|**hc** | **Double** | Handicap - the handicap of the runner (selection) (null if not applicable) |  [optional] |
|**id** | **Long** | Selection Id - the id of the runner (selection) |  [optional] |
|**ltp** | **Double** | Last Traded Price - The last traded price (or null if un-changed) |  [optional] |
|**spb** | **List&lt;List&lt;Double&gt;&gt;** | Starting Price Back - PriceVol tuple delta of price changes (0 vol is remove) |  [optional] |
|**spf** | **Double** | Starting Price Far - The far starting price (or null if un-changed) |  [optional] |
|**spl** | **List&lt;List&lt;Double&gt;&gt;** | Starting Price Lay - PriceVol tuple delta of price changes (0 vol is remove) |  [optional] |
|**spn** | **Double** | Starting Price Near - The far starting price (or null if un-changed) |  [optional] |
|**trd** | **List&lt;List&lt;Double&gt;&gt;** | Traded - PriceVol tuple delta of price changes (0 vol is remove) |  [optional] |
|**tv** | **Double** | The total amount matched. This value is truncated at 2dp. |  [optional] |



