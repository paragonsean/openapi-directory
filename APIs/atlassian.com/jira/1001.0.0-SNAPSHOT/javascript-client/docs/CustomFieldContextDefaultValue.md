# TheJiraCloudPlatformRestApi.CustomFieldContextDefaultValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cascadingOptionId** | **String** | The ID of the default cascading option. | [optional] 
**contextId** | **String** | The ID of the context. | 
**optionId** | **String** | The ID of the default option. | 
**type** | **String** |  | 
**optionIds** | **[String]** | The list of IDs of the default options. | 
**accountId** | **String** | The ID of the default user. | 
**userFilter** | [**UserFilter**](UserFilter.md) |  | 
**accountIds** | **[String]** | The IDs of the default users. | 
**groupId** | **String** | The ID of the the default group. | 
**groupIds** | **[String]** | The IDs of the default groups. | 
**date** | **String** | The default date in ISO format. Ignored if &#x60;useCurrent&#x60; is true. | [optional] 
**useCurrent** | **Boolean** | Whether to use the current date. | [optional] [default to false]
**dateTime** | **String** | The default date-time in ISO format. Ignored if &#x60;useCurrent&#x60; is true. | [optional] 
**url** | **String** | The default URL. | 
**projectId** | **String** | The ID of the default project. | 
**number** | **Number** | The default floating-point number. | 
**labels** | **[String]** | The default labels value. | 
**text** | **String** | The default text. The maximum length is 254 characters. | [optional] 
**versionId** | **String** | The ID of the default version. | 
**versionOrder** | **String** | The order the pickable versions are displayed in. If not provided, the released-first order is used. Available version orders are &#x60;\&quot;releasedFirst\&quot;&#x60; and &#x60;\&quot;unreleasedFirst\&quot;&#x60;. | [optional] 
**versionIds** | **[String]** | The IDs of the default versions. | 
**values** | **[String]** | List of string values. The maximum length for a value is 254 characters. | [optional] 
**object** | **Object** | The default JSON object. | [optional] 


