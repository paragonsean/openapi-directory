# GiteaApi.CreateHookOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** |  | [optional] [default to false]
**authorizationHeader** | **String** |  | [optional] 
**branchFilter** | **String** |  | [optional] 
**config** | **{String: String}** | CreateHookOptionConfig has all config options in it required are \&quot;content_type\&quot; and \&quot;url\&quot; Required | 
**events** | **[String]** |  | [optional] 
**type** | **String** |  | 



## Enum: TypeEnum


* `dingtalk` (value: `"dingtalk"`)

* `discord` (value: `"discord"`)

* `gitea` (value: `"gitea"`)

* `gogs` (value: `"gogs"`)

* `msteams` (value: `"msteams"`)

* `slack` (value: `"slack"`)

* `telegram` (value: `"telegram"`)

* `feishu` (value: `"feishu"`)

* `wechatwork` (value: `"wechatwork"`)

* `packagist` (value: `"packagist"`)




