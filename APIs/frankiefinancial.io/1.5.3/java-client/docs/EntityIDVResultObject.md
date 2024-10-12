

# EntityIDVResultObject

Contains the results of a given document entity create/update and IDV token details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicantId** | **String** | The applicantId is either the same one that was supplied in the request for a fresh token, or a new one. This ID must be supplied along with the token to your SDK so that it knows who any uploaded documents are for.  The latest applicant will also be written to the extraData of the entity as well for safe keeping. Older applicantIds will be overwritten.  |  |
|**entity** | [**EntityObject**](EntityObject.md) |  |  |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  |
|**supportTwoDocs** | **Boolean** | If the requesting customer can support requesting 2 documents. |  [optional] |
|**token** | **String** | Token to be used in the SDK to authenticate the applicant and application/referrer.  Tokens are time limited (1 hour) and can only be used with the applicantId supplied.  |  |



