# AzureSqlDatabase.ElasticPoolProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationDate** | **Date** | The creation date of the elastic pool (ISO8601 format). | [optional] [readonly] 
**databaseDtuMax** | **Number** | The maximum DTU any one database can consume. | [optional] 
**databaseDtuMin** | **Number** | The minimum DTU all databases are guaranteed. | [optional] 
**dtu** | **Number** | The total shared DTU for the database elastic pool. | [optional] 
**edition** | **String** | The edition of the elastic pool. | [optional] 
**state** | **String** | The state of the elastic pool. | [optional] [readonly] 
**storageMB** | **Number** | Gets storage limit for the database elastic pool in MB. | [optional] 
**zoneRedundant** | **Boolean** | Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availability zones. | [optional] 



## Enum: EditionEnum


* `Basic` (value: `"Basic"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `GeneralPurpose` (value: `"GeneralPurpose"`)

* `BusinessCritical` (value: `"BusinessCritical"`)





## Enum: StateEnum


* `Creating` (value: `"Creating"`)

* `Ready` (value: `"Ready"`)

* `Disabled` (value: `"Disabled"`)




