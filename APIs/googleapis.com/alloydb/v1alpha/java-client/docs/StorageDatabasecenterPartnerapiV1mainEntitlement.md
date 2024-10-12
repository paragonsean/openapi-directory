

# StorageDatabasecenterPartnerapiV1mainEntitlement

Proto representing the access that a user has to a specific feature/service. NextId: 3.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entitlementState** | [**EntitlementStateEnum**](#EntitlementStateEnum) | The current state of user&#39;s accessibility to a feature/benefit. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | An enum that represents the type of this entitlement. |  [optional] |



## Enum: EntitlementStateEnum

| Name | Value |
|---- | -----|
| ENTITLEMENT_STATE_UNSPECIFIED | &quot;ENTITLEMENT_STATE_UNSPECIFIED&quot; |
| ENTITLED | &quot;ENTITLED&quot; |
| REVOKED | &quot;REVOKED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ENTITLEMENT_TYPE_UNSPECIFIED | &quot;ENTITLEMENT_TYPE_UNSPECIFIED&quot; |
| DUET_AI | &quot;DUET_AI&quot; |



