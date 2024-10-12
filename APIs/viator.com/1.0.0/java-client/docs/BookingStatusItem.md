

# BookingStatusItem

**object** containing item booking status information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amended** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking has been amended |  [optional] |
|**cancelled** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking has been cancelled |  [optional] |
|**confirmed** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking is confirmed |  [optional] |
|**failed** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking has failed |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | **level** of *this* item&#39;s booking status |  [optional] |
|**pending** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking is pending |  [optional] |
|**status** | **Integer** | **numeric identifier** of *this* item&#39;s booking status |  [optional] |
|**text** | **String** | **natural-language description** of *this* item&#39;s booking status; e.g., &#39;Waiting to be booked&#39; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **specifier** of *this* item&#39;s booking status * See: [bookingStatus fields and meanings](#section/Appendices/bookingStatus-field-values-and-meanings)  |  [optional] |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| ITEM | &quot;ITEM&quot; |
| ITINERARY | &quot;ITINERARY&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WAITING | &quot;WAITING&quot; |
| CONFIRMED | &quot;CONFIRMED&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |
| PENDING | &quot;PENDING&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| AMENDED | &quot;AMENDED&quot; |
| PENDING_AMEND | &quot;PENDING_AMEND&quot; |
| REJECTED | &quot;REJECTED&quot; |
| ON_HOLD | &quot;ON_HOLD&quot; |



