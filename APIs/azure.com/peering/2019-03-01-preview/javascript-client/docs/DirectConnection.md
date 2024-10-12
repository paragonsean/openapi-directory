# PeeringManagementClient.DirectConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthInMbps** | **Number** | The bandwidth of the connection. | [optional] 
**bgpSession** | [**BgpSession**](BgpSession.md) |  | [optional] 
**connectionState** | **String** | The state of the connection. | [optional] [readonly] 
**peeringDBFacilityId** | **Number** | The PeeringDB.com ID of the facility at which the connection has to be set up. | [optional] 
**provisionedBandwidthInMbps** | **Number** | The bandwidth that is actually provisioned. | [optional] 



## Enum: ConnectionStateEnum


* `None` (value: `"None"`)

* `PendingApproval` (value: `"PendingApproval"`)

* `Approved` (value: `"Approved"`)

* `ProvisioningStarted` (value: `"ProvisioningStarted"`)

* `ProvisioningFailed` (value: `"ProvisioningFailed"`)

* `ProvisioningCompleted` (value: `"ProvisioningCompleted"`)

* `Validating` (value: `"Validating"`)

* `Active` (value: `"Active"`)




