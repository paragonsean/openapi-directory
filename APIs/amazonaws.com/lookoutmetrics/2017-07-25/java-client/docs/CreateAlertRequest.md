

# CreateAlertRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertName** | **String** | The name of the alert. |  |
|**alertSensitivityThreshold** | **Integer** | An integer from 0 to 100 specifying the alert sensitivity threshold. |  [optional] |
|**alertDescription** | **String** | A description of the alert. |  [optional] |
|**anomalyDetectorArn** | **String** | The ARN of the detector to which the alert is attached. |  |
|**action** | [**CreateAlertRequestAction**](CreateAlertRequestAction.md) |  |  |
|**tags** | **Map&lt;String, String&gt;** | A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lookoutmetrics/latest/dev/detectors-tags.html\&quot;&gt;tags&lt;/a&gt; to apply to the alert. |  [optional] |
|**alertFilters** | [**CreateAlertRequestAlertFilters**](CreateAlertRequestAlertFilters.md) |  |  [optional] |



