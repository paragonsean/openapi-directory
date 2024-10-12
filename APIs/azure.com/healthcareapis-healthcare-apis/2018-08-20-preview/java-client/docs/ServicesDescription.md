

# ServicesDescription

The description of the service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**ServicesProperties**](ServicesProperties.md) |  |  [optional] |
|**etag** | **String** | An etag associated with the resource, used for optimistic concurrency when editing it. |  [optional] |
|**id** | **String** | The resource identifier. |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | The kind of the service. Valid values are: fhir, fhir-Stu3 and fhir-R4. |  |
|**location** | **String** | The resource location. |  |
|**name** | **String** | The resource name. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | The resource tags. |  [optional] |
|**type** | **String** | The resource type. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| FHIR | &quot;fhir&quot; |
| FHIR_STU3 | &quot;fhir-Stu3&quot; |
| FHIR_R4 | &quot;fhir-R4&quot; |



