

# MonitorContactRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | **String** | The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of the instance. |  |
|**contactId** | **String** | The identifier of the contact. |  |
|**userId** | **String** | The identifier of the user account. |  |
|**allowedMonitorCapabilities** | **List&lt;MonitorCapability&gt;** | Specify which monitoring actions the user is allowed to take. For example, whether the user is allowed to escalate from silent monitoring to barge. |  [optional] |
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. |  [optional] |



