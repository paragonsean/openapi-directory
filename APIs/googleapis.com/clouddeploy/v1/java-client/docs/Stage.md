

# Stage

Stage specifies a location to which to deploy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployParameters** | [**List&lt;DeployParameters&gt;**](DeployParameters.md) | Optional. The deploy parameters to use for the target in this stage. |  [optional] |
|**profiles** | **List&lt;String&gt;** | Skaffold profiles to use when rendering the manifest for this stage&#39;s &#x60;Target&#x60;. |  [optional] |
|**strategy** | [**Strategy**](Strategy.md) |  |  [optional] |
|**targetId** | **String** | The target_id to which this stage points. This field refers exclusively to the last segment of a target name. For example, this field would just be &#x60;my-target&#x60; (rather than &#x60;projects/project/locations/location/targets/my-target&#x60;). The location of the &#x60;Target&#x60; is inferred to be the same as the location of the &#x60;DeliveryPipeline&#x60; that contains this &#x60;Stage&#x60;. |  [optional] |



