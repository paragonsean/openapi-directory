

# OptimadeError

detail MUST be present

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | an application-specific error code, expressed as a string value. |  [optional] |
|**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. |  |
|**id** | **String** | A unique identifier for this particular occurrence of the problem. |  [optional] |
|**links** | [**ErrorLinks**](ErrorLinks.md) | A links object storing about |  [optional] |
|**meta** | **Object** | a meta object containing non-standard meta-information about the error. |  [optional] |
|**source** | [**ErrorSource**](ErrorSource.md) | An object containing references to the source of the error |  [optional] |
|**status** | **String** | the HTTP status code applicable to this problem, expressed as a string value. |  [optional] |
|**title** | **String** | A short, human-readable summary of the problem. It **SHOULD NOT** change from occurrence to occurrence of the problem, except for purposes of localization. |  [optional] |



