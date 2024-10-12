# VertexAiApi.GoogleCloudAiplatformV1beta1AutoscalingMetricSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricName** | **String** | Required. The resource metric name. Supported metrics: * For Online Prediction: * &#x60;aiplatform.googleapis.com/prediction/online/accelerator/duty_cycle&#x60; * &#x60;aiplatform.googleapis.com/prediction/online/cpu/utilization&#x60; | [optional] 
**target** | **Number** | The target resource utilization in percentage (1% - 100%) for the given metric; once the real usage deviates from the target by a certain percentage, the machine replicas change. The default value is 60 (representing 60%) if not provided. | [optional] 


