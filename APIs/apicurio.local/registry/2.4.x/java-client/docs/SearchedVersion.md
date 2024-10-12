

# SearchedVersion

Models a single artifact from the result set returned when searching for artifacts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentId** | **Long** |  |  |
|**createdBy** | **String** |  |  |
|**createdOn** | **OffsetDateTime** |  |  |
|**description** | **String** |  |  [optional] |
|**globalId** | **Long** |  |  |
|**labels** | **List&lt;String&gt;** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | User-defined name-value pairs. Name and value must be strings. |  [optional] |
|**references** | [**List&lt;ArtifactReference&gt;**](ArtifactReference.md) |  |  |
|**state** | **ArtifactState** |  |  |
|**type** | **String** |  |  |
|**version** | **String** |  |  |



