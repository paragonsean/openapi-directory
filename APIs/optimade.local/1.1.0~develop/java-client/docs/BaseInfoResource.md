

# BaseInfoResource

Resource objects appear in a JSON API document to represent resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**BaseInfoAttributes**](BaseInfoAttributes.md) |  |  |
|**id** | **String** |  |  |
|**links** | [**ResourceLinks**](ResourceLinks.md) | a links object containing links related to the resource. |  [optional] |
|**meta** | **Object** | a meta object containing non-standard meta-information about a resource that can not be represented as an attribute or relationship. |  [optional] |
|**relationships** | **Object** | [Relationships object](https://jsonapi.org/format/1.0/#document-resource-object-relationships) describing relationships between the resource and other JSON API resources. |  [optional] |
|**type** | **String** |  |  |



