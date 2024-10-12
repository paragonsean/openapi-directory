

# VerifyNotificationChannelRequest

The VerifyNotificationChannel request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Required. The verification code that was delivered to the channel as a result of invoking the SendNotificationChannelVerificationCode API method or that was retrieved from a verified channel via GetNotificationChannelVerificationCode. For example, one might have \&quot;G-123456\&quot; or \&quot;TKNZGhhd2EyN3I1MnRnMjRv\&quot; (in general, one is only guaranteed that the code is valid UTF-8; one should not make any assumptions regarding the structure or format of the code). |  [optional] |



