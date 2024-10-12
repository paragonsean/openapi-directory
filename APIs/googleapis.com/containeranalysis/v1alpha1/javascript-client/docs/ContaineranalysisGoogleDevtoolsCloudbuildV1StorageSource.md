# ContainerAnalysisApi.ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **String** | Cloud Storage bucket containing the source (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)). | [optional] 
**generation** | **String** | Cloud Storage generation for the object. If the generation is omitted, the latest generation will be used. | [optional] 
**object** | **String** | Cloud Storage object containing the source. This object must be a zipped (&#x60;.zip&#x60;) or gzipped archive file (&#x60;.tar.gz&#x60;) containing source to build. | [optional] 
**sourceFetcher** | **String** | Optional. Option to specify the tool to fetch the source file for the build. | [optional] 



## Enum: SourceFetcherEnum


* `SOURCE_FETCHER_UNSPECIFIED` (value: `"SOURCE_FETCHER_UNSPECIFIED"`)

* `GSUTIL` (value: `"GSUTIL"`)

* `GCS_FETCHER` (value: `"GCS_FETCHER"`)




