

# GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigYumRepositoryPublicRepository

Publicly available Yum repositories constructed from a common repository base and a custom repository path.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**repositoryBase** | [**RepositoryBaseEnum**](#RepositoryBaseEnum) | A common public repository base for Yum. |  [optional] |
|**repositoryPath** | **String** | A custom field to define a path to a specific repository from the base. |  [optional] |



## Enum: RepositoryBaseEnum

| Name | Value |
|---- | -----|
| REPOSITORY_BASE_UNSPECIFIED | &quot;REPOSITORY_BASE_UNSPECIFIED&quot; |
| CENTOS | &quot;CENTOS&quot; |
| CENTOS_DEBUG | &quot;CENTOS_DEBUG&quot; |
| CENTOS_VAULT | &quot;CENTOS_VAULT&quot; |
| CENTOS_STREAM | &quot;CENTOS_STREAM&quot; |
| ROCKY | &quot;ROCKY&quot; |
| EPEL | &quot;EPEL&quot; |



