

# GoogleCloudMlV1AutoScaling

Options for automatically scaling a model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxNodes** | **Integer** | The maximum number of nodes to scale this model under load. The actual value will depend on resource quota and availability. |  [optional] |
|**metrics** | [**List&lt;GoogleCloudMlV1MetricSpec&gt;**](GoogleCloudMlV1MetricSpec.md) | MetricSpec contains the specifications to use to calculate the desired nodes count. |  [optional] |
|**minNodes** | **Integer** | Optional. The minimum number of nodes to allocate for this model. These nodes are always up, starting from the time the model is deployed. Therefore, the cost of operating this model will be at least &#x60;rate&#x60; * &#x60;min_nodes&#x60; * number of hours since last billing cycle, where &#x60;rate&#x60; is the cost per node-hour as documented in the [pricing guide](/ml-engine/docs/pricing), even if no predictions are performed. There is additional cost for each prediction performed. Unlike manual scaling, if the load gets too heavy for the nodes that are up, the service will automatically add nodes to handle the increased load as well as scale back as traffic drops, always maintaining at least &#x60;min_nodes&#x60;. You will be charged for the time in which additional nodes are used. If &#x60;min_nodes&#x60; is not specified and AutoScaling is used with a [legacy (MLS1) machine type](/ml-engine/docs/machine-types-online-prediction), &#x60;min_nodes&#x60; defaults to 0, in which case, when traffic to a model stops (and after a cool-down period), nodes will be shut down and no charges will be incurred until traffic to the model resumes. If &#x60;min_nodes&#x60; is not specified and AutoScaling is used with a [Compute Engine (N1) machine type](/ml-engine/docs/machine-types-online-prediction), &#x60;min_nodes&#x60; defaults to 1. &#x60;min_nodes&#x60; must be at least 1 for use with a Compute Engine machine type. You can set &#x60;min_nodes&#x60; when creating the model version, and you can also update &#x60;min_nodes&#x60; for an existing version: update_body.json: { &#39;autoScaling&#39;: { &#39;minNodes&#39;: 5 } } HTTP request: PATCH https://ml.googleapis.com/v1/{name&#x3D;projects/_*_/models/_*_/versions/_*}?update_mask&#x3D;autoScaling.minNodes -d @./update_body.json  |  [optional] |



