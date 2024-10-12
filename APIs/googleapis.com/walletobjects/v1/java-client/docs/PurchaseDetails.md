

# PurchaseDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ID of the account used to purchase the ticket. |  [optional] |
|**confirmationCode** | **String** | The confirmation code for the purchase. This may be the same for multiple different tickets and is used to group tickets together. |  [optional] |
|**purchaseDateTime** | **String** | The purchase date/time of the ticket. This is an ISO 8601 extended format date/time, with or without an offset. Time may be specified up to nanosecond precision. Offsets may be specified with seconds precision (even though offset seconds is not part of ISO 8601). For example: &#x60;1985-04-12T23:20:50.52Z&#x60; would be 20 minutes and 50.52 seconds after the 23rd hour of April 12th, 1985 in UTC. &#x60;1985-04-12T19:20:50.52-04:00&#x60; would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985, 4 hours before UTC (same instant in time as the above example). If the event were in New York, this would be the equivalent of Eastern Daylight Time (EDT). Remember that offset varies in regions that observe Daylight Saving Time (or Summer Time), depending on the time of the year. &#x60;1985-04-12T19:20:50.52&#x60; would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985 with no offset information. Without offset information, some rich features may not be available. |  [optional] |
|**purchaseReceiptNumber** | **String** | Receipt number/identifier for tracking the ticket purchase via the body that sold the ticket. |  [optional] |
|**ticketCost** | [**TicketCost**](TicketCost.md) |  |  [optional] |



