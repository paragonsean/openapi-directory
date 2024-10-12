# InfluxOssApiService.Authorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the token. | [optional] 
**status** | **String** | If inactive the token is inactive and requests using the token will be rejected. | [optional] [default to &#39;active&#39;]
**createdAt** | **Date** |  | [optional] [readonly] 
**id** | **String** |  | [optional] [readonly] 
**links** | [**AuthorizationAllOfLinks**](AuthorizationAllOfLinks.md) |  | [optional] 
**org** | **String** | Name of the org token is scoped to. | [optional] [readonly] 
**orgID** | **String** | ID of org that authorization is scoped to. | 
**permissions** | [**[Permission]**](Permission.md) | List of permissions for an auth.  An auth must have at least one Permission. | 
**token** | **String** | Passed via the Authorization Header and Token Authentication type. | [optional] [readonly] 
**updatedAt** | **Date** |  | [optional] [readonly] 
**user** | **String** | Name of user that created and owns the token. | [optional] [readonly] 
**userID** | **String** | ID of user that created and owns the token. | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)




