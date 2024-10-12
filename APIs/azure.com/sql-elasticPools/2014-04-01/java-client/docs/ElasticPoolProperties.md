

# ElasticPoolProperties

Represents the properties of an elastic pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **OffsetDateTime** | The creation date of the elastic pool (ISO8601 format). |  [optional] [readonly] |
|**databaseDtuMax** | **Integer** | The maximum DTU any one database can consume. |  [optional] |
|**databaseDtuMin** | **Integer** | The minimum DTU all databases are guaranteed. |  [optional] |
|**dtu** | **Integer** | The total shared DTU for the database elastic pool. |  [optional] |
|**edition** | [**EditionEnum**](#EditionEnum) | The edition of the elastic pool. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the elastic pool. |  [optional] [readonly] |
|**storageMB** | **Integer** | Gets storage limit for the database elastic pool in MB. |  [optional] |
|**zoneRedundant** | **Boolean** | Whether or not this database elastic pool is zone redundant, which means the replicas of this database will be spread across multiple availability zones. |  [optional] |



## Enum: EditionEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| GENERAL_PURPOSE | &quot;GeneralPurpose&quot; |
| BUSINESS_CRITICAL | &quot;BusinessCritical&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| READY | &quot;Ready&quot; |
| DISABLED | &quot;Disabled&quot; |



