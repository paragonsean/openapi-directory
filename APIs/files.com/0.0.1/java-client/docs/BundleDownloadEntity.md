

# BundleDownloadEntity

List Bundle Downloads

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundleRegistration** | [**BundleRegistrationEntity**](BundleRegistrationEntity.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Download date/time |  [optional] |
|**downloadMethod** | [**DownloadMethodEnum**](#DownloadMethodEnum) | Download method (file or full_zip) |  [optional] |
|**path** | **String** | Download path |  [optional] |



## Enum: DownloadMethodEnum

| Name | Value |
|---- | -----|
| FILE | &quot;file&quot; |
| FULL_ZIP | &quot;full_zip&quot; |



