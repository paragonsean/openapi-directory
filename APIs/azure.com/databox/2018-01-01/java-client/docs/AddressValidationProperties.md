

# AddressValidationProperties

The address validation output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateAddresses** | [**List&lt;ShippingAddress&gt;**](ShippingAddress.md) | List of alternate addresses. |  [optional] [readonly] |
|**validationStatus** | [**ValidationStatusEnum**](#ValidationStatusEnum) | The address validation status. |  [optional] [readonly] |



## Enum: ValidationStatusEnum

| Name | Value |
|---- | -----|
| VALID | &quot;Valid&quot; |
| INVALID | &quot;Invalid&quot; |
| AMBIGUOUS | &quot;Ambiguous&quot; |



