# PeeringManagementClient.DirectConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthInMbps** | **Number** | The bandwidth of the connection. | [optional] 
**bgpSession** | [**BgpSession**](BgpSession.md) |  | [optional] 
**connectionIdentifier** | **String** | The unique identifier (GUID) for the connection. | [optional] 
**connectionState** | **String** | The state of the connection. | [optional] [readonly] 
**errorMessage** | **String** | The error message related to the connection state, if any. | [optional] [readonly] 
**peeringDBFacilityId** | **Number** | The PeeringDB.com ID of the facility at which the connection has to be set up. | [optional] 
**provisionedBandwidthInMbps** | **Number** | The bandwidth that is actually provisioned. | [optional] [readonly] 
**sessionAddressProvider** | **String** | The field indicating if Microsoft provides session ip addresses. | [optional] 
**useForPeeringService** | **Boolean** | The flag that indicates whether or not the connection is used for peering service. | [optional] 



## Enum: ConnectionStateEnum


* `None` (value: `"None"`)

* `PendingApproval` (value: `"PendingApproval"`)

* `Approved` (value: `"Approved"`)

* `ProvisioningStarted` (value: `"ProvisioningStarted"`)

* `ProvisioningFailed` (value: `"ProvisioningFailed"`)

* `ProvisioningCompleted` (value: `"ProvisioningCompleted"`)

* `Validating` (value: `"Validating"`)

* `Active` (value: `"Active"`)





## Enum: SessionAddressProviderEnum


* `Microsoft` (value: `"Microsoft"`)

* `Peer` (value: `"Peer"`)




