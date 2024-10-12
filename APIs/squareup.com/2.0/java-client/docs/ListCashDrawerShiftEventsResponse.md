

# ListCashDrawerShiftEventsResponse



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | Opaque cursor for fetching the next page. Cursor is not present in the last page of results. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**events** | [**List&lt;CashDrawerShiftEvent&gt;**](CashDrawerShiftEvent.md) | All of the events (payments, refunds, etc.) for a cash drawer during the shift. |  [optional] |



