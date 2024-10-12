

# PatientAllergy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the allergy, such as &#x60;\&quot;Cat hair\&quot;&#x60; |  [optional] |
|**doctor** | **Integer** | Id of the doctor who diagnosed the allergy |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**notes** | **String** | Any additional notes from the provider |  [optional] |
|**patient** | **Integer** |  |  |
|**reaction** | **String** | Short description of the patient&#39;s allergic reaction, such as &#x60;\&quot;Hives\&quot;&#x60; |  [optional] |
|**rxnorm** | **String** | If the allergy is a drug allergy, this is the RxNorm code of the drug |  [optional] |
|**snomedReaction** | [**SnomedReactionEnum**](#SnomedReactionEnum) | SNOMED code for the reaction. For possible SnoMED codes, please see [this link from PHIN VADS](https://phinvads.cdc.gov/vads/ViewValueSet.action?id&#x3D;896AABB4-5ACD-DE11-913D-0015173D1785) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | One of &#x60;\&quot;active\&quot;&#x60;, &#x60;\&quot;inactive\&quot;&#x60;. If absent in &#x60;POST&#x60;, default to &#x60;\&quot;active\&quot;&#x60; |  [optional] |



## Enum: SnomedReactionEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| _14669001 | &quot;14669001&quot; |
| _39579001 | &quot;39579001&quot; |
| _57676002 | &quot;57676002&quot; |
| _43724002 | &quot;43724002&quot; |
| _49727002 | &quot;49727002&quot; |
| _386661006 | &quot;386661006&quot; |
| _25064002 | &quot;25064002&quot; |
| _247472004 | &quot;247472004&quot; |
| _271795006 | &quot;271795006&quot; |
| _68962001 | &quot;68962001&quot; |
| _68235000 | &quot;68235000&quot; |
| _422587007 | &quot;422587007&quot; |
| _95388000 | &quot;95388000&quot; |
| _271807003 | &quot;271807003&quot; |
| _271825005 | &quot;271825005&quot; |
| _64531003 | &quot;64531003&quot; |
| _267036007 | &quot;267036007&quot; |
| _162397003 | &quot;162397003&quot; |
| _65124004 | &quot;65124004&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



