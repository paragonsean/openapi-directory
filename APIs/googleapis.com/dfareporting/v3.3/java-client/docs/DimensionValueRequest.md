

# DimensionValueRequest

Represents a DimensionValuesRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionName** | **String** | The name of the dimension for which values should be requested. |  [optional] |
|**endDate** | **LocalDate** |  |  [optional] |
|**filters** | [**List&lt;DimensionFilter&gt;**](DimensionFilter.md) | The list of filters by which to filter values. The filters are ANDed. |  [optional] |
|**kind** | **String** | The kind of request this is, in this case dfareporting#dimensionValueRequest . |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |



