

# TicketCountsDetailedEntity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approved** | **Boolean** | Defines whether this ticket count is approved or not. |  |
|**comment** | **String** | Comment for the ticket count. |  |
|**date** | **LocalDate** | Date of the ticket count. |  |
|**eventChannels** | [**List&lt;TicketCountsDetailedEntityEventChannelsInner&gt;**](TicketCountsDetailedEntityEventChannelsInner.md) | Array of event channels where the sales were made. |  [optional] |
|**_final** | **Boolean** | Whether this ticket count is the last and final one of its event or not. If it is, it means that no further ticket counts will be added for the event it belongs to. |  |
|**id** | **Integer** | Unique ID of the ticket count. |  |



