# ApigeeApi.GoogleCloudApigeeV1AppGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appGroupId** | **String** | Output only. Internal identifier that cannot be edited | [optional] [readonly] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | A list of attributes | [optional] 
**channelId** | **String** | channel identifier identifies the owner maintaing this grouping. | [optional] 
**channelUri** | **String** | A reference to the associated storefront/marketplace. | [optional] 
**createdAt** | **String** | Output only. Created time as milliseconds since epoch. | [optional] [readonly] 
**displayName** | **String** | app group name displayed in the UI | [optional] 
**lastModifiedAt** | **String** | Output only. Modified time as milliseconds since epoch. | [optional] [readonly] 
**name** | **String** | Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._\\-$ %. | [optional] 
**organization** | **String** | Immutable. the org the app group is created | [optional] 
**status** | **String** | Valid values are &#x60;active&#x60; or &#x60;inactive&#x60;. Note that the status of the AppGroup should be updated via UpdateAppGroupRequest by setting the action as &#x60;active&#x60; or &#x60;inactive&#x60;. | [optional] 


