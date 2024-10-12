

# UpdateJobOutput

Output structure for the UpateJob operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** | Specifies whether (true) or not (false) AWS Import/Export updated your job. |  [optional] |
|**warningMessage** | **String** | An optional message notifying you of non-fatal issues with the job, such as use of an incompatible Amazon S3 bucket name. |  [optional] |
|**artifactList** | [**List&lt;Artifact&gt;**](Artifact.md) | A collection of artifacts. |  [optional] |



