

# LKENodePoolRequestBodyAutoscaler

When enabled, the number of nodes autoscales within the defined minimum and maximum values.  When making a request, `max` and `min` require each other. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether autoscaling is enabled for this Node Pool. Defaults to &#x60;false&#x60;. |  [optional] |
|**max** | **Integer** | The maximum number of nodes to autoscale to. Defaults to the Node Pool&#39;s &#x60;count&#x60;. Defaults to the value provided by the &#x60;count&#x60; field.  |  [optional] |
|**min** | **Integer** | The minimum number of nodes to autoscale to. Defaults to the Node Pool&#39;s &#x60;count&#x60;. |  [optional] |



