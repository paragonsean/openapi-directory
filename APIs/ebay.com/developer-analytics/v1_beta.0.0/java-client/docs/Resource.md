

# Resource

This complex type defines the resource (API method) and the current rate-limit data for that resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the resource (an API or an API method) to which the rate-limit data applies. |  [optional] |
|**rates** | [**List&lt;Rate&gt;**](Rate.md) | A list of rate-limit data, where each list element represents the rate-limit data for a specific resource. |  [optional] |



