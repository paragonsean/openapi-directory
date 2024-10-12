

# Instance

A Looker instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminSettings** | [**AdminSettings**](AdminSettings.md) |  |  [optional] |
|**consumerNetwork** | **String** | Network name in the consumer project. Format: &#x60;projects/{project}/global/networks/{network}&#x60;. Note that the consumer network may be in a different GCP project than the consumer project that is hosting the Looker Instance. |  [optional] |
|**createTime** | **String** | Output only. The time when the Looker instance provisioning was first requested. |  [optional] [readonly] |
|**customDomain** | [**CustomDomain**](CustomDomain.md) |  |  [optional] |
|**denyMaintenancePeriod** | [**DenyMaintenancePeriod**](DenyMaintenancePeriod.md) |  |  [optional] |
|**egressPublicIp** | **String** | Output only. Public Egress IP (IPv4). |  [optional] [readonly] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**ingressPrivateIp** | **String** | Output only. Private Ingress IP (IPv4). |  [optional] [readonly] |
|**ingressPublicIp** | **String** | Output only. Public Ingress IP (IPv4). |  [optional] [readonly] |
|**lastDenyMaintenancePeriod** | [**DenyMaintenancePeriod**](DenyMaintenancePeriod.md) |  |  [optional] |
|**lookerUri** | **String** | Output only. Looker instance URI which can be used to access the Looker Instance UI. |  [optional] [readonly] |
|**lookerVersion** | **String** | Output only. The Looker version that the instance is using. |  [optional] [readonly] |
|**maintenanceSchedule** | [**MaintenanceSchedule**](MaintenanceSchedule.md) |  |  [optional] |
|**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  |  [optional] |
|**name** | **String** | Output only. Format: &#x60;projects/{project}/locations/{location}/instances/{instance}&#x60;. |  [optional] [readonly] |
|**oauthConfig** | [**OAuthConfig**](OAuthConfig.md) |  |  [optional] |
|**platformEdition** | [**PlatformEditionEnum**](#PlatformEditionEnum) | Platform edition. |  [optional] |
|**privateIpEnabled** | **Boolean** | Whether private IP is enabled on the Looker instance. |  [optional] |
|**pscConfig** | [**PscConfig**](PscConfig.md) |  |  [optional] |
|**pscEnabled** | **Boolean** | Optional. Whether to use Private Service Connect (PSC) for private IP connectivity. If true, VPC peering (PSA) will not be used. |  [optional] |
|**publicIpEnabled** | **Boolean** | Whether public IP is enabled on the Looker instance. |  [optional] |
|**reservedRange** | **String** | Name of a reserved IP address range within the Instance.consumer_network, to be used for private services access connection. May or may not be specified in a create request. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the instance. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the Looker instance was last updated. |  [optional] [readonly] |
|**userMetadata** | [**UserMetadata**](UserMetadata.md) |  |  [optional] |



## Enum: PlatformEditionEnum

| Name | Value |
|---- | -----|
| PLATFORM_EDITION_UNSPECIFIED | &quot;PLATFORM_EDITION_UNSPECIFIED&quot; |
| LOOKER_CORE_TRIAL | &quot;LOOKER_CORE_TRIAL&quot; |
| LOOKER_CORE_STANDARD | &quot;LOOKER_CORE_STANDARD&quot; |
| LOOKER_CORE_STANDARD_ANNUAL | &quot;LOOKER_CORE_STANDARD_ANNUAL&quot; |
| LOOKER_CORE_ENTERPRISE_ANNUAL | &quot;LOOKER_CORE_ENTERPRISE_ANNUAL&quot; |
| LOOKER_CORE_EMBED_ANNUAL | &quot;LOOKER_CORE_EMBED_ANNUAL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| FAILED | &quot;FAILED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| EXPORTING | &quot;EXPORTING&quot; |
| IMPORTING | &quot;IMPORTING&quot; |



