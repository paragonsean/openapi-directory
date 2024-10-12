

# RatesBatchUpdateRequestItem

A rateplan update entry, for a given range and a given price.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basePrice** | **Double** | The price of the rateplan for the default room type and single occupancy. |  |
|**from** | **OffsetDateTime** | Defines the first business day you would like to update rates. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. |  |
|**rateplan** | **String** | The rateplan code to be updated. NOTE: this must be a base rateplan and not a derived one. |  |
|**to** | **OffsetDateTime** | Defines the last business day you would like to update rates. This can be same as {Hetras.PublicApi.Models.Hotels.Rateplans.Rates.RatesBatchUpdateRequestItem.To} if the update is for a single date. |  |



