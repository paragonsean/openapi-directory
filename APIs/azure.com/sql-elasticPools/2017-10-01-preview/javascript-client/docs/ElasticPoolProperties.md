# SqlManagementClient.ElasticPoolProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationDate** | **Date** | The creation date of the elastic pool (ISO8601 format). | [optional] [readonly] 
**licenseType** | **String** | The license type to apply for this elastic pool. | [optional] 
**maxSizeBytes** | **Number** | The storage limit for the database elastic pool in bytes. | [optional] 
**perDatabaseSettings** | [**ElasticPoolPerDatabaseSettings**](ElasticPoolPerDatabaseSettings.md) |  | [optional] 
**state** | **String** | The state of the elastic pool. | [optional] [readonly] 
**zoneRedundant** | **Boolean** | Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones. | [optional] 



## Enum: LicenseTypeEnum


* `LicenseIncluded` (value: `"LicenseIncluded"`)

* `BasePrice` (value: `"BasePrice"`)





## Enum: StateEnum


* `Creating` (value: `"Creating"`)

* `Ready` (value: `"Ready"`)

* `Disabled` (value: `"Disabled"`)




