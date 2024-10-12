

# ServerConfig

Kubernetes Engine service configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channels** | [**List&lt;ReleaseChannelConfig&gt;**](ReleaseChannelConfig.md) | List of release channel configurations. |  [optional] |
|**defaultClusterVersion** | **String** | Version of Kubernetes the service deploys by default. |  [optional] |
|**defaultImageType** | **String** | Default image type. |  [optional] |
|**validImageTypes** | **List&lt;String&gt;** | List of valid image types. |  [optional] |
|**validMasterVersions** | **List&lt;String&gt;** | List of valid master versions, in descending order. |  [optional] |
|**validNodeVersions** | **List&lt;String&gt;** | List of valid node upgrade target versions, in descending order. |  [optional] |



