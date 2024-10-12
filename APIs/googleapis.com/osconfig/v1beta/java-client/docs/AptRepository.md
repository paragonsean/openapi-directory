

# AptRepository

Represents a single Apt package repository. This repository is added to a repo file that is stored at `/etc/apt/sources.list.d/google_osconfig.list`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveType** | [**ArchiveTypeEnum**](#ArchiveTypeEnum) | Type of archive files in this repository. The default behavior is DEB. |  [optional] |
|**components** | **List&lt;String&gt;** | Required. List of components for this repository. Must contain at least one item. |  [optional] |
|**distribution** | **String** | Required. Distribution of this repository. |  [optional] |
|**gpgKey** | **String** | URI of the key file for this repository. The agent maintains a keyring at &#x60;/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg&#x60; containing all the keys in any applied guest policy. |  [optional] |
|**uri** | **String** | Required. URI for this repository. |  [optional] |



## Enum: ArchiveTypeEnum

| Name | Value |
|---- | -----|
| ARCHIVE_TYPE_UNSPECIFIED | &quot;ARCHIVE_TYPE_UNSPECIFIED&quot; |
| DEB | &quot;DEB&quot; |
| DEB_SRC | &quot;DEB_SRC&quot; |



