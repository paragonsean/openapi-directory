# AmazonLookoutForMetrics.ListAnomalyGroupRelatedMetricsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomalyDetectorArn** | **String** | The Amazon Resource Name (ARN) of the anomaly detector. | 
**anomalyGroupId** | **String** | The ID of the anomaly group. | 
**relationshipTypeFilter** | **String** | Filter for potential causes (&lt;code&gt;CAUSE_OF_INPUT_ANOMALY_GROUP&lt;/code&gt;) or downstream effects (&lt;code&gt;EFFECT_OF_INPUT_ANOMALY_GROUP&lt;/code&gt;) of the anomaly group. | [optional] 
**maxResults** | **Number** | The maximum number of results to return. | [optional] 
**nextToken** | **String** | Specify the pagination token that&#39;s returned by a previous request to retrieve the next page of results. | [optional] 



## Enum: RelationshipTypeFilterEnum


* `CAUSE_OF_INPUT_ANOMALY_GROUP` (value: `"CAUSE_OF_INPUT_ANOMALY_GROUP"`)

* `EFFECT_OF_INPUT_ANOMALY_GROUP` (value: `"EFFECT_OF_INPUT_ANOMALY_GROUP"`)




