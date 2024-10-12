

# AddressesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**city** | **String** | City of the customer |  [optional] |
|**country** | **String** | Country of the customer |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**line1** | **String** | First line of the street address of the customer |  [optional] |
|**line2** | **String** | Second line of the street address of the customer |  [optional] |
|**postalCode** | **String** | Postal code of the customer |  [optional] |
|**state** | **String** | State of the customer |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BILLING | &quot;billing&quot; |
| SHIPPING | &quot;shipping&quot; |
| OTHER | &quot;other&quot; |



