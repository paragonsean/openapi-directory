

# StationNetworkTierOneData

Metadata about the top-level organization in the network, if this station is part of a network

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The unique identifier of the top-level organization in the network |  |
|**name** | **String** | The display name for the top-level organization in the network |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the top-level organization within NPR&#39;s system, not typically used by consumers |  [optional] |
|**tier2** | [**List&lt;StationNetworkTierTwoData&gt;**](StationNetworkTierTwoData.md) | One or more stations that are hierarchical children of this organization |  [optional] |
|**usesInheritance** | **Boolean** | Whether or not this station inherits from a parent organization, also referred to as a network |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| _1 | &quot;1&quot; |
| _9 | &quot;9&quot; |
| _10 | &quot;10&quot; |
| _12 | &quot;12&quot; |
| _15 | &quot;15&quot; |



