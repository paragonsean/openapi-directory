

# SalesOrderShippingDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**AddressDto**](AddressDto.md) |  |  [optional] |
|**contact** | [**ContactDto**](ContactDto.md) |  |  [optional] |
|**fobPoint** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |
|**insurance** | **Boolean** | Whether insurance applies to this shipping |  [optional] |
|**intrastatTransactionType** | [**IdDescriptionPairDto**](IdDescriptionPairDto.md) |  |  [optional] |
|**preferredWarehouse** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |
|**priority** | **Integer** | Priority of the order |  [optional] |
|**residentialDelivery** | **Boolean** | Whether this is residential delivery |  [optional] |
|**rule** | **String** | The shipping rule |  [optional] |
|**saturdayDelivery** | **Boolean** | Whether this is a saturday delivery |  [optional] |
|**scheduledDate** | **OffsetDateTime** | The shipping scheduled date  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**shipSeparately** | **Boolean** | Whether this order can/is shipped separately |  [optional] |
|**shipVia** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |
|**terms** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |
|**zone** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |



