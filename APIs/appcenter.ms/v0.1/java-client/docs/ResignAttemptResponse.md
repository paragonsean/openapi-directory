

# ResignAttemptResponse

URL that can be used to check the status of the update devices operation and the updated profiles.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | App ID that the resign operation is being performed against. |  |
|**contextId** | **String** | Context ID for the resigning operation. |  |
|**destinations** | **List&lt;Object&gt;** | List of destinations that the resign operation is being performed against. |  [optional] |
|**errorCode** | **String** | Error code associated with the exception. |  [optional] |
|**errorMessage** | **String** | Error message associated with the exception. |  [optional] |
|**originalReleaseId** | **BigDecimal** | ID of the release which is being resigned. |  |
|**resignId** | **String** | ID of the resign operation. |  |
|**startTime** | **BigDecimal** | The time that the resign operation was started. |  |
|**status** | **String** | The status of the resigning operation. |  |
|**userId** | **String** | ID of the user performing the resign operaiton. |  |



