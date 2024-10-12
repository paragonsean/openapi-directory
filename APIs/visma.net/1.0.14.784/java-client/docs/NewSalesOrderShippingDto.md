

# NewSalesOrderShippingDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**NewSalesOrderAddressDto**](NewSalesOrderAddressDto.md) |  |  [optional] |
|**contact** | [**NewSalesOrderContactDto**](NewSalesOrderContactDto.md) |  |  [optional] |
|**fobPointId** | **String** | The identifier of the point (such as a city or town) where the title of goods passes from the company to the customer. |  [optional] |
|**insurance** | **Boolean** | Sets whether insurance applies to this shipping |  [optional] |
|**intrastatTransactionTypeId** | **Integer** | Sets the intrastat transaction type id for the sales order, if not supplied the default value from the ordertype will be used. Must be a valid intrastat transaction type id. |  [optional] |
|**preferredWarehouseId** | **String** | Sets the default site for the customer supplied to use on the order. Must be a valid site id |  [optional] |
|**priority** | **Integer** | Sets priority of the order |  [optional] |
|**residentialDelivery** | **Boolean** | Sets whether this is residential delivery |  [optional] |
|**rule** | **String** | Sets the shipping rule for the order |  [optional] |
|**saturdayDelivery** | **Boolean** | Sets whether this is a saturday delivery |  [optional] |
|**scheduledDate** | **OffsetDateTime** | Sets the date the shipment is scheduled for  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**shipSeparately** | **Boolean** | Sets whether the order should be shipped separately or included in a batch segment |  [optional] |
|**shipViaId** | **String** | Sets the unique id that represents the carrier and its service to be used for shipping the ordered goods. |  [optional] |
|**termsId** | **String** | The identifier of the shipping terms used for the order. |  [optional] |
|**zoneId** | **String** | Sets the shipping zone of the order freight |  [optional] |



