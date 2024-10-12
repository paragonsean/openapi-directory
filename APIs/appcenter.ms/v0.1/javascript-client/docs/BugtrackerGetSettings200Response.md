# AppCenterClient.BugtrackerGetSettings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventTypes** | **[String]** | Event types enabled for bugtracker | [optional] 
**settings** | [**BugtrackerGetSettings200ResponseSettings**](BugtrackerGetSettings200ResponseSettings.md) |  | [optional] 
**state** | **String** | bugtracker state | [optional] 
**tokenId** | **String** | ID of OAuth token | [optional] 
**type** | **String** | type of bugtracker | [optional] 



## Enum: [EventTypesEnum]


* `newCrashGroupCreated` (value: `"newCrashGroupCreated"`)

* `newAppReleased` (value: `"newAppReleased"`)





## Enum: StateEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)

* `unauthorized` (value: `"unauthorized"`)





## Enum: TypeEnum


* `github` (value: `"github"`)

* `vsts` (value: `"vsts"`)

* `jira` (value: `"jira"`)




