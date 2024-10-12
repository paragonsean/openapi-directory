

# ServiceSpec

ServiceSpec holds the desired state of the Route (from the client), which is used to manipulate the underlying Route and Configuration(s).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**template** | [**RevisionTemplate**](RevisionTemplate.md) |  |  [optional] |
|**traffic** | [**List&lt;TrafficTarget&gt;**](TrafficTarget.md) | Specifies how to distribute traffic over a collection of Knative Revisions and Configurations to the Service&#39;s main URL. |  [optional] |



