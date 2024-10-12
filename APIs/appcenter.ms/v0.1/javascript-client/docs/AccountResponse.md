# AppCenterClient.AccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The display name of the account | 
**email** | **String** | The account&#39;s email. For org that value might be empty. | [optional] 
**id** | **String** | The internal unique id (UUID) of the account. | 
**name** | **String** | The slug name of the account | 
**origin** | **String** | The creation origin of this account | 
**type** | **String** | The type of this account | 



## Enum: OriginEnum


* `appcenter` (value: `"appcenter"`)

* `hockeyapp` (value: `"hockeyapp"`)





## Enum: TypeEnum


* `user` (value: `"user"`)

* `org` (value: `"org"`)




