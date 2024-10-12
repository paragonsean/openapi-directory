

# OperationMetadataV1

Metadata describing an Operation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildId** | **String** | The Cloud Build ID of the function created or updated by an API call. This field is only populated for Create and Update operations. |  [optional] |
|**buildName** | **String** | The Cloud Build Name of the function deployment. This field is only populated for Create and Update operations. &#x60;projects//locations//builds/&#x60;. |  [optional] |
|**request** | **Map&lt;String, Object&gt;** | The original request that started the operation. |  [optional] |
|**sourceToken** | **String** | An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments. |  [optional] |
|**target** | **String** | Target of the operation - for example &#x60;projects/project-1/locations/region-1/functions/function-1&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of operation. |  [optional] |
|**updateTime** | **String** | The last update timestamp of the operation. |  [optional] |
|**versionId** | **String** | Version id of the function created or updated by an API call. This field is only populated for Create and Update operations. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OPERATION_UNSPECIFIED | &quot;OPERATION_UNSPECIFIED&quot; |
| CREATE_FUNCTION | &quot;CREATE_FUNCTION&quot; |
| UPDATE_FUNCTION | &quot;UPDATE_FUNCTION&quot; |
| DELETE_FUNCTION | &quot;DELETE_FUNCTION&quot; |



