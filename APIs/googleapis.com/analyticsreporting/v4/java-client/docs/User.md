

# User

Contains information to identify a particular user uniquely.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Type of the user in the request. The field &#x60;userId&#x60; is associated with this type. |  [optional] |
|**userId** | **String** | Unique Id of the user for which the data is being requested. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER_ID_TYPE_UNSPECIFIED | &quot;USER_ID_TYPE_UNSPECIFIED&quot; |
| USER_ID | &quot;USER_ID&quot; |
| CLIENT_ID | &quot;CLIENT_ID&quot; |



