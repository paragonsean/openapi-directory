

# ElasticPoolUpdateProperties

Properties of an elastic pool

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type to apply for this elastic pool. |  [optional] |
|**maxSizeBytes** | **Long** | The storage limit for the database elastic pool in bytes. |  [optional] |
|**perDatabaseSettings** | [**ElasticPoolPerDatabaseSettings**](ElasticPoolPerDatabaseSettings.md) |  |  [optional] |
|**zoneRedundant** | **Boolean** | Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones. |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| LICENSE_INCLUDED | &quot;LicenseIncluded&quot; |
| BASE_PRICE | &quot;BasePrice&quot; |



