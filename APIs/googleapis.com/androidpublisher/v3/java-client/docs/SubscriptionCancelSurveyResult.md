

# SubscriptionCancelSurveyResult

Information provided by the user when they complete the subscription cancellation flow (cancellation reason survey).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancelSurveyReason** | **Integer** | The cancellation reason the user chose in the survey. Possible values are: 0. Other 1. I don&#39;t use this service enough 2. Technical issues 3. Cost-related reasons 4. I found a better app |  [optional] |
|**userInputCancelReason** | **String** | The customized input cancel reason from the user. Only present when cancelReason is 0. |  [optional] |



