

# GetRatesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expand** | [**ExpandEnum**](#ExpandEnum) | You can expand the supplements per room type on demand. By default they are not shown. |  [optional] |
|**from** | **OffsetDateTime** | Defines the last business day you would like to get rates for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days. |  |
|**to** | **OffsetDateTime** | Defines the first business day you would like to get rates for. |  |



## Enum: ExpandEnum

| Name | Value |
|---- | -----|
| ROOM_TYPE_SUPPLEMENTS | &quot;RoomTypeSupplements&quot; |



