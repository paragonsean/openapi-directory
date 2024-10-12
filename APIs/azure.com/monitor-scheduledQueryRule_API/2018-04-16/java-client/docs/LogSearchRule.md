

# LogSearchRule

Log Search Rule Definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**Action**](Action.md) |  |  |
|**description** | **String** | The description of the Log Search rule. |  [optional] |
|**enabled** | [**EnabledEnum**](#EnabledEnum) | The flag which indicates whether the Log Search rule is enabled. Value should be true or false |  [optional] |
|**lastUpdatedTime** | **OffsetDateTime** | Last time the rule was updated in IS08601 format. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the scheduled query rule |  [optional] [readonly] |
|**schedule** | [**Schedule**](Schedule.md) |  |  [optional] |
|**source** | [**Source**](Source.md) |  |  |



## Enum: EnabledEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| DEPLOYING | &quot;Deploying&quot; |
| CANCELED | &quot;Canceled&quot; |
| FAILED | &quot;Failed&quot; |



