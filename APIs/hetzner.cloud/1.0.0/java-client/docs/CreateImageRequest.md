

# CreateImageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the Image, will be auto-generated if not set |  [optional] |
|**labels** | [**CreateLoadBalancerRequestLabels**](CreateLoadBalancerRequestLabels.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of Image to create (default: &#x60;snapshot&#x60;) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SNAPSHOT | &quot;snapshot&quot; |
| BACKUP | &quot;backup&quot; |



