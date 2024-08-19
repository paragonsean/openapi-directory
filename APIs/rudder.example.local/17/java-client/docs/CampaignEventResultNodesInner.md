

# CampaignEventResultNodesInner

Campaign result for a Node

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **LocalDate** |  |  [optional] |
|**nbPackages** | **Integer** | Number of software updated |  [optional] |
|**nodeId** | **String** | Node id |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Campaign status |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| ERROR | &quot;error&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| MISSING | &quot;missing&quot; |



