

# AccountResourceRequest

The body of a PUT request to modify a Visual Studio account resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** | The account name. |  [optional] |
|**location** | **String** | The Azure instance location. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The type of the operation. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | The custom properties of the resource. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The custom tags of the resource. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| CREATE | &quot;create&quot; |
| UPDATE | &quot;update&quot; |
| LINK | &quot;link&quot; |



