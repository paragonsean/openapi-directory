# DialogflowApi.GoogleCloudDialogflowV2SmartReplyMetricsTopNMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n** | **Number** | Number of retrieved smart replies. For example, when &#x60;n&#x60; is 3, this evaluation contains metrics for when Dialogflow retrieves 3 smart replies with the model. | [optional] 
**recall** | **Number** | Defined as &#x60;number of queries whose top n smart replies have at least one similar (token match similarity above the defined threshold) reply as the real reply&#x60; divided by &#x60;number of queries with at least one smart reply&#x60;. Value ranges from 0.0 to 1.0 inclusive. | [optional] 


