

# Ticket


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closedAt** | **OffsetDateTime** | Date-time when ticket was closed |  [optional] |
|**createdAt** | **OffsetDateTime** | Date time that ticket was created |  [optional] |
|**customer** | [**CustomerReference**](CustomerReference.md) |  |  [optional] |
|**description** | **String** | Trouble ticked brief description |  [optional] |
|**metadata** | [**List&lt;Metadata&gt;**](Metadata.md) |  |  [optional] |
|**priority** | **String** | Trouble ticket priority |  [optional] |
|**sla** | **OffsetDateTime** | Date-time with a promisse for the customer when this ticket will be resolved |  [optional] |
|**status** | **String** | Trouble Ticket status. &#39;OPEN&#39;,&#39;CLOSED&#39;,&#39;REOPENED&#39; |  [optional] |
|**subject** | **String** | Short one line title describing ticket. |  [optional] |
|**ticketId** | **String** | Trouble Ticket unique identification Id |  [optional] |
|**type** | **String** | Trouble ticket type. |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date-time with last update of this ticket |  [optional] |



