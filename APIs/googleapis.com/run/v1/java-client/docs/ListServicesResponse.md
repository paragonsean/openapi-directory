

# ListServicesResponse

A list of Service resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call; returns \&quot;serving.knative.dev/v1\&quot;. |  [optional] |
|**items** | [**List&lt;Service&gt;**](Service.md) | List of Services. |  [optional] |
|**kind** | **String** | The kind of this resource; returns \&quot;ServiceList\&quot;. |  [optional] |
|**metadata** | [**ListMeta**](ListMeta.md) |  |  [optional] |
|**unreachable** | **List&lt;String&gt;** | For calls against the global endpoint, returns the list of Cloud locations that could not be reached. For regional calls, this field is not used. |  [optional] |



