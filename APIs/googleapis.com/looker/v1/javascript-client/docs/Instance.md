# LookerGoogleCloudCoreApi.Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminSettings** | [**AdminSettings**](AdminSettings.md) |  | [optional] 
**consumerNetwork** | **String** | Network name in the consumer project. Format: &#x60;projects/{project}/global/networks/{network}&#x60;. Note that the consumer network may be in a different GCP project than the consumer project that is hosting the Looker Instance. | [optional] 
**createTime** | **String** | Output only. The time when the Looker instance provisioning was first requested. | [optional] [readonly] 
**customDomain** | [**CustomDomain**](CustomDomain.md) |  | [optional] 
**denyMaintenancePeriod** | [**DenyMaintenancePeriod**](DenyMaintenancePeriod.md) |  | [optional] 
**egressPublicIp** | **String** | Output only. Public Egress IP (IPv4). | [optional] [readonly] 
**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**ingressPrivateIp** | **String** | Output only. Private Ingress IP (IPv4). | [optional] [readonly] 
**ingressPublicIp** | **String** | Output only. Public Ingress IP (IPv4). | [optional] [readonly] 
**lastDenyMaintenancePeriod** | [**DenyMaintenancePeriod**](DenyMaintenancePeriod.md) |  | [optional] 
**lookerUri** | **String** | Output only. Looker instance URI which can be used to access the Looker Instance UI. | [optional] [readonly] 
**lookerVersion** | **String** | Output only. The Looker version that the instance is using. | [optional] [readonly] 
**maintenanceSchedule** | [**MaintenanceSchedule**](MaintenanceSchedule.md) |  | [optional] 
**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 
**name** | **String** | Output only. Format: &#x60;projects/{project}/locations/{location}/instances/{instance}&#x60;. | [optional] [readonly] 
**oauthConfig** | [**OAuthConfig**](OAuthConfig.md) |  | [optional] 
**platformEdition** | **String** | Platform edition. | [optional] 
**privateIpEnabled** | **Boolean** | Whether private IP is enabled on the Looker instance. | [optional] 
**pscConfig** | [**PscConfig**](PscConfig.md) |  | [optional] 
**pscEnabled** | **Boolean** | Optional. Whether to use Private Service Connect (PSC) for private IP connectivity. If true, VPC peering (PSA) will not be used. | [optional] 
**publicIpEnabled** | **Boolean** | Whether public IP is enabled on the Looker instance. | [optional] 
**reservedRange** | **String** | Name of a reserved IP address range within the Instance.consumer_network, to be used for private services access connection. May or may not be specified in a create request. | [optional] 
**state** | **String** | Output only. The state of the instance. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the Looker instance was last updated. | [optional] [readonly] 
**userMetadata** | [**UserMetadata**](UserMetadata.md) |  | [optional] 



## Enum: PlatformEditionEnum


* `PLATFORM_EDITION_UNSPECIFIED` (value: `"PLATFORM_EDITION_UNSPECIFIED"`)

* `LOOKER_CORE_TRIAL` (value: `"LOOKER_CORE_TRIAL"`)

* `LOOKER_CORE_STANDARD` (value: `"LOOKER_CORE_STANDARD"`)

* `LOOKER_CORE_STANDARD_ANNUAL` (value: `"LOOKER_CORE_STANDARD_ANNUAL"`)

* `LOOKER_CORE_ENTERPRISE_ANNUAL` (value: `"LOOKER_CORE_ENTERPRISE_ANNUAL"`)

* `LOOKER_CORE_EMBED_ANNUAL` (value: `"LOOKER_CORE_EMBED_ANNUAL"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `FAILED` (value: `"FAILED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `EXPORTING` (value: `"EXPORTING"`)

* `IMPORTING` (value: `"IMPORTING"`)




