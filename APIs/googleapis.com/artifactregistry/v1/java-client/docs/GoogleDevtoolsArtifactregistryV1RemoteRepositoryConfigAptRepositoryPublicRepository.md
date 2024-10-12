

# GoogleDevtoolsArtifactregistryV1RemoteRepositoryConfigAptRepositoryPublicRepository

Publicly available Apt repositories constructed from a common repository base and a custom repository path.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**repositoryBase** | [**RepositoryBaseEnum**](#RepositoryBaseEnum) | A common public repository base for Apt. |  [optional] |
|**repositoryPath** | **String** | A custom field to define a path to a specific repository from the base. |  [optional] |



## Enum: RepositoryBaseEnum

| Name | Value |
|---- | -----|
| REPOSITORY_BASE_UNSPECIFIED | &quot;REPOSITORY_BASE_UNSPECIFIED&quot; |
| DEBIAN | &quot;DEBIAN&quot; |
| UBUNTU | &quot;UBUNTU&quot; |
| DEBIAN_SNAPSHOT | &quot;DEBIAN_SNAPSHOT&quot; |



