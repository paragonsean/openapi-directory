# AwsSigner.StartSigningJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**StartSigningJobRequestSource**](StartSigningJobRequestSource.md) |  | 
**destination** | [**StartSigningJobRequestDestination**](StartSigningJobRequestDestination.md) |  | 
**profileName** | **String** | The name of the signing profile. | 
**clientRequestToken** | **String** | String that identifies the signing request. All calls after the first that use this token return the same response as the first call. | 
**profileOwner** | **String** | The AWS account ID of the signing profile owner. | [optional] 


