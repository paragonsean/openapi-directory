

# ImageDetail

A metadata detail record for a specific image. Multiple detail records may map a single catalog image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**dockerfile** | **String** |  |  [optional] |
|**fulldigest** | **String** | Full docker-pullable digest string including the registry url and repository necessary get the image |  [optional] |
|**fulltag** | **String** | Full docker-pullable tag string referencing the image |  [optional] |
|**imageDigest** | **String** | The parent Anchore Image record to which this detail maps |  [optional] |
|**imageId** | **String** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**registry** | **String** |  |  [optional] |
|**repo** | **String** |  |  [optional] |
|**userId** | **String** |  |  [optional] |



