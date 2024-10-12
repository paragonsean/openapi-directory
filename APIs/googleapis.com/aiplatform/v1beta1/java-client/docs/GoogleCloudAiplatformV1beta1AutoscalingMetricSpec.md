

# GoogleCloudAiplatformV1beta1AutoscalingMetricSpec

The metric specification that defines the target resource utilization (CPU utilization, accelerator's duty cycle, and so on) for calculating the desired replica count.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricName** | **String** | Required. The resource metric name. Supported metrics: * For Online Prediction: * &#x60;aiplatform.googleapis.com/prediction/online/accelerator/duty_cycle&#x60; * &#x60;aiplatform.googleapis.com/prediction/online/cpu/utilization&#x60; |  [optional] |
|**target** | **Integer** | The target resource utilization in percentage (1% - 100%) for the given metric; once the real usage deviates from the target by a certain percentage, the machine replicas change. The default value is 60 (representing 60%) if not provided. |  [optional] |



