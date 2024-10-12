

# ConditionDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acuteness** | [**AcutenessEnum**](#AcutenessEnum) |  |  [optional] |
|**categories** | **List&lt;String&gt;** |  |  |
|**commonName** | **String** |  |  [optional] |
|**extras** | **Map&lt;String, Object&gt;** | additional content, like custom properties or images |  [optional] |
|**id** | **String** |  |  |
|**name** | **String** |  |  |
|**prevalence** | [**PrevalenceEnum**](#PrevalenceEnum) |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |
|**sexFilter** | [**SexFilterEnum**](#SexFilterEnum) |  |  |
|**triageLevel** | [**TriageLevelEnum**](#TriageLevelEnum) |  |  [optional] |



## Enum: AcutenessEnum

| Name | Value |
|---- | -----|
| CHRONIC | &quot;chronic&quot; |
| CHRONIC_WITH_EXACERBATIONS | &quot;chronic_with_exacerbations&quot; |
| ACUTE_POTENTIALLY_CHRONIC | &quot;acute_potentially_chronic&quot; |
| ACUTE | &quot;acute&quot; |



## Enum: PrevalenceEnum

| Name | Value |
|---- | -----|
| VERY_RARE | &quot;very_rare&quot; |
| RARE | &quot;rare&quot; |
| MODERATE | &quot;moderate&quot; |
| COMMON | &quot;common&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| MILD | &quot;mild&quot; |
| MODERATE | &quot;moderate&quot; |
| SEVERE | &quot;severe&quot; |



## Enum: SexFilterEnum

| Name | Value |
|---- | -----|
| BOTH | &quot;both&quot; |
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



## Enum: TriageLevelEnum

| Name | Value |
|---- | -----|
| EMERGENCY_AMBULANCE | &quot;emergency_ambulance&quot; |
| EMERGENCY | &quot;emergency&quot; |
| CONSULTATION_24 | &quot;consultation_24&quot; |
| CONSULTATION | &quot;consultation&quot; |
| SELF_CARE | &quot;self_care&quot; |



