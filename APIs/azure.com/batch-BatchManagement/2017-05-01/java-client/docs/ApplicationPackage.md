

# ApplicationPackage

An application package which represents a particular version of an application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | **String** | The format of the application package, if the package is active. |  [optional] [readonly] |
|**id** | **String** | The ID of the application. |  [optional] [readonly] |
|**lastActivationTime** | **OffsetDateTime** | The time at which the package was last activated, if the package is active. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the application package. |  [optional] [readonly] |
|**storageUrl** | **String** | The URL for the application package in Azure Storage. |  [optional] [readonly] |
|**storageUrlExpiry** | **OffsetDateTime** | The UTC time at which the Azure Storage URL will expire. |  [optional] [readonly] |
|**version** | **String** | The version of the application package.  |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACTIVE | &quot;active&quot; |
| UNMAPPED | &quot;unmapped&quot; |



