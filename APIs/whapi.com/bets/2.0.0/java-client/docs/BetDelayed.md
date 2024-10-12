

# BetDelayed


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delayPeriodSeconds** | **Integer** | The delay time period of the bet in seconds. The resubmission of the bet has to wait for the length of time (in seconds) returned in the delayPeriod before submitting the second request. |  |
|**delayedBetId** | **String** | The unique identifier of the delayed bet. After the initial response is received, containing the delayPeriod and the delayBetId, the request is then resubmitted using the same delayBetId token that came in that initial response. Check the example below to see how to resend a delayed bet payload. |  |
|**id** | **String** | The number of the bet |  |
|**number** | **BigDecimal** | Number of the bet if this is part of a multiple bet |  [optional] |



