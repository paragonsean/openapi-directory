# OsConfigApi.SoftwareRecipeArtifactGcs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **String** | Bucket of the Google Cloud Storage object. Given an example URL: &#x60;https://storage.googleapis.com/my-bucket/foo/bar#1234567&#x60; this value would be &#x60;my-bucket&#x60;. | [optional] 
**generation** | **String** | Must be provided if allow_insecure is false. Generation number of the Google Cloud Storage object. &#x60;https://storage.googleapis.com/my-bucket/foo/bar#1234567&#x60; this value would be &#x60;1234567&#x60;. | [optional] 
**object** | **String** | Name of the Google Cloud Storage object. As specified [here] (https://cloud.google.com/storage/docs/naming#objectnames) Given an example URL: &#x60;https://storage.googleapis.com/my-bucket/foo/bar#1234567&#x60; this value would be &#x60;foo/bar&#x60;. | [optional] 


