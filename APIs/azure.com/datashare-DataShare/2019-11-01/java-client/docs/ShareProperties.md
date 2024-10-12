

# ShareProperties

Share property bag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Time at which the share was created. |  [optional] [readonly] |
|**description** | **String** | Share description. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets or sets the provisioning state |  [optional] [readonly] |
|**shareKind** | [**ShareKindEnum**](#ShareKindEnum) | Share kind. |  [optional] |
|**terms** | **String** | Share terms. |  [optional] |
|**userEmail** | **String** | Email of the user who created the resource |  [optional] [readonly] |
|**userName** | **String** | Name of the user who created the resource |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: ShareKindEnum

| Name | Value |
|---- | -----|
| COPY_BASED | &quot;CopyBased&quot; |
| IN_PLACE | &quot;InPlace&quot; |



