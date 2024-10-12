

# CampaignSoftwareUpdate

Software update campaign details (type software-update, version 1)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reboot** | [**RebootEnum**](#RebootEnum) | Define the behavior after update |  [optional] |
|**softwareUpdate** | [**List&lt;CampaignSoftwareUpdateSoftwareUpdateInner&gt;**](CampaignSoftwareUpdateSoftwareUpdateInner.md) | List of all software to update |  [optional] |
|**targets** | **List&lt;List&lt;RuleTargetsInner&gt;&gt;** | List of all  groups of node to target the campaign |  [optional] |



## Enum: RebootEnum

| Name | Value |
|---- | -----|
| AS_NEEDED | &quot;as-needed&quot; |
| DISABLED | &quot;disabled&quot; |
| ALWAYS | &quot;always&quot; |
| SERVICES_ONLY | &quot;services-only&quot; |



