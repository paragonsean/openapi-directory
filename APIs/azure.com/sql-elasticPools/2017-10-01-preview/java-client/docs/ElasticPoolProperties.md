

# ElasticPoolProperties

Properties of an elastic pool

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **OffsetDateTime** | The creation date of the elastic pool (ISO8601 format). |  [optional] [readonly] |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type to apply for this elastic pool. |  [optional] |
|**maxSizeBytes** | **Long** | The storage limit for the database elastic pool in bytes. |  [optional] |
|**perDatabaseSettings** | [**ElasticPoolPerDatabaseSettings**](ElasticPoolPerDatabaseSettings.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the elastic pool. |  [optional] [readonly] |
|**zoneRedundant** | **Boolean** | Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones. |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| LICENSE_INCLUDED | &quot;LicenseIncluded&quot; |
| BASE_PRICE | &quot;BasePrice&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| READY | &quot;Ready&quot; |
| DISABLED | &quot;Disabled&quot; |



