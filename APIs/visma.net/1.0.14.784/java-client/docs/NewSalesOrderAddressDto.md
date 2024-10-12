

# NewSalesOrderAddressDto

Defines a new address when creating a sales order.  When the address information is provided, it is expected to provide all needed fields for the address(line1, line2, countryId etc).  No default values from the customer will be set for the non defined address fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**city** | **String** | The city |  [optional] |
|**countryId** | **String** | The country. Required when setting the address. |  [optional] |
|**line1** | **String** | Address line 1 |  [optional] |
|**line2** | **String** | Address line 2 |  [optional] |
|**line3** | **String** | Address line 3 |  [optional] |
|**postalCode** | **String** | The postal code |  [optional] |
|**stateId** | **String** | The state |  [optional] |



