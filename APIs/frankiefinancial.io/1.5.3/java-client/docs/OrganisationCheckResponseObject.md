

# OrganisationCheckResponseObject

The result of an /business/ownership/query call retrieved via GET /retrieve/response/{requestId} after you receive a notification that the result is ready. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**flags** | [**List&lt;EntityFlagObject&gt;**](EntityFlagObject.md) | Used to set additional information flags for this response.  |  [optional] |
|**organisationCheckId** | **UUID** | Batch identifier for the KYC/AML check results if any.  |  [optional] |
|**organisationCheckResult** | [**OrganisationCheckResultObject**](OrganisationCheckResultObject.md) |  |  [optional] |
|**ownershipCheckDate** | **OffsetDateTime** | If an ownership result is provided in this response then this is the date and time the service provided that result.  |  [optional] |
|**ownershipCheckId** | **UUID** | Unique identifier for the ownership check.  |  [optional] |
|**ownershipQueryError** | [**ErrorObject**](ErrorObject.md) |  |  [optional] |
|**ownershipQueryResult** | [**OwnershipQueryResultObject**](OwnershipQueryResultObject.md) |  |  [optional] |
|**reportError** | [**ErrorObject**](ErrorObject.md) |  |  [optional] |
|**reportResult** | [**BusinessReportResultObject**](BusinessReportResultObject.md) |  |  [optional] |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  [optional] |
|**uboResponse** | [**UBOResponse**](UBOResponse.md) |  |  [optional] |



