

# ApiManagementServiceNameAvailabilityResult

Response of the CheckNameAvailability operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | If reason &#x3D;&#x3D; invalid, provide the user with the reason why the given name is invalid, and provide the resource naming requirements so that the user can select a valid name. If reason &#x3D;&#x3D; AlreadyExists, explain that &lt;resourceName&gt; is already in use, and direct them to select a different name. |  [optional] |
|**nameAvailable** | **Boolean** | True if the name is available and can be used to create a new API Management service; otherwise false. |  |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Invalid indicates the name provided does not match the resource provider’s naming requirements (incorrect length, unsupported characters, etc.)  AlreadyExists indicates that the name is already in use and is therefore unavailable. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| VALID | &quot;Valid&quot; |
| INVALID | &quot;Invalid&quot; |
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |



