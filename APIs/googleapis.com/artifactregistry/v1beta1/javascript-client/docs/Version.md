# ArtifactRegistryApi.Version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time when the version was created. | [optional] 
**description** | **String** | Optional. Description of the version, as specified in its metadata. | [optional] 
**name** | **String** | The name of the version, for example: \&quot;projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/art1\&quot;. If the package or version ID parts contain slashes, the slashes are escaped. | [optional] 
**relatedTags** | [**[Tag]**](Tag.md) | Output only. A list of related tags. Will contain up to 100 tags that reference this version. | [optional] 
**updateTime** | **String** | The time when the version was last updated. | [optional] 


