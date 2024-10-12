

# RetryConfig

Retry configuration will help you to resend a call or text if it was not delivered first time

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxAttempts** | **Integer** | Maximum number of retry attempts. Default value: 1 |  [optional] |
|**minutesBetweenAttempts** | **Integer** | A number of minutes between retry attempts. Default value: 60 |  [optional] |
|**retryPhoneTypes** | **List&lt;String&gt;** | A list of phone number types to retry. Available values: FIRST_NUMBER, HOME_PHONE, WORK_PHONE, MOBILE_PHONE |  [optional] |
|**retryResults** | **List&lt;String&gt;** | List of result states when a call/text should be addressed to this contact again. Supports any combination of result statuses. Available values: LA, BUSY, AM, NO_ANS, SENT, RECEIVED, etc. See [call/text states and results](https://developers.callfire.com/results-responses-errors.html) |  [optional] |



