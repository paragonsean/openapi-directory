

# AccountReturnCarrier

 The return carrier information. This service is designed for merchants enrolled in the Buy on Google program. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierAccountId** | **String** | Output only. Immutable. The Google-provided unique carrier ID, used to update the resource. |  [optional] [readonly] |
|**carrierAccountName** | **String** | Name of the carrier account. |  [optional] |
|**carrierAccountNumber** | **String** | Number of the carrier account. |  [optional] |
|**carrierCode** | [**CarrierCodeEnum**](#CarrierCodeEnum) | The carrier code enum. Accepts the values FEDEX or UPS. |  [optional] |



## Enum: CarrierCodeEnum

| Name | Value |
|---- | -----|
| CARRIER_CODE_UNSPECIFIED | &quot;CARRIER_CODE_UNSPECIFIED&quot; |
| FEDEX | &quot;FEDEX&quot; |
| UPS | &quot;UPS&quot; |



