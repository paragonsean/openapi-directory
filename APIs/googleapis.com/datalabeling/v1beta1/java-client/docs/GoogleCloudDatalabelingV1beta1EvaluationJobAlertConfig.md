

# GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfig

Provides details for how an evaluation job sends email alerts based on the results of a run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Required. An email address to send alerts to. |  [optional] |
|**minAcceptableMeanAveragePrecision** | **Double** | Required. A number between 0 and 1 that describes a minimum mean average precision threshold. When the evaluation job runs, if it calculates that your model version&#39;s predictions from the recent interval have meanAveragePrecision below this threshold, then it sends an alert to your specified email. |  [optional] |



