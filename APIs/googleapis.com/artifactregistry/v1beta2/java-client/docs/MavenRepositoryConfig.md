

# MavenRepositoryConfig

MavenRepositoryConfig is maven related repository details. Provides additional configuration details for repositories of the maven format type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowSnapshotOverwrites** | **Boolean** | The repository with this flag will allow publishing the same snapshot versions. |  [optional] |
|**versionPolicy** | [**VersionPolicyEnum**](#VersionPolicyEnum) | Version policy defines the versions that the registry will accept. |  [optional] |



## Enum: VersionPolicyEnum

| Name | Value |
|---- | -----|
| VERSION_POLICY_UNSPECIFIED | &quot;VERSION_POLICY_UNSPECIFIED&quot; |
| RELEASE | &quot;RELEASE&quot; |
| SNAPSHOT | &quot;SNAPSHOT&quot; |



