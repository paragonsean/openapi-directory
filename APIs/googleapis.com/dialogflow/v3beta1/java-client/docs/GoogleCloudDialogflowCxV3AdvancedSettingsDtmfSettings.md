

# GoogleCloudDialogflowCxV3AdvancedSettingsDtmfSettings

Define behaviors for DTMF (dual tone multi frequency).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a \&quot;3\&quot; was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). |  [optional] |
|**finishDigit** | **String** | The digit that terminates a DTMF digit sequence. |  [optional] |
|**maxDigits** | **Integer** | Max length of DTMF digits. |  [optional] |



