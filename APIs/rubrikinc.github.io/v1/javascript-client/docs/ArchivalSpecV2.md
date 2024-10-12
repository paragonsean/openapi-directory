# RubrikRestApi.ArchivalSpecV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archivalThreshold** | **Number** | Amount of time, in seconds, after which the snapshot must be uploaded. | 
**archivalTieringSpec** | [**ArchivalTieringSpec**](ArchivalTieringSpec.md) |  | [optional] 
**isPassthroughSupported** | **Boolean** | Boolean value that indicates if the archival location type supports direct archive backups.  | [optional] 
**locationId** | **String** |  | [optional] 
**locationName** | **String** |  | [optional] 
**polarisManagedId** | **String** | The Polaris managed ID of an archival location. At least one of the parameters locationId and polarisManagedId must be defined to correctly refer to an archival location.  | [optional] 


