# AppCenterClient.DistributionGroupWithUsersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadGroups** | [**[DistributionGroupWithUsersResponseAadGroupsInner]**](DistributionGroupWithUsersResponseAadGroupsInner.md) | The distribution group aad groups | [optional] 
**id** | **String** | The unique ID of the distribution group | 
**isPublic** | **Boolean** | Whether the distribution group is public | [optional] 
**name** | **String** | The name of the distribution group used in URLs | 
**notifiedUserCount** | **Number** | The count of non-pending users in the distribution group who will be notified by new releases | 
**totalGroupsCount** | **Number** | The count of aad groups in the distribution group | [optional] 
**totalUserCount** | **Number** | The count of users in the distribution group | 
**users** | [**[DistributionGroupsListUsers200ResponseInner]**](DistributionGroupsListUsers200ResponseInner.md) | The distribution group users | 


