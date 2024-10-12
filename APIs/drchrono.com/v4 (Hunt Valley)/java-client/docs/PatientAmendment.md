

# PatientAmendment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amendmentFile** | **String** | A PDF file containing the amended information for the patient&#39;s record |  |
|**amendmentName** | **String** |  |  |
|**appointment** | **Integer** | ID of the appointment to which the amendment applies, if any. If present, the &#x60;amendment_file&#x60; will be appended to the clinical note for this appointment. |  [optional] |
|**comments** | **String** |  |  [optional] |
|**doctor** | **Integer** | ID of the doctor who owns the amendment |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**patient** | **Integer** | ID of the patient to whom the amendment applies |  |



