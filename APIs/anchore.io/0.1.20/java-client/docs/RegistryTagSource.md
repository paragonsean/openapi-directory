

# RegistryTagSource

An image reference using a tag in a registry, this is the most common source type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dockerfile** | **String** | Base64 encoded content of the dockerfile used to build the image, if available. |  [optional] |
|**pullstring** | **String** | A docker pull string (e.g. docker.io/nginx:latest, or docker.io/nginx@sha256:abd) to retrieve the image |  |



