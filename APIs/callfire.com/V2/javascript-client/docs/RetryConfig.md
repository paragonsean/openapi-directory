# CallFireApiDocumentation.RetryConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxAttempts** | **Number** | Maximum number of retry attempts. Default value: 1 | [optional] 
**minutesBetweenAttempts** | **Number** | A number of minutes between retry attempts. Default value: 60 | [optional] 
**retryPhoneTypes** | **[String]** | A list of phone number types to retry. Available values: FIRST_NUMBER, HOME_PHONE, WORK_PHONE, MOBILE_PHONE | [optional] 
**retryResults** | **[String]** | List of result states when a call/text should be addressed to this contact again. Supports any combination of result statuses. Available values: LA, BUSY, AM, NO_ANS, SENT, RECEIVED, etc. See [call/text states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] 


