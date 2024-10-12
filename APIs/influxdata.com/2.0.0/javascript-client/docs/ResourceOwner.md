# InfluxOssApiService.ResourceOwner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] [readonly] 
**links** | [**UserResponseLinks**](UserResponseLinks.md) |  | [optional] 
**name** | **String** |  | 
**oauthID** | **String** |  | [optional] 
**status** | **String** | If inactive the user is inactive. | [optional] [default to &#39;active&#39;]
**role** | **String** |  | [optional] [default to &#39;owner&#39;]



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)





## Enum: RoleEnum


* `owner` (value: `"owner"`)




