

# Response

If Result is Success, ErrorCondition is absent or not used in the processing of the message. In the other cases, the ErrorCondition has to be present and can refine the processing of the message response. AdditionalResponse gives more information about the success or the failure of the message request processing, for logging without real time involvements. Result of a message request processing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalResponse** | **String** | If present, the POI logs it for further examination. |  [optional] |
|**errorCondition** | **ErrorCondition** |  |  [optional] |
|**result** | **Result** |  |  |



