

# Gateway

Gateway represents a user facing component that serves as an entrance to enable connectivity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of hosting used by the gateway. |  [optional] |
|**uri** | **String** | Output only. Server-defined URI for this resource. |  [optional] [readonly] |
|**userPort** | **Integer** | Output only. User port reserved on the gateways for this connection, if not specified or zero, the default port is 19443. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GCP_REGIONAL_MIG | &quot;GCP_REGIONAL_MIG&quot; |



