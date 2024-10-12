

# AptArtifact

A detailed representation of an Apt artifact. Information in the record is derived from the archive's control file. See https://www.debian.org/doc/debian-policy/ch-controlfields.html

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | **String** | Output only. Operating system architecture of the artifact. |  [optional] [readonly] |
|**component** | **String** | Output only. Repository component of the artifact. |  [optional] [readonly] |
|**controlFile** | **byte[]** | Output only. Contents of the artifact&#39;s control metadata file. |  [optional] [readonly] |
|**name** | **String** | Output only. The Artifact Registry resource name of the artifact. |  [optional] [readonly] |
|**packageName** | **String** | Output only. The Apt package name of the artifact. |  [optional] [readonly] |
|**packageType** | [**PackageTypeEnum**](#PackageTypeEnum) | Output only. An artifact is a binary or source package. |  [optional] [readonly] |



## Enum: PackageTypeEnum

| Name | Value |
|---- | -----|
| PACKAGE_TYPE_UNSPECIFIED | &quot;PACKAGE_TYPE_UNSPECIFIED&quot; |
| BINARY | &quot;BINARY&quot; |
| SOURCE | &quot;SOURCE&quot; |



