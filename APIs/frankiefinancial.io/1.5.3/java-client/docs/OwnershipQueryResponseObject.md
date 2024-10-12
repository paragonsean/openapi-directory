

# OwnershipQueryResponseObject

Frankie internal use only.  The result of an /business/ownership/query call as returned by a suitable service connector. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkDate** | **OffsetDateTime** | If a result is provided in this response then this is the date and time the service provided that result.  |  [optional] |
|**checkId** | **UUID** |  |  [optional] |
|**ownershipQueryResult** | [**OwnershipQueryResultObject**](OwnershipQueryResultObject.md) |  |  [optional] |
|**providerCheckId** | **String** | Unique identifier provided by the service.  |  [optional] |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  [optional] |



