

# ServingConfig

The configuration for how incoming requests to a site should be routed and processed before serving content. The URL request paths are matched against the specified URL patterns in the configuration, then Hosting applies the applicable configuration according to a specific [priority order](https://firebase.google.com/docs/hosting/full-config#hosting_priority_order).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appAssociation** | [**AppAssociationEnum**](#AppAssociationEnum) | How to handle well known App Association files. |  [optional] |
|**cleanUrls** | **Boolean** | Defines whether to drop the file extension from uploaded files. |  [optional] |
|**headers** | [**List&lt;Header&gt;**](Header.md) | An array of objects, where each object specifies a URL pattern that, if matched to the request URL path, triggers Hosting to apply the specified custom response headers. |  [optional] |
|**i18n** | [**I18nConfig**](I18nConfig.md) |  |  [optional] |
|**redirects** | [**List&lt;Redirect&gt;**](Redirect.md) | An array of objects (called redirect rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond with a redirect to the specified destination path. |  [optional] |
|**rewrites** | [**List&lt;Rewrite&gt;**](Rewrite.md) | An array of objects (called rewrite rules), where each rule specifies a URL pattern that, if matched to the request URL path, triggers Hosting to respond as if the service were given the specified destination URL. |  [optional] |
|**trailingSlashBehavior** | [**TrailingSlashBehaviorEnum**](#TrailingSlashBehaviorEnum) | Defines how to handle a trailing slash in the URL path. |  [optional] |



## Enum: AppAssociationEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;AUTO&quot; |
| NONE | &quot;NONE&quot; |



## Enum: TrailingSlashBehaviorEnum

| Name | Value |
|---- | -----|
| TRAILING_SLASH_BEHAVIOR_UNSPECIFIED | &quot;TRAILING_SLASH_BEHAVIOR_UNSPECIFIED&quot; |
| ADD | &quot;ADD&quot; |
| REMOVE | &quot;REMOVE&quot; |



