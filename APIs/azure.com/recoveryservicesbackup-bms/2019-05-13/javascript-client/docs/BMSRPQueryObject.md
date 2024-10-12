# RecoveryServicesBackupClient.BMSRPQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endDate** | **Date** | Backup copies created before this time. | [optional] 
**extendedInfo** | **Boolean** | In Get Recovery Point, it tells whether extended information about recovery point is asked. | [optional] 
**restorePointQueryType** | **String** | RestorePoint type | [optional] 
**startDate** | **Date** | Backup copies created after this time. | [optional] 



## Enum: RestorePointQueryTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Full` (value: `"Full"`)

* `Log` (value: `"Log"`)

* `Differential` (value: `"Differential"`)

* `FullAndDifferential` (value: `"FullAndDifferential"`)

* `All` (value: `"All"`)




