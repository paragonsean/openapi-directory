

# StageCdmSoftwareInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**md5sum** | **String** | The MD5 checksum for the CDM software package. |  |
|**packageUrl** | **String** | The URL where the package that contains CDM software is located.  |  |
|**size** | **Long** | Size, in bytes, of the package containing CDM software. |  [optional] |
|**skipDownload** | **Boolean** | Specifies whether to download the CDM software externally. When this value is false, the CDM software package must be available on the cluster. When this value is true, provide the version. |  [optional] |
|**version** | **String** | The version of the CDM software package. If the version is not provided, an attempt is made to parse the version from the package URL. The version is not needed unless the Rubrik provided software package has been renamed.  |  [optional] |



