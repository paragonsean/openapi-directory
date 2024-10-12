# PeeringManagementClient.ExchangeConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgpSession** | [**BgpSession**](BgpSession.md) |  | [optional] 
**connectionState** | **String** | The state of the connection. | [optional] [readonly] 
**peeringDBFacilityId** | **Number** | The PeeringDB.com ID of the facility at which the connection has to be set up. | [optional] 



## Enum: ConnectionStateEnum


* `None` (value: `"None"`)

* `PendingApproval` (value: `"PendingApproval"`)

* `Approved` (value: `"Approved"`)

* `ProvisioningStarted` (value: `"ProvisioningStarted"`)

* `ProvisioningFailed` (value: `"ProvisioningFailed"`)

* `ProvisioningCompleted` (value: `"ProvisioningCompleted"`)

* `Validating` (value: `"Validating"`)

* `Active` (value: `"Active"`)




