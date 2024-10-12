# AmazonLookoutForMetrics.CreateAnomalyDetectorRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomalyDetectorName** | **String** | The name of the detector. | 
**anomalyDetectorDescription** | **String** | A description of the detector. | [optional] 
**anomalyDetectorConfig** | [**CreateAnomalyDetectorRequestAnomalyDetectorConfig**](CreateAnomalyDetectorRequestAnomalyDetectorConfig.md) |  | 
**kmsKeyArn** | **String** | The ARN of the KMS key to use to encrypt your data. | [optional] 
**tags** | **{String: String}** | A list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lookoutmetrics/latest/dev/detectors-tags.html\&quot;&gt;tags&lt;/a&gt; to apply to the anomaly detector. | [optional] 


