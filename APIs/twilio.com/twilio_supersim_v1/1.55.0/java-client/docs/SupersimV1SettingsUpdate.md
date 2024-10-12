

# SupersimV1SettingsUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateCompleted** | **OffsetDateTime** | The time, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, when the update successfully completed and the new settings were applied to the SIM. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date that this Settings Update was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this Settings Update was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**iccid** | **String** | The [ICCID](https://en.wikipedia.org/wiki/SIM_card#ICCID) associated with the SIM. |  [optional] |
|**packages** | **List&lt;Object&gt;** | Array containing the different Settings Packages that will be applied to the SIM after the update completes. Each object within the array indicates the name and the version of the Settings Package that will be on the SIM if the update is successful. |  [optional] |
|**sid** | **String** | The unique identifier of this Settings Update. |  [optional] |
|**simSid** | **String** | The SID of the Super SIM to which this Settings Update was applied. |  [optional] |
|**status** | **SettingsUpdateEnumStatus** |  |  [optional] |



