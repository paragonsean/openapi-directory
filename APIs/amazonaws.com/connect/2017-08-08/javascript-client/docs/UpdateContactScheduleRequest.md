# AmazonConnectService.UpdateContactScheduleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceId** | **String** | The identifier of the Amazon Connect instance. You can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\&quot;&gt;find the instance ID&lt;/a&gt; in the Amazon Resource Name (ARN) of the instance. | 
**contactId** | **String** | The identifier of the contact. | 
**scheduledTime** | **Date** | The timestamp, in Unix Epoch seconds format, at which to start running the inbound flow. The scheduled time cannot be in the past. It must be within up to 6 days in future.  | 


