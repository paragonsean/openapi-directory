# InfluxOssApiService.AuthorizationPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the token. | [optional] 
**status** | **String** | If inactive the token is inactive and requests using the token will be rejected. | [optional] [default to &#39;active&#39;]
**orgID** | **String** | ID of org that authorization is scoped to. | 
**permissions** | [**[Permission]**](Permission.md) | List of permissions for an auth.  An auth must have at least one Permission. | 
**userID** | **String** | ID of user that authorization is scoped to. | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)




