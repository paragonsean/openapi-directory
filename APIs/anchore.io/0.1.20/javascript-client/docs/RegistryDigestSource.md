# AnchoreEngineApiServer.RegistryDigestSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTimestampOverride** | **Date** | Optional override of the image creation time to support proper tag history construction in cases of out-of-order analysis compared to registry history for the tag | [optional] 
**dockerfile** | **String** | Base64 encoded content of the dockerfile used to build the image, if available. | [optional] 
**pullstring** | **String** | A digest-based pullstring (e.g. docker.io/nginx@sha256:123abc) | 
**tag** | **String** | A valid docker tag reference (e.g. docker.io/nginx:latest) that will be associated with the image but not used to pull the image. | 


