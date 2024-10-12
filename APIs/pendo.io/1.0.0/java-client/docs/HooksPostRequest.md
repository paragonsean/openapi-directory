

# HooksPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**event** | **String** | The event field can contain one of the following values- 1) &#39;feature_created&#39; - When a new feature is created a webhook will be triggered with the details of the feature. Feature details can be found in the model section under Feature object 2) &#39;feature_status_changed&#39; - When a feature status is updated a webhook will be triggered with the updated Feature details. Feature details can be found in the model section under Feature object. 3) &#39;feature_comment_created&#39; - When a commment is created on a feature, a webhook will be triggered with the details about the Feature and the new comment. Feature and Comment details can be found in the model section under Feature object and Comment object. |  [optional] |
|**targetUrl** | **String** | The target URL where the events will be sent to. |  [optional] |



