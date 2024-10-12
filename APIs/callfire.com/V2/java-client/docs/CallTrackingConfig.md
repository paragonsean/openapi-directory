

# CallTrackingConfig

Call tracking configuration allows you track incoming calls, analyze, respond to customers using sms or voice replies. For more information see [call tracking page](https://www.callfire.com/products/call-tracking)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failedTransferSoundId** | **Long** | An id of sound file, played if caller can not be connected to transfer number for any reason |  [optional] |
|**googleAnalytics** | [**GoogleAnalytics**](GoogleAnalytics.md) |  |  [optional] |
|**introSoundId** | **Long** | An id of sound file, played if call is answered |  [optional] |
|**recorded** | **Boolean** | Records all inbound calls |  [optional] |
|**screen** | **Boolean** | Screens the incoming calls |  [optional] |
|**transferNumbers** | **List&lt;String&gt;** | List of phone numbers in E.164 format (11-digit) are used for transfer. Example: 12132000384 |  [optional] |
|**voicemail** | **Boolean** | Enables voicemail if call is not transferred |  [optional] |
|**voicemailSoundId** | **Long** | An id of sound file, played if voicemail is enabled and a call isn&#39;t transferred |  [optional] |
|**weeklySchedule** | [**WeeklySchedule**](WeeklySchedule.md) |  |  [optional] |
|**whisperSoundId** | **Long** | An id of sound file, played if call is screened |  [optional] |



