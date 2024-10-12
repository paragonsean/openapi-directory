

# CheckRequest

Request message for the Check method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**AttributeContext**](AttributeContext.md) |  |  [optional] |
|**flags** | **String** | Optional. Contains a comma-separated list of flags. |  [optional] |
|**resources** | [**List&lt;ResourceInfo&gt;**](ResourceInfo.md) | Describes the resources and the policies applied to each resource. |  [optional] |
|**serviceConfigId** | **String** | Specifies the version of the service configuration that should be used to process the request. Must not be empty. Set this field to &#39;latest&#39; to specify using the latest configuration. |  [optional] |



