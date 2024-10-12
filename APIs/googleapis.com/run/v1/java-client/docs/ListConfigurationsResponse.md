

# ListConfigurationsResponse

ListConfigurationsResponse is a list of Configuration resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;serving.knative.dev/v1\&quot;. |  [optional] |
|**items** | [**List&lt;ModelConfiguration&gt;**](ModelConfiguration.md) | List of Configurations. |  [optional] |
|**kind** | **String** | The kind of this resource, in this case \&quot;ConfigurationList\&quot;. |  [optional] |
|**metadata** | [**ListMeta**](ListMeta.md) |  |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



