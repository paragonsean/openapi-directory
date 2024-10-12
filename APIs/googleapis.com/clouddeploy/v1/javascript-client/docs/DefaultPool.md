# CloudDeployApi.DefaultPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactStorage** | **String** | Optional. Cloud Storage location where execution outputs should be stored. This can either be a bucket (\&quot;gs://my-bucket\&quot;) or a path within a bucket (\&quot;gs://my-bucket/my-dir\&quot;). If unspecified, a default bucket located in the same region will be used. | [optional] 
**serviceAccount** | **String** | Optional. Google service account to use for execution. If unspecified, the project execution service account (-compute@developer.gserviceaccount.com) will be used. | [optional] 


