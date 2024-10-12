# OpenapiJsClient.PatientAllergy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the allergy, such as &#x60;\&quot;Cat hair\&quot;&#x60; | [optional] 
**doctor** | **Number** | Id of the doctor who diagnosed the allergy | 
**id** | **Number** |  | [optional] [readonly] 
**notes** | **String** | Any additional notes from the provider | [optional] 
**patient** | **Number** |  | 
**reaction** | **String** | Short description of the patient&#39;s allergic reaction, such as &#x60;\&quot;Hives\&quot;&#x60; | [optional] 
**rxnorm** | **String** | If the allergy is a drug allergy, this is the RxNorm code of the drug | [optional] 
**snomedReaction** | **String** | SNOMED code for the reaction. For possible SnoMED codes, please see [this link from PHIN VADS](https://phinvads.cdc.gov/vads/ViewValueSet.action?id&#x3D;896AABB4-5ACD-DE11-913D-0015173D1785) | [optional] 
**status** | **String** | One of &#x60;\&quot;active\&quot;&#x60;, &#x60;\&quot;inactive\&quot;&#x60;. If absent in &#x60;POST&#x60;, default to &#x60;\&quot;active\&quot;&#x60; | [optional] 



## Enum: SnomedReactionEnum


* `empty` (value: `""`)

* `14669001` (value: `"14669001"`)

* `39579001` (value: `"39579001"`)

* `57676002` (value: `"57676002"`)

* `43724002` (value: `"43724002"`)

* `49727002` (value: `"49727002"`)

* `386661006` (value: `"386661006"`)

* `25064002` (value: `"25064002"`)

* `247472004` (value: `"247472004"`)

* `271795006` (value: `"271795006"`)

* `68962001` (value: `"68962001"`)

* `68235000` (value: `"68235000"`)

* `422587007` (value: `"422587007"`)

* `95388000` (value: `"95388000"`)

* `271807003` (value: `"271807003"`)

* `271825005` (value: `"271825005"`)

* `64531003` (value: `"64531003"`)

* `267036007` (value: `"267036007"`)

* `162397003` (value: `"162397003"`)

* `65124004` (value: `"65124004"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)




