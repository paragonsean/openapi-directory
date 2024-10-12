

# Schema

A [JSON API links object](http://jsonapi.org/format/1.0/#document-links) that points to a schema for the response. If it is a string, or a dictionary containing no `meta` field, the provided URL MUST point at an [OpenAPI](https://swagger.io/specification/) schema. It is possible that future versions of this specification allows for alternative schema types. Hence, if the `meta` field of the JSON API links object is provided and contains a field `schema_type` that is not equal to the string `OpenAPI` the client MUST not handle failures to parse the schema or to validate the response against the schema as errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**href** | **URI** | a string containing the link’s URL. |  |
|**meta** | **Object** | a meta object containing non-standard meta-information about the link. |  [optional] |



