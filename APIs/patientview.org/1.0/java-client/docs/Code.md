

# Code


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** |  |  [optional] |
|**codeCategories** | [**Set&lt;CodeCategory&gt;**](CodeCategory.md) |  |  [optional] |
|**codeType** | [**Lookup**](Lookup.md) |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**displayOrder** | **Integer** |  |  [optional] |
|**externalStandards** | [**Set&lt;CodeExternalStandard&gt;**](CodeExternalStandard.md) |  |  [optional] |
|**fullDescription** | **String** |  |  [optional] |
|**hideFromPatients** | **Boolean** |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**lastUpdate** | **OffsetDateTime** |  |  [optional] |
|**links** | [**Set&lt;Link&gt;**](Link.md) |  |  [optional] |
|**patientFriendlyName** | **String** |  |  [optional] |
|**removedExternally** | **Boolean** |  |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) |  |  [optional] |
|**standardType** | [**Lookup**](Lookup.md) |  |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| PATIENTVIEW | &quot;PATIENTVIEW&quot; |
| NHS_CHOICES | &quot;NHS_CHOICES&quot; |



