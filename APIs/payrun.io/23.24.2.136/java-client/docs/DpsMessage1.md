

# DpsMessage1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formType** | **String** | The dps messages&#39; form type |  [optional] |
|**issueDate** | **LocalDate** | The dps messages&#39; issue date |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The dps messages&#39; last updated |  [optional] |
|**message** | **String** | The dps messages&#39; message |  [optional] |
|**messageStatus** | [**MessageStatusEnum**](#MessageStatusEnum) | The dps messages&#39; message status |  [optional] |
|**messageType** | **String** | The dps messages&#39; message type |  [optional] |
|**processingResult** | **String** | The dps messages&#39; processing result |  [optional] |
|**retrieveDate** | **OffsetDateTime** | The dps messages&#39; retrieve date |  [optional] |
|**sequenceNumber** | **Integer** | The dps messages&#39; sequence number |  [optional] |



## Enum: MessageStatusEnum

| Name | Value |
|---- | -----|
| RETRIEVED | &quot;Retrieved&quot; |
| APPLIED | &quot;Applied&quot; |
| UNRESOLVED | &quot;Unresolved&quot; |
| IGNORED | &quot;Ignored&quot; |
| INFORMATION | &quot;Information&quot; |



