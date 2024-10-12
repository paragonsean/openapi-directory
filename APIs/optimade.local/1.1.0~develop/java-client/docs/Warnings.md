

# Warnings

OPTIMADE-specific warning class based on OPTIMADE-specific JSON API Error.  From the specification:  A warning resource object is defined similarly to a JSON API error object, but MUST also include the field type, which MUST have the value \"warning\". The field detail MUST be present and SHOULD contain a non-critical message, e.g., reporting unrecognized search attributes or deprecated features.  Note: Must be named \"Warnings\", since \"Warning\" is a built-in Python class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | an application-specific error code, expressed as a string value. |  [optional] |
|**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. |  |
|**id** | **String** | A unique identifier for this particular occurrence of the problem. |  [optional] |
|**links** | [**ErrorLinks**](ErrorLinks.md) | A links object storing about |  [optional] |
|**meta** | **Object** | a meta object containing non-standard meta-information about the error. |  [optional] |
|**source** | [**ErrorSource**](ErrorSource.md) | An object containing references to the source of the error |  [optional] |
|**title** | **String** | A short, human-readable summary of the problem. It **SHOULD NOT** change from occurrence to occurrence of the problem, except for purposes of localization. |  [optional] |
|**type** | **String** | Warnings must be of type \&quot;warning\&quot; |  |



