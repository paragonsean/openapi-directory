# ApiClient.ResourceNameAvailability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | If reason &#x3D;&#x3D; invalid, provide the user with the reason why the given name is invalid, and provide the resource naming requirements so that the user can select a valid name. If reason &#x3D;&#x3D; AlreadyExists, explain that resource name is already in use, and direct them to select a different name. | [optional] 
**nameAvailable** | **Boolean** | &lt;code&gt;true&lt;/code&gt; indicates name is valid and available. &lt;code&gt;false&lt;/code&gt; indicates the name is invalid, unavailable, or both. | [optional] 
**reason** | **String** | &lt;code&gt;Invalid&lt;/code&gt; indicates the name provided does not match Azure App Service naming requirements. &lt;code&gt;AlreadyExists&lt;/code&gt; indicates that the name is already in use and is therefore unavailable. | [optional] 



## Enum: ReasonEnum


* `Invalid` (value: `"Invalid"`)

* `AlreadyExists` (value: `"AlreadyExists"`)




