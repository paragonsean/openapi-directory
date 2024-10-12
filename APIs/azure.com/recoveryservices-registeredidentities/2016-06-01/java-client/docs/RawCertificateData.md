

# RawCertificateData

Raw certificate data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | Specifies the authentication type. |  [optional] |
|**certificate** | **byte[]** | The base64 encoded certificate raw data string |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| ACS | &quot;ACS&quot; |
| AAD | &quot;AAD&quot; |
| ACCESS_CONTROL_SERVICE | &quot;AccessControlService&quot; |
| AZURE_ACTIVE_DIRECTORY | &quot;AzureActiveDirectory&quot; |



