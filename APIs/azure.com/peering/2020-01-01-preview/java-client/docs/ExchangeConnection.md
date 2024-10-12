

# ExchangeConnection

The properties that define an exchange connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bgpSession** | [**BgpSession**](BgpSession.md) |  |  [optional] |
|**connectionIdentifier** | **String** | The unique identifier (GUID) for the connection. |  [optional] |
|**connectionState** | [**ConnectionStateEnum**](#ConnectionStateEnum) | The state of the connection. |  [optional] [readonly] |
|**errorMessage** | **String** | The error message related to the connection state, if any. |  [optional] [readonly] |
|**peeringDBFacilityId** | **Integer** | The PeeringDB.com ID of the facility at which the connection has to be set up. |  [optional] |



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



