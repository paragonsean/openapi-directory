

# NetworkingConfig

Configuration options for networking connections in the Composer 2 environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) | Optional. Indicates the user requested specifc connection type between Tenant and Customer projects. You cannot set networking connection type in public IP environment. |  [optional] |



## Enum: ConnectionTypeEnum

| Name | Value |
|---- | -----|
| CONNECTION_TYPE_UNSPECIFIED | &quot;CONNECTION_TYPE_UNSPECIFIED&quot; |
| VPC_PEERING | &quot;VPC_PEERING&quot; |
| PRIVATE_SERVICE_CONNECT | &quot;PRIVATE_SERVICE_CONNECT&quot; |



