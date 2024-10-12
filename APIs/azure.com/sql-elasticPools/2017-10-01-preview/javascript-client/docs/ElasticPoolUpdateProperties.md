# SqlManagementClient.ElasticPoolUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenseType** | **String** | The license type to apply for this elastic pool. | [optional] 
**maxSizeBytes** | **Number** | The storage limit for the database elastic pool in bytes. | [optional] 
**perDatabaseSettings** | [**ElasticPoolPerDatabaseSettings**](ElasticPoolPerDatabaseSettings.md) |  | [optional] 
**zoneRedundant** | **Boolean** | Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones. | [optional] 



## Enum: LicenseTypeEnum


* `LicenseIncluded` (value: `"LicenseIncluded"`)

* `BasePrice` (value: `"BasePrice"`)




