

# ShareSubscriptionProperties

Share subscription property bag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Time at which the share subscription was created. |  [optional] [readonly] |
|**invitationId** | **String** | The invitation id. |  |
|**providerEmail** | **String** | Email of the provider who created the resource |  [optional] [readonly] |
|**providerName** | **String** | Name of the provider who created the resource |  [optional] [readonly] |
|**providerTenantName** | **String** | Tenant name of the provider who created the resource |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the share subscription |  [optional] [readonly] |
|**shareDescription** | **String** | Description of share |  [optional] [readonly] |
|**shareKind** | [**ShareKindEnum**](#ShareKindEnum) | Kind of share |  [optional] [readonly] |
|**shareName** | **String** | Name of the share |  [optional] [readonly] |
|**shareSubscriptionStatus** | [**ShareSubscriptionStatusEnum**](#ShareSubscriptionStatusEnum) | Gets the current status of share subscription. |  [optional] [readonly] |
|**shareTerms** | **String** | Terms of a share |  [optional] [readonly] |
|**sourceShareLocation** | **String** | Source share location. |  |
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



## Enum: ShareSubscriptionStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| REVOKED | &quot;Revoked&quot; |
| SOURCE_DELETED | &quot;SourceDeleted&quot; |
| REVOKING | &quot;Revoking&quot; |



