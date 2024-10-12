

# InsightsV1Conference


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique SID identifier of the Account. |  [optional] |
|**conferenceSid** | **String** | The unique SID identifier of the Conference. |  [optional] |
|**connectDurationSeconds** | **Integer** | Duration of the between conference start event and conference end event in seconds. |  [optional] |
|**createTime** | **OffsetDateTime** | Conference creation date and time in ISO 8601 format. |  [optional] |
|**detectedIssues** | **Object** | Potential issues detected by Twilio during the conference. |  [optional] |
|**durationSeconds** | **Integer** | Conference duration in seconds. |  [optional] |
|**endReason** | **ConferenceEnumConferenceEndReason** |  |  [optional] |
|**endTime** | **OffsetDateTime** | Conference end date and time in ISO 8601 format. |  [optional] |
|**endedBy** | **String** | Call SID of the participant whose actions ended the conference. |  [optional] |
|**friendlyName** | **String** | Custom label for the conference resource, up to 64 characters. |  [optional] |
|**links** | **Object** | Contains a dictionary of URL links to nested resources of this Conference. |  [optional] |
|**maxConcurrentParticipants** | **Integer** | Actual maximum number of concurrent participants in the conference. |  [optional] |
|**maxParticipants** | **Integer** | Maximum number of concurrent participants as specified by the configuration. |  [optional] |
|**mixerRegion** | **ConferenceEnumRegion** |  |  [optional] |
|**mixerRegionRequested** | **ConferenceEnumRegion** |  |  [optional] |
|**processingState** | **ConferenceEnumProcessingState** |  |  [optional] |
|**recordingEnabled** | **Boolean** | Boolean. Indicates whether recording was enabled at the conference mixer. |  [optional] |
|**startTime** | **OffsetDateTime** | Timestamp in ISO 8601 format when the conference started. Conferences do not start until at least two participants join, at least one of whom has startConferenceOnEnter&#x3D;true. |  [optional] |
|**status** | **ConferenceEnumConferenceStatus** |  |  [optional] |
|**tagInfo** | **Object** | Object. Contains details about conference tags including severity. |  [optional] |
|**tags** | **List&lt;ConferenceEnumTag&gt;** | Tags for detected conference conditions and participant behaviors which may be of interest. |  [optional] |
|**uniqueParticipants** | **Integer** | Unique conference participants based on caller ID. |  [optional] |
|**url** | **URI** | The URL of this resource. |  [optional] |



