# AppCenterClient.RepositoryConfigurationsList200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Repository configuration identifier | 
**state** | **String** | State of the configuration | 
**type** | **String** | Type of repository | 
**userEmail** | **String** | Email of the user who linked the repository | [optional] 
**installationId** | **String** | The GitHub App Installation id. Required for repositories connected from GitHub App | [optional] 
**externalUserId** | **String** | The external user id from the repository provider. Required for GitLab.com repositories | [optional] 
**repoId** | **String** | The repository id from the repository provider. Required for repositories connected from GitHub App and GitLab.com | [optional] 
**repoUrl** | **String** | The repository&#39;s git url, must be a HTTPS URL | 
**serviceConnectionId** | **String** | The id of the service connection (private). Required for GitLab self-hosted repositories | [optional] 



## Enum: StateEnum


* `unauthorized` (value: `"unauthorized"`)

* `inactive` (value: `"inactive"`)

* `active` (value: `"active"`)




