# OsConfigApi.AptRepository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveType** | **String** | Type of archive files in this repository. The default behavior is DEB. | [optional] 
**components** | **[String]** | Required. List of components for this repository. Must contain at least one item. | [optional] 
**distribution** | **String** | Required. Distribution of this repository. | [optional] 
**gpgKey** | **String** | URI of the key file for this repository. The agent maintains a keyring at &#x60;/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg&#x60; containing all the keys in any applied guest policy. | [optional] 
**uri** | **String** | Required. URI for this repository. | [optional] 



## Enum: ArchiveTypeEnum


* `ARCHIVE_TYPE_UNSPECIFIED` (value: `"ARCHIVE_TYPE_UNSPECIFIED"`)

* `DEB` (value: `"DEB"`)

* `DEB_SRC` (value: `"DEB_SRC"`)




