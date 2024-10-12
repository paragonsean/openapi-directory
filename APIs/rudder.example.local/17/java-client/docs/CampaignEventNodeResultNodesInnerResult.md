

# CampaignEventNodeResultNodesInnerResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errors** | **String** | campaign standard errors |  [optional] |
|**output** | **String** | campaign standard output |  [optional] |
|**softwareUpdated** | [**List&lt;CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner&gt;**](CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner.md) | List of updated software |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Campaign result |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| ERROR | &quot;error&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| MISSING | &quot;missing&quot; |



