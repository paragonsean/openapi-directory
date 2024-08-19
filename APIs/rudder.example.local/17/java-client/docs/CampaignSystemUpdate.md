

# CampaignSystemUpdate

System update campaign details (type system-update, version 2)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reboot** | [**RebootEnum**](#RebootEnum) | Define the behavior after update |  [optional] |
|**targets** | **List&lt;List&lt;RuleTargetsInner&gt;&gt;** | List of all  groups of node to target the campaign |  [optional] |



## Enum: RebootEnum

| Name | Value |
|---- | -----|
| AS_NEEDED | &quot;as-needed&quot; |
| DISABLED | &quot;disabled&quot; |
| ALWAYS | &quot;always&quot; |
| SERVICES_ONLY | &quot;services-only&quot; |



