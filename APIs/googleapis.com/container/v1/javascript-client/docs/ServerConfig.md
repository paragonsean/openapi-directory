# KubernetesEngineApi.ServerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**[ReleaseChannelConfig]**](ReleaseChannelConfig.md) | List of release channel configurations. | [optional] 
**defaultClusterVersion** | **String** | Version of Kubernetes the service deploys by default. | [optional] 
**defaultImageType** | **String** | Default image type. | [optional] 
**validImageTypes** | **[String]** | List of valid image types. | [optional] 
**validMasterVersions** | **[String]** | List of valid master versions, in descending order. | [optional] 
**validNodeVersions** | **[String]** | List of valid node upgrade target versions, in descending order. | [optional] 


