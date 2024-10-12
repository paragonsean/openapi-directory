

# AvailableVersionInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availability** | **SoftwareAvailability** |  |  |
|**description** | **String** | Brief description of the Rubrik CDM version. An example response value is \&quot;Rubrik 5.0 (GA)\&quot;.  |  [optional] |
|**downloadJobInfo** | [**DownloadJobInfo**](DownloadJobInfo.md) |  |  [optional] |
|**generalAvailabilityReleaseDateForReleaseFamily** | **String** | The date the Rubrik CDM family was released. This date is only available for software images stored remotely and not yet downloaded. |  [optional] |
|**md5sum** | **String** | The MD5 checksum of the software image. This value is used to verify the integrity of the package download. |  [optional] |
|**releaseDate** | **String** | The date the Rubrik CDM version was released. This is only available for software images stored remotely and not yet downloaded. |  [optional] |
|**releaseNotes** | **String** | The URL used to access the version Release Notes for the Rubrik CDM software image. The URL is available only for software images stored remotely and not yet downloaded. |  [optional] |
|**remoteDownloadUrl** | **String** | The remote download URL of the Rubrik CDM software image. This URL is used to download the software to the Rubrik cluster. |  [optional] |
|**size** | **Long** | The size, in bytes, of the downloaded software image. |  [optional] |
|**version** | **String** | The version of Rubrik CDM available in the Rubrik cluster or in the Rubrik remote central repository. |  |



