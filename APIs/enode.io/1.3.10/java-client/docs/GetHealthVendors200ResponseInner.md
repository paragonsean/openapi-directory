

# GetHealthVendors200ResponseInner

Vendor status and metadata

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Displayable name of the Vendor |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Ready-state of the Vendor |  [optional] |
|**vendor** | **Object** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;READY&quot; |
| ELEVATED_ERROR_RATE | &quot;ELEVATED_ERROR_RATE&quot; |
| OUTAGE | &quot;OUTAGE&quot; |



