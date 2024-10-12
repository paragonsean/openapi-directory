

# GetStatusOutput

Output structure for the GetStatus operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | **String** | A unique identifier which refers to a particular job. |  [optional] |
|**jobType** | **JobType** |  |  [optional] |
|**locationCode** | **String** | A token representing the location of the storage device, such as \&quot;AtAWS\&quot;. |  [optional] |
|**locationMessage** | **String** | A more human readable form of the physical location of the storage device. |  [optional] |
|**progressCode** | **String** | A token representing the state of the job, such as \&quot;Started\&quot;. |  [optional] |
|**progressMessage** | **String** | A more human readable form of the job status. |  [optional] |
|**carrier** | **String** | Name of the shipping company. This value is included when the LocationCode is \&quot;Returned\&quot;. |  [optional] |
|**trackingNumber** | **String** | The shipping tracking number assigned by AWS Import/Export to the storage device when it&#39;s returned to you. We return this value when the LocationCode is \&quot;Returned\&quot;. |  [optional] |
|**logBucket** | **String** | Amazon S3 bucket for user logs. |  [optional] |
|**logKey** | **String** | The key where the user logs were stored. |  [optional] |
|**errorCount** | **Integer** | Number of errors. We return this value when the ProgressCode is Success or SuccessWithErrors. |  [optional] |
|**signature** | **String** | An encrypted code used to authenticate the request and response, for example, \&quot;DV+TpDfx1/TdSE9ktyK9k/bDTVI&#x3D;\&quot;. Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value. |  [optional] |
|**signatureFileContents** | **String** | An encrypted code used to authenticate the request and response, for example, \&quot;DV+TpDfx1/TdSE9ktyK9k/bDTVI&#x3D;\&quot;. Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value. |  [optional] |
|**currentManifest** | **String** | The last manifest submitted, which will be used to process the job. |  [optional] |
|**creationDate** | **OffsetDateTime** | Timestamp of the CreateJob request in ISO8601 date format. For example \&quot;2010-03-28T20:27:35Z\&quot;. |  [optional] |
|**artifactList** | [**List&lt;Artifact&gt;**](Artifact.md) | A collection of artifacts. |  [optional] |



