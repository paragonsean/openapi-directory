

# DirectConnection

The properties that define a direct connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthInMbps** | **Integer** | The bandwidth of the connection. |  [optional] |
|**bgpSession** | [**BgpSession**](BgpSession.md) |  |  [optional] |
|**connectionIdentifier** | **String** | The unique identifier (GUID) for the connection. |  [optional] |
|**connectionState** | [**ConnectionStateEnum**](#ConnectionStateEnum) | The state of the connection. |  [optional] [readonly] |
|**peeringDBFacilityId** | **Integer** | The PeeringDB.com ID of the facility at which the connection has to be set up. |  [optional] |
|**provisionedBandwidthInMbps** | **Integer** | The bandwidth that is actually provisioned. |  [optional] |
|**sessionAddressProvider** | [**SessionAddressProviderEnum**](#SessionAddressProviderEnum) | The field indicating if Microsoft provides session ip addresses. |  [optional] |
|**useForPeeringService** | **Boolean** | The flag that indicates whether or not the connection is used for peering service. |  [optional] |



## Enum: ConnectionStateEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PENDING_APPROVAL | &quot;PendingApproval&quot; |
| APPROVED | &quot;Approved&quot; |
| PROVISIONING_STARTED | &quot;ProvisioningStarted&quot; |
| PROVISIONING_FAILED | &quot;ProvisioningFailed&quot; |
| PROVISIONING_COMPLETED | &quot;ProvisioningCompleted&quot; |
| VALIDATING | &quot;Validating&quot; |
| ACTIVE | &quot;Active&quot; |



## Enum: SessionAddressProviderEnum

| Name | Value |
|---- | -----|
| MICROSOFT | &quot;Microsoft&quot; |
| PEER | &quot;Peer&quot; |



