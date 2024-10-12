

# ServiceStoreConfigCutoffConfig

Time local delivery ends for the day based on the local timezone of the store. `local_cutoff_time` and `store_close_offset_hours` are mutually exclusive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localCutoffTime** | [**ServiceStoreConfigCutoffConfigLocalCutoffTime**](ServiceStoreConfigCutoffConfigLocalCutoffTime.md) |  |  [optional] |
|**noDeliveryPostCutoff** | **Boolean** | Merchants can opt-out of showing n+1 day local delivery when they have a shipping service configured to n day local delivery. For example, if the shipping service defines same-day delivery, and it&#39;s past the cut-off, setting this field to &#x60;true&#x60; results in the calculated shipping service rate returning &#x60;NO_DELIVERY_POST_CUTOFF&#x60;. In the same example, setting this field to &#x60;false&#x60; results in the calculated shipping time being one day. This is only for local delivery. |  [optional] |
|**storeCloseOffsetHours** | **String** | Represents cutoff time as the number of hours before store closing. Mutually exclusive with other fields (hour and minute). |  [optional] |



