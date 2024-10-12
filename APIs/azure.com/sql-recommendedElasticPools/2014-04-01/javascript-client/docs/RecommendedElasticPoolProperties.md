# AzureSqlDatabase.RecommendedElasticPoolProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseDtuMax** | **Number** | The maximum DTU for the database. | [optional] 
**databaseDtuMin** | **Number** | The minimum DTU for the database. | [optional] 
**databaseEdition** | **String** | The edition of the recommended elastic pool. The ElasticPoolEdition enumeration contains all the valid editions. | [optional] [readonly] 
**databases** | [**[RecommendedElasticPoolPropertiesDatabasesInner]**](RecommendedElasticPoolPropertiesDatabasesInner.md) | The list of databases in this pool. Expanded property | [optional] [readonly] 
**dtu** | **Number** | The DTU for the recommended elastic pool. | [optional] 
**maxObservedDtu** | **Number** | Gets maximum observed DTU. | [optional] [readonly] 
**maxObservedStorageMB** | **Number** | Gets maximum observed storage in megabytes. | [optional] [readonly] 
**metrics** | [**[RecommendedElasticPoolMetric]**](RecommendedElasticPoolMetric.md) | The list of databases housed in the server. Expanded property | [optional] [readonly] 
**observationPeriodEnd** | **Date** | The observation period start (ISO8601 format). | [optional] [readonly] 
**observationPeriodStart** | **Date** | The observation period start (ISO8601 format). | [optional] [readonly] 
**storageMB** | **Number** | Gets storage size in megabytes. | [optional] 



## Enum: DatabaseEditionEnum


* `Basic` (value: `"Basic"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `GeneralPurpose` (value: `"GeneralPurpose"`)

* `BusinessCritical` (value: `"BusinessCritical"`)




