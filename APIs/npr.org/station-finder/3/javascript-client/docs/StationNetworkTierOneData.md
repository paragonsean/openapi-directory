# NprStationFinderService.StationNetworkTierOneData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The unique identifier of the top-level organization in the network | 
**name** | **String** | The display name for the top-level organization in the network | 
**status** | **String** | The status of the top-level organization within NPR&#39;s system, not typically used by consumers | [optional] [default to &#39;10&#39;]
**tier2** | [**[StationNetworkTierTwoData]**](StationNetworkTierTwoData.md) | One or more stations that are hierarchical children of this organization | [optional] 
**usesInheritance** | **Boolean** | Whether or not this station inherits from a parent organization, also referred to as a network | 



## Enum: StatusEnum


* `1` (value: `"1"`)

* `9` (value: `"9"`)

* `10` (value: `"10"`)

* `12` (value: `"12"`)

* `15` (value: `"15"`)




