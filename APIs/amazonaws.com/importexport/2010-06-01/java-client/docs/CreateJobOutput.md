

# CreateJobOutput

Output structure for the CreateJob operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | **String** | A unique identifier which refers to a particular job. |  [optional] |
|**jobType** | **JobType** |  |  [optional] |
|**signature** | **String** | An encrypted code used to authenticate the request and response, for example, \&quot;DV+TpDfx1/TdSE9ktyK9k/bDTVI&#x3D;\&quot;. Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value. |  [optional] |
|**signatureFileContents** | **String** | The actual text of the SIGNATURE file to be written to disk. |  [optional] |
|**warningMessage** | **String** | An optional message notifying you of non-fatal issues with the job, such as use of an incompatible Amazon S3 bucket name. |  [optional] |
|**artifactList** | [**List&lt;Artifact&gt;**](Artifact.md) | A collection of artifacts. |  [optional] |



