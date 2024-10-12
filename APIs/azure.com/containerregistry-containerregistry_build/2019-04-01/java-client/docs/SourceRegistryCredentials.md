

# SourceRegistryCredentials

Describes the credential parameters for accessing the source registry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loginMode** | [**LoginModeEnum**](#LoginModeEnum) | The authentication mode which determines the source registry login scope. The credentials for the source registry  will be generated using the given scope. These credentials will be used to login to  the source registry during the run. |  [optional] |



## Enum: LoginModeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| DEFAULT | &quot;Default&quot; |



