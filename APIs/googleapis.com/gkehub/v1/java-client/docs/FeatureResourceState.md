

# FeatureResourceState

FeatureResourceState describes the state of a Feature *resource* in the GkeHub API. See `FeatureState` for the \"running state\" of the Feature in the Hub and across Memberships.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | [**StateEnum**](#StateEnum) | The current state of the Feature resource in the Hub API. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ENABLING | &quot;ENABLING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DISABLING | &quot;DISABLING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| SERVICE_UPDATING | &quot;SERVICE_UPDATING&quot; |



