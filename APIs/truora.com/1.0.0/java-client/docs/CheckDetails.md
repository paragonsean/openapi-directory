

# CheckDetails

Represents background check details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkId** | **String** | Associated background check ID |  |
|**dataSet** | **String** | Details dataset |  |
|**databaseName** | **String** | Database name. Do not use this field to identify the database as its value may vary as the check is completed |  |
|**group** | [**GroupEnum**](#GroupEnum) | table group type |  |
|**id** | **String** | Detail ID |  |
|**result** | [**ResultEnum**](#ResultEnum) | Database result |  |
|**score** | **BigDecimal** | Partial detail score. Scores are aggregated later in the background check |  |
|**tables** | [**List&lt;Table&gt;**](Table.md) | Query detailed information |  |



## Enum: GroupEnum

| Name | Value |
|---- | -----|
| PROFILE | &quot;profile&quot; |
| LEGAL | &quot;legal&quot; |
| AFFILIATIONS | &quot;affiliations&quot; |
| VEHICLE | &quot;vehicle&quot; |
| GLOBAL | &quot;global&quot; |
| MEDIA | &quot;media&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| FOUND | &quot;found&quot; |
| NOT_FOUND | &quot;not_found&quot; |
| ERROR | &quot;error&quot; |



