

# ReportRequest

Request message for the Report method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operations** | [**List&lt;AttributeContext&gt;**](AttributeContext.md) | Describes the list of operations to be reported. Each operation is represented as an AttributeContext, and contains all attributes around an API access. |  [optional] |
|**serviceConfigId** | **String** | Specifies the version of the service configuration that should be used to process the request. Must not be empty. Set this field to &#39;latest&#39; to specify using the latest configuration. |  [optional] |



