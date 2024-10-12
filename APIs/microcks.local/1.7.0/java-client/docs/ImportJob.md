

# ImportJob

An ImportJob allow defining a repository artifact to poll for discovering Services and APIs mocks and tests

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether this ImportJob is active (ie. scheduled for execution) |  [optional] |
|**createdDate** | **OffsetDateTime** | Creation date for this ImportJob |  [optional] |
|**etag** | **String** | Etag of repository URL during previous import. Is used for not re-importing if no recent changes |  [optional] |
|**frequency** | **String** | Reserved for future usage |  [optional] |
|**id** | **String** | Unique identifier of ImportJob |  [optional] |
|**lastImportDate** | **OffsetDateTime** | Date last import was done |  [optional] |
|**lastImportError** | **String** | Error message of last import (if any) |  [optional] |
|**mainArtifact** | **Boolean** | Flag telling if considered as primary or secondary artifact. Default to &#x60;true&#x60; |  [optional] |
|**metadata** | [**Metadata**](Metadata.md) |  |  [optional] |
|**name** | **String** | Unique distinct name of this ImportJob |  |
|**repositoryDisableSSLValidation** | **Boolean** | Whether to disable SSL certificate verification when checking repository |  [optional] |
|**repositoryUrl** | **String** | URL of mocks and tests repository artifact |  |
|**secretRef** | [**SecretRef**](SecretRef.md) |  |  [optional] |
|**serviceRefs** | [**List&lt;ServiceRef&gt;**](ServiceRef.md) | References of Services discovered when checking repository |  [optional] |



