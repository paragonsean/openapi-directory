

# OBStatement2

Provides further details on a statement resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner. |  |
|**creationDateTime** | **OffsetDateTime** | Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  |
|**endDateTime** | **OffsetDateTime** | Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  |
|**startDateTime** | **OffsetDateTime** | Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone.An example is below:  2017-04-05T10:43:07+00:00 |  |
|**statementId** | **String** | Unique identifier for the statement resource within an servicing institution. This identifier is both unique and immutable. |  [optional] |
|**statementReference** | **String** | Unique reference for the statement. This reference may be optionally populated if available. |  [optional] |
|**type** | **OBExternalStatementType1Code** |  |  |



