

# ListLegs200Response

List Legs Response Payload Object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embedded** | [**ListLegs200ResponseEmbedded**](ListLegs200ResponseEmbedded.md) |  |  |
|**links** | [**ListLegs200ResponseLinks**](ListLegs200ResponseLinks.md) |  |  |
|**count** | **BigDecimal** | The total number of records returned by your request. |  |
|**pageSize** | **BigDecimal** | The amount of records returned in this response |  |
|**recordIndex** | **BigDecimal** | Return &#x60;page_size&#x60; amount of conversations from this index in the response. That is, if your request returns 300 conversations, set &#x60;record_index&#x60; to 5 in order to return conversations 50 to 59. The default value is 0. That is, the first &#x60;page_size&#x60; calls. |  |



