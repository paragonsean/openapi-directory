# TheJiraCloudPlatformRestApi.ApplicationRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultGroups** | **[String]** | The groups that are granted default access for this application role. As a group&#39;s name can change, use of &#x60;defaultGroupsDetails&#x60; is recommended to identify a groups. | [optional] 
**defaultGroupsDetails** | [**[GroupName]**](GroupName.md) | The groups that are granted default access for this application role. | [optional] 
**defined** | **Boolean** | Deprecated. | [optional] 
**groupDetails** | [**[GroupName]**](GroupName.md) | The groups associated with the application role. | [optional] 
**groups** | **[String]** | The groups associated with the application role. As a group&#39;s name can change, use of &#x60;groupDetails&#x60; is recommended to identify a groups. | [optional] 
**hasUnlimitedSeats** | **Boolean** |  | [optional] 
**key** | **String** | The key of the application role. | [optional] 
**name** | **String** | The display name of the application role. | [optional] 
**numberOfSeats** | **Number** | The maximum count of users on your license. | [optional] 
**platform** | **Boolean** | Indicates if the application role belongs to Jira platform (&#x60;jira-core&#x60;). | [optional] 
**remainingSeats** | **Number** | The count of users remaining on your license. | [optional] 
**selectedByDefault** | **Boolean** | Determines whether this application role should be selected by default on user creation. | [optional] 
**userCount** | **Number** | The number of users counting against your license. | [optional] 
**userCountDescription** | **String** | The [type of users](https://confluence.atlassian.com/x/lRW3Ng) being counted against your license. | [optional] 


