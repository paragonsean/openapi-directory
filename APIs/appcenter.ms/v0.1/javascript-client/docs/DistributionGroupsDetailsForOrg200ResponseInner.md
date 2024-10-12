# AppCenterClient.DistributionGroupsDetailsForOrg200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The name of the distribution group | [optional] 
**id** | **String** | The unique ID of the distribution group | 
**isPublic** | **Boolean** | Whether the distribution group is public | 
**name** | **String** | The name of the distribution group used in URLs | 
**origin** | **String** | The creation origin of this distribution group | 
**apps** | [**[AppsList200ResponseInner]**](AppsList200ResponseInner.md) | The apps associated with the distribution group | 
**totalAppsCount** | **Number** | The count of apps associated with this distribution group | 
**totalUsersCount** | **Number** | The count of users in the distribution group | 



## Enum: OriginEnum


* `appcenter` (value: `"appcenter"`)

* `hockeyapp` (value: `"hockeyapp"`)




