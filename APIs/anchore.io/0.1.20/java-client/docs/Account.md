

# Account

Account information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The timestamp when the account was created |  [optional] |
|**email** | **String** | Optional email address associated with the account |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The timestamp of the last update to the account metadata itself (not users or creds) |  [optional] |
|**name** | **String** | The account identifier, not updatable after creation |  |
|**state** | [**StateEnum**](#StateEnum) | State of the account. Disabled accounts prevent member users from logging in, deleting accounts are disabled and pending deletion and will be removed once all owned resources are garbage collected by the system |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The user type (admin vs user). If not specified in a POST request, &#39;user&#39; is default |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |
| DELETING | &quot;deleting&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| ADMIN | &quot;admin&quot; |
| SERVICE | &quot;service&quot; |



