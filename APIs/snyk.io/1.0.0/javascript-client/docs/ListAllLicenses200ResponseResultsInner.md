# SnykApi.ListAllLicenses200ResponseResultsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | [**[ListAllLicenses200ResponseResultsInnerDependenciesInner]**](ListAllLicenses200ResponseResultsInnerDependenciesInner.md) | The dependencies of projects in the organization which have the license | 
**id** | **String** | The identifier of the license | 
**instructions** | **String** | Custom instructions assigned to this license | [optional] 
**projects** | [**[ListAllDependencies200ResponseResultsInnerProjectsInner]**](ListAllDependencies200ResponseResultsInnerProjectsInner.md) | The projects which contain the license | 
**severity** | **String** | The severity assigned to this license | [optional] 



## Enum: SeverityEnum


* `none` (value: `"none"`)

* `high` (value: `"high"`)

* `medium` (value: `"medium"`)

* `low` (value: `"low"`)




