

# PatientResourceAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**archiveHistory** | [**List&lt;ArchiveHistory&gt;**](ArchiveHistory.md) |  |  [optional] |
|**archived** | **Boolean** |  |  [optional] [readonly] |
|**birthDate** | **LocalDate** |  |  [optional] |
|**emailAddress** | **String** |  |  [optional] |
|**enrolledAt** | **String** |  |  [optional] [readonly] |
|**firstAccessAt** | **String** |  |  [optional] [readonly] |
|**firstName** | **String** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  [optional] |
|**identifiers** | [**List&lt;PatientIdentifier&gt;**](PatientIdentifier.md) |  |  [optional] |
|**invitedAt** | **String** |  |  [optional] [readonly] |
|**lastAccessAt** | **String** |  |  [optional] [readonly] |
|**lastName** | **String** |  |  [optional] |
|**note** | **String** | Coach&#39;s note about the patient. Not visible to the patient. |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) |  |  [optional] |
|**statement** | [**PatientResourceAttributesStatement**](PatientResourceAttributesStatement.md) |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |
| OTHER | &quot;other&quot; |



