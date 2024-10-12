# CloudOsLoginApi.PosixAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Output only. A POSIX account identifier. | [optional] [readonly] 
**gecos** | **String** | The GECOS (user information) entry for this account. | [optional] 
**gid** | **String** | The default group ID. | [optional] 
**homeDirectory** | **String** | The path to the home directory for this account. | [optional] 
**name** | **String** | Output only. The canonical resource name. | [optional] [readonly] 
**operatingSystemType** | **String** | The operating system type where this account applies. | [optional] 
**primary** | **Boolean** | Only one POSIX account can be marked as primary. | [optional] 
**shell** | **String** | The path to the logic shell for this account. | [optional] 
**systemId** | **String** | System identifier for which account the username or uid applies to. By default, the empty value is used. | [optional] 
**uid** | **String** | The user ID. | [optional] 
**username** | **String** | The username of the POSIX account. | [optional] 



## Enum: OperatingSystemTypeEnum


* `OPERATING_SYSTEM_TYPE_UNSPECIFIED` (value: `"OPERATING_SYSTEM_TYPE_UNSPECIFIED"`)

* `LINUX` (value: `"LINUX"`)

* `WINDOWS` (value: `"WINDOWS"`)




