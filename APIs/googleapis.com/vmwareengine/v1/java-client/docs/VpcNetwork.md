

# VpcNetwork

Represents a VMware Engine VPC network that is managed by a VMware Engine network resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**network** | **String** | Output only. The relative resource name of the service VPC network this VMware Engine network is attached to. For example: &#x60;projects/123123/global/networks/my-network&#x60; |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Type of VPC network (INTRANET, INTERNET, or GOOGLE_CLOUD) |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| INTRANET | &quot;INTRANET&quot; |
| INTERNET | &quot;INTERNET&quot; |
| GOOGLE_CLOUD | &quot;GOOGLE_CLOUD&quot; |



