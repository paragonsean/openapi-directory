

# HttpUpdate

A file you can add to your existing, non-Hosting hosting service that confirms your intent to allow Hosting's Certificate Authorities to create an SSL certificate for your domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkError** | [**Status**](Status.md) |  |  [optional] |
|**desired** | **String** | Output only. A text string to serve at the path. |  [optional] [readonly] |
|**discovered** | **String** | Output only. Whether Hosting was able to find the required file contents on the specified path during its last check. |  [optional] [readonly] |
|**lastCheckTime** | **String** | Output only. The last time Hosting systems checked for the file contents. |  [optional] [readonly] |
|**path** | **String** | Output only. The path to the file. |  [optional] [readonly] |



