

# ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource

Location of the source in an archive file in Cloud Storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | **String** | Cloud Storage bucket containing the source (see [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-naming#requirements)). |  [optional] |
|**generation** | **String** | Cloud Storage generation for the object. If the generation is omitted, the latest generation will be used. |  [optional] |
|**_object** | **String** | Cloud Storage object containing the source. This object must be a zipped (&#x60;.zip&#x60;) or gzipped archive file (&#x60;.tar.gz&#x60;) containing source to build. |  [optional] |
|**sourceFetcher** | [**SourceFetcherEnum**](#SourceFetcherEnum) | Optional. Option to specify the tool to fetch the source file for the build. |  [optional] |



## Enum: SourceFetcherEnum

| Name | Value |
|---- | -----|
| SOURCE_FETCHER_UNSPECIFIED | &quot;SOURCE_FETCHER_UNSPECIFIED&quot; |
| GSUTIL | &quot;GSUTIL&quot; |
| GCS_FETCHER | &quot;GCS_FETCHER&quot; |



