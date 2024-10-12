

# AccessCredential

A login credential mapped to a user identity. For password credentials, the username to present for Basic auth is the user's username from the user record

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | The timestamp of creation of the credential |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of credential |  |
|**value** | **String** | The credential value (e.g. the password) |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PASSWORD | &quot;password&quot; |



