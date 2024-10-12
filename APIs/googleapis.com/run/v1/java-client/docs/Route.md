

# Route

Route is responsible for configuring ingress over a collection of Revisions. Some of the Revisions a Route distributes traffic over may be specified by referencing the Configuration responsible for creating them; in these cases the Route is additionally responsible for monitoring the Configuration for \"latest ready\" revision changes, and smoothly rolling out latest revisions. Cloud Run currently supports referencing a single Configuration to automatically deploy the \"latest ready\" Revision from that Configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | The API version for this call such as \&quot;serving.knative.dev/v1\&quot;. |  [optional] |
|**kind** | **String** | The kind of this resource, in this case always \&quot;Route\&quot;. |  [optional] |
|**metadata** | [**ObjectMeta**](ObjectMeta.md) |  |  [optional] |
|**spec** | [**RouteSpec**](RouteSpec.md) |  |  [optional] |
|**status** | [**RouteStatus**](RouteStatus.md) |  |  [optional] |



