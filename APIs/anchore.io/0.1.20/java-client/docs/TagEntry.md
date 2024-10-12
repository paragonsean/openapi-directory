

# TagEntry

A docker-pullable tag value as well as deconstructed components

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detectedAt** | **OffsetDateTime** | The timestamp at which the Anchore Engine detected this tag was mapped to the image digest. Does not necessarily indicate when the tag was actually pushed to the registry. |  [optional] |
|**pullstring** | **String** | The pullable string for the tag. E.g. \&quot;docker.io/library/node:latest\&quot; |  [optional] |
|**registry** | **String** | The registry hostname:port section of the pull string |  [optional] |
|**repository** | **String** | The repository section of the pull string |  [optional] |
|**tag** | **String** | The tag-only section of the pull string |  [optional] |



