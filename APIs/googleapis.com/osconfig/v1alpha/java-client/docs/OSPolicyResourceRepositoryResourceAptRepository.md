

# OSPolicyResourceRepositoryResourceAptRepository

Represents a single apt package repository. These will be added to a repo file that will be managed at `/etc/apt/sources.list.d/google_osconfig.list`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveType** | [**ArchiveTypeEnum**](#ArchiveTypeEnum) | Required. Type of archive files in this repository. |  [optional] |
|**components** | **List&lt;String&gt;** | Required. List of components for this repository. Must contain at least one item. |  [optional] |
|**distribution** | **String** | Required. Distribution of this repository. |  [optional] |
|**gpgKey** | **String** | URI of the key file for this repository. The agent maintains a keyring at &#x60;/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg&#x60;. |  [optional] |
|**uri** | **String** | Required. URI for this repository. |  [optional] |



## Enum: ArchiveTypeEnum

| Name | Value |
|---- | -----|
| ARCHIVE_TYPE_UNSPECIFIED | &quot;ARCHIVE_TYPE_UNSPECIFIED&quot; |
| DEB | &quot;DEB&quot; |
| DEB_SRC | &quot;DEB_SRC&quot; |



