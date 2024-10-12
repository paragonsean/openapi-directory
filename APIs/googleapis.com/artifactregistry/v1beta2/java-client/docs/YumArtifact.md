

# YumArtifact

A detailed representation of a Yum artifact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | **String** | Output only. Operating system architecture of the artifact. |  [optional] [readonly] |
|**name** | **String** | Output only. The Artifact Registry resource name of the artifact. |  [optional] [readonly] |
|**packageName** | **String** | Output only. The yum package name of the artifact. |  [optional] [readonly] |
|**packageType** | [**PackageTypeEnum**](#PackageTypeEnum) | Output only. An artifact is a binary or source package. |  [optional] [readonly] |



## Enum: PackageTypeEnum

| Name | Value |
|---- | -----|
| PACKAGE_TYPE_UNSPECIFIED | &quot;PACKAGE_TYPE_UNSPECIFIED&quot; |
| BINARY | &quot;BINARY&quot; |
| SOURCE | &quot;SOURCE&quot; |



