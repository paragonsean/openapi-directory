

# CarrierAndIspTargetingOptionDetails

Represents a targetable carrier or ISP. This will be populated in the carrier_and_isp_details field of a TargetingOption when targeting_type is `TARGETING_TYPE_CARRIER_AND_ISP`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Output only. The display name of the carrier or ISP. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type indicating if it&#39;s carrier or ISP. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CARRIER_AND_ISP_TYPE_UNSPECIFIED&quot; |
| ISP | &quot;CARRIER_AND_ISP_TYPE_ISP&quot; |
| CARRIER | &quot;CARRIER_AND_ISP_TYPE_CARRIER&quot; |



