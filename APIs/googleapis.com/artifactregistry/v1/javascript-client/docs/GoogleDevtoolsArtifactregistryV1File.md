# ArtifactRegistryApi.GoogleDevtoolsArtifactregistryV1File

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the File was created. | [optional] [readonly] 
**fetchTime** | **String** | Output only. The time when the last attempt to refresh the file&#39;s data was made. Only set when the repository is remote. | [optional] [readonly] 
**hashes** | [**[Hash]**](Hash.md) | The hashes of the file content. | [optional] 
**name** | **String** | The name of the file, for example: \&quot;projects/p1/locations/us-central1/repositories/repo1/files/a%2Fb%2Fc.txt\&quot;. If the file ID part contains slashes, they are escaped. | [optional] 
**owner** | **String** | The name of the Package or Version that owns this file, if any. | [optional] 
**sizeBytes** | **String** | The size of the File in bytes. | [optional] 
**updateTime** | **String** | Output only. The time when the File was last updated. | [optional] [readonly] 


