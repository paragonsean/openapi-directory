

# DescribeAcceleratorOfferingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationType** | [**LocationTypeEnum**](#LocationTypeEnum) |  The location type that you want to describe accelerator type offerings for. It can assume the following values: region: will return the accelerator type offering at the regional level. availability-zone: will return the accelerator type offering at the availability zone level. availability-zone-id: will return the accelerator type offering at the availability zone level returning the availability zone id.  |  |
|**acceleratorTypes** | **List&lt;String&gt;** |  The list of accelerator types to describe.  |  [optional] |



## Enum: LocationTypeEnum

| Name | Value |
|---- | -----|
| REGION | &quot;region&quot; |
| AVAILABILITY_ZONE | &quot;availability-zone&quot; |
| AVAILABILITY_ZONE_ID | &quot;availability-zone-id&quot; |



