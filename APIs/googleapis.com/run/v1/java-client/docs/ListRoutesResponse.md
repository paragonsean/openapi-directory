

# ListRoutesResponse

ListRoutesResponse is a list of Route resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;serving.knative.dev/v1\&quot;. |  [optional] |
|**items** | [**List&lt;Route&gt;**](Route.md) | List of Routes. |  [optional] |
|**kind** | **String** | The kind of this resource, in this case always \&quot;RouteList\&quot;. |  [optional] |
|**metadata** | [**ListMeta**](ListMeta.md) |  |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



