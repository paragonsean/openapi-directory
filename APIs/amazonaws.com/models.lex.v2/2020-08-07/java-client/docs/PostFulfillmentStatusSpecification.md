

# PostFulfillmentStatusSpecification

Provides a setting that determines whether the post-fulfillment response is sent to the user. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete\">https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete</a> 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**successResponse** | [**ResponseSpecification**](ResponseSpecification.md) |  |  [optional] |
|**failureResponse** | [**ResponseSpecification**](ResponseSpecification.md) |  |  [optional] |
|**timeoutResponse** | [**ResponseSpecification**](ResponseSpecification.md) |  |  [optional] |
|**successNextStep** | [**PostFulfillmentStatusSpecificationSuccessNextStep**](PostFulfillmentStatusSpecificationSuccessNextStep.md) |  |  [optional] |
|**successConditional** | [**PostFulfillmentStatusSpecificationSuccessConditional**](PostFulfillmentStatusSpecificationSuccessConditional.md) |  |  [optional] |
|**failureNextStep** | [**PostFulfillmentStatusSpecificationFailureNextStep**](PostFulfillmentStatusSpecificationFailureNextStep.md) |  |  [optional] |
|**failureConditional** | [**PostFulfillmentStatusSpecificationFailureConditional**](PostFulfillmentStatusSpecificationFailureConditional.md) |  |  [optional] |
|**timeoutNextStep** | [**PostFulfillmentStatusSpecificationTimeoutNextStep**](PostFulfillmentStatusSpecificationTimeoutNextStep.md) |  |  [optional] |
|**timeoutConditional** | [**PostFulfillmentStatusSpecificationTimeoutConditional**](PostFulfillmentStatusSpecificationTimeoutConditional.md) |  |  [optional] |



