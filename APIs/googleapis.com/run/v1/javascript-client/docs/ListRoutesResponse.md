# CloudRunAdminApi.ListRoutesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersion** | **String** | The API version for this call such as \&quot;serving.knative.dev/v1\&quot;. | [optional] 
**items** | [**[Route]**](Route.md) | List of Routes. | [optional] 
**kind** | **String** | The kind of this resource, in this case always \&quot;RouteList\&quot;. | [optional] 
**metadata** | [**ListMeta**](ListMeta.md) |  | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


