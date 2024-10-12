# FirebaseHostingApi.ServingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appAssociation** | **String** | How to handle well known App Association files. | [optional] 
**cleanUrls** | **Boolean** | Defines whether to drop the file extension from uploaded files. | [optional] 
**headers** | [**[Header]**](Header.md) | An array of objects, where each object specifies a URL pattern that, if matched to the request URL path, triggers Hosting to apply the specified custom response headers. | [optional] 
**i18n** | [**I18nConfig**](I18nConfig.md) |  | [optional] 
**redirects** | [**[Redirect]**](Redirect.md) | An array of objects (called redirect rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond with a redirect to the specified destination path. | [optional] 
**rewrites** | [**[Rewrite]**](Rewrite.md) | An array of objects (called rewrite rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond as if the service were given the specified destination URL. | [optional] 
**trailingSlashBehavior** | **String** | Defines how to handle a trailing slash in the URL path. | [optional] 



## Enum: AppAssociationEnum


* `AUTO` (value: `"AUTO"`)

* `NONE` (value: `"NONE"`)





## Enum: TrailingSlashBehaviorEnum


* `TRAILING_SLASH_BEHAVIOR_UNSPECIFIED` (value: `"TRAILING_SLASH_BEHAVIOR_UNSPECIFIED"`)

* `ADD` (value: `"ADD"`)

* `REMOVE` (value: `"REMOVE"`)




