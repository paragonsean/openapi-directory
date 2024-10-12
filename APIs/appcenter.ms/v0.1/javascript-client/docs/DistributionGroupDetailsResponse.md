# AppCenterClient.DistributionGroupDetailsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The name of the distribution group | [optional] 
**id** | **String** | The unique ID of the distribution group | 
**isPublic** | **Boolean** | Whether the distribution group is public | 
**name** | **String** | The name of the distribution group used in URLs | 
**origin** | **String** | The creation origin of this distribution group | 
**groupType** | **String** | Type of group (Default, HockeyAppDefault or MicrosoftDogfooding) | [optional] 
**isShared** | **Boolean** | Whether the distribution group is shared group or not | 
**notifiedUserCount** | **Number** | The count of non-pending users in the distribution group who will be notified by new releases | 
**totalAppsCount** | **Number** | The count of apps associated with this distribution group | 
**totalUserCount** | **Number** | The count of users in the distribution group | 
**users** | [**[DistributionGroupsListUsers200ResponseInner]**](DistributionGroupsListUsers200ResponseInner.md) | The distribution group users | 



## Enum: OriginEnum


* `appcenter` (value: `"appcenter"`)

* `hockeyapp` (value: `"hockeyapp"`)





## Enum: GroupTypeEnum


* `Default` (value: `"Default"`)

* `HockeyAppDefault` (value: `"HockeyAppDefault"`)

* `MicrosoftDogfooding` (value: `"MicrosoftDogfooding"`)




