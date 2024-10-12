# AppCenterClient.AppRepoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The unique id (UUID) of the app that this repository integration belongs to | 
**externalUserId** | **String** | User id from the provider | [optional] 
**id** | **String** | The unique id (UUID) of the repository integration | 
**installationId** | **String** | Installation id from the provider | [optional] 
**repoId** | **String** | Repository id from the provider | [optional] 
**repoProvider** | **String** | The provider of the repository | [optional] 
**repoUrl** | **String** | The absolute URL of the repository | 
**serviceConnectionId** | **String** | The id of the service connection stored in customer credential store | [optional] 
**userId** | **String** | The unique id (UUID) of the user who configured the repository | 



## Enum: RepoProviderEnum


* `github` (value: `"github"`)

* `bitbucket` (value: `"bitbucket"`)

* `vsts` (value: `"vsts"`)

* `gitlab` (value: `"gitlab"`)




