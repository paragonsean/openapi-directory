

# CloudResource

The resource on GCP

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Output only. ComputeInstance, ComputeDisk, VPC, Bare Metal server, etc. |  [optional] [readonly] |
|**name** | **String** | Output only. resource name |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;RESOURCE_KIND_UNSPECIFIED&quot; |
| INSTANCE | &quot;RESOURCE_KIND_INSTANCE&quot; |
| DISK | &quot;RESOURCE_KIND_DISK&quot; |
| ADDRESS | &quot;RESOURCE_KIND_ADDRESS&quot; |
| FILESTORE | &quot;RESOURCE_KIND_FILESTORE&quot; |
| HEALTH_CHECK | &quot;RESOURCE_KIND_HEALTH_CHECK&quot; |
| FORWARDING_RULE | &quot;RESOURCE_KIND_FORWARDING_RULE&quot; |
| BACKEND_SERVICE | &quot;RESOURCE_KIND_BACKEND_SERVICE&quot; |
| SUBNETWORK | &quot;RESOURCE_KIND_SUBNETWORK&quot; |
| NETWORK | &quot;RESOURCE_KIND_NETWORK&quot; |
| PUBLIC_ADDRESS | &quot;RESOURCE_KIND_PUBLIC_ADDRESS&quot; |
| INSTANCE_GROUP | &quot;RESOURCE_KIND_INSTANCE_GROUP&quot; |



