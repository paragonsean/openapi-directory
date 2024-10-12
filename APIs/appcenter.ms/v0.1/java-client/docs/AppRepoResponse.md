

# AppRepoResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **UUID** | The unique id (UUID) of the app that this repository integration belongs to |  |
|**externalUserId** | **String** | User id from the provider |  [optional] |
|**id** | **UUID** | The unique id (UUID) of the repository integration |  |
|**installationId** | **String** | Installation id from the provider |  [optional] |
|**repoId** | **String** | Repository id from the provider |  [optional] |
|**repoProvider** | [**RepoProviderEnum**](#RepoProviderEnum) | The provider of the repository |  [optional] |
|**repoUrl** | **String** | The absolute URL of the repository |  |
|**serviceConnectionId** | **UUID** | The id of the service connection stored in customer credential store |  [optional] |
|**userId** | **UUID** | The unique id (UUID) of the user who configured the repository |  |



## Enum: RepoProviderEnum

| Name | Value |
|---- | -----|
| GITHUB | &quot;github&quot; |
| BITBUCKET | &quot;bitbucket&quot; |
| VSTS | &quot;vsts&quot; |
| GITLAB | &quot;gitlab&quot; |



