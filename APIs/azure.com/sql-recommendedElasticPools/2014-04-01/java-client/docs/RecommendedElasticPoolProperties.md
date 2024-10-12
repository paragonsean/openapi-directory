

# RecommendedElasticPoolProperties

Represents the properties of a recommended elastic pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseDtuMax** | **Double** | The maximum DTU for the database. |  [optional] |
|**databaseDtuMin** | **Double** | The minimum DTU for the database. |  [optional] |
|**databaseEdition** | [**DatabaseEditionEnum**](#DatabaseEditionEnum) | The edition of the recommended elastic pool. The ElasticPoolEdition enumeration contains all the valid editions. |  [optional] [readonly] |
|**databases** | [**List&lt;RecommendedElasticPoolPropertiesDatabasesInner&gt;**](RecommendedElasticPoolPropertiesDatabasesInner.md) | The list of databases in this pool. Expanded property |  [optional] [readonly] |
|**dtu** | **Double** | The DTU for the recommended elastic pool. |  [optional] |
|**maxObservedDtu** | **Double** | Gets maximum observed DTU. |  [optional] [readonly] |
|**maxObservedStorageMB** | **Double** | Gets maximum observed storage in megabytes. |  [optional] [readonly] |
|**metrics** | [**List&lt;RecommendedElasticPoolMetric&gt;**](RecommendedElasticPoolMetric.md) | The list of databases housed in the server. Expanded property |  [optional] [readonly] |
|**observationPeriodEnd** | **OffsetDateTime** | The observation period start (ISO8601 format). |  [optional] [readonly] |
|**observationPeriodStart** | **OffsetDateTime** | The observation period start (ISO8601 format). |  [optional] [readonly] |
|**storageMB** | **Double** | Gets storage size in megabytes. |  [optional] |



## Enum: DatabaseEditionEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| GENERAL_PURPOSE | &quot;GeneralPurpose&quot; |
| BUSINESS_CRITICAL | &quot;BusinessCritical&quot; |



