

# BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel

Container for passing address data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressAddition** | **String** |  |  [optional] |
|**addressType** | [**AddressTypeEnum**](#AddressTypeEnum) | The type of the address |  [optional] |
|**archivedAt** | **OffsetDateTime** | If set, the customeraddress was already archived at the given date. Further modification is disabled. |  [optional] |
|**city** | **String** |  |  [optional] |
|**company** | **String** | The name of the company |  [optional] |
|**countryCode** | **String** | The ISO2 code of the country |  [optional] |
|**customerId** | **Long** | The internal Billbee id of the customer the address belongs to |  [optional] |
|**email** | **String** |  |  [optional] |
|**fax** | **String** |  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**housenumber** | **String** |  |  [optional] |
|**id** | **Long** | The internal Billbee ID of the address record. Can be null if a new address is created |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**name2** | **String** | Optionally an additional name field |  [optional] |
|**restoredAt** | **OffsetDateTime** | If set, the customeraddress was restored from the archive at the given date. |  [optional] |
|**state** | **String** |  |  [optional] |
|**street** | **String** |  |  [optional] |
|**tel1** | **String** |  |  [optional] |
|**tel2** | **String** |  |  [optional] |
|**zip** | **String** |  |  [optional] |



## Enum: AddressTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



