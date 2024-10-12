

# Conversion

A Conversion represents when a user successfully performs a desired action after seeing an ad.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childDirectedTreatment** | **Boolean** | Whether this particular request may come from a user under the age of 13, under COPPA compliance. |  [optional] |
|**customVariables** | [**List&lt;CustomFloodlightVariable&gt;**](CustomFloodlightVariable.md) | Custom floodlight variables. This field may only be used when calling batchinsert; it is not supported by batchupdate. |  [optional] |
|**encryptedUserId** | **String** | The alphanumeric encrypted user ID. When set, encryptionInfo should also be specified. This field is mutually exclusive with encryptedUserIdCandidates[], matchId, mobileDeviceId and gclid. This or encryptedUserIdCandidates[] or matchId or mobileDeviceId or gclid is a required field. |  [optional] |
|**encryptedUserIdCandidates** | **List&lt;String&gt;** | A list of the alphanumeric encrypted user IDs. Any user ID with exposure prior to the conversion timestamp will be used in the inserted conversion. If no such user ID is found then the conversion will be rejected with INVALID_ARGUMENT error. When set, encryptionInfo should also be specified. This field may only be used when calling batchinsert; it is not supported by batchupdate. This field is mutually exclusive with encryptedUserId, matchId, mobileDeviceId and gclid. This or encryptedUserId or matchId or mobileDeviceId or gclid is a required field. |  [optional] |
|**floodlightActivityId** | **String** | Floodlight Activity ID of this conversion. This is a required field. |  [optional] |
|**floodlightConfigurationId** | **String** | Floodlight Configuration ID of this conversion. This is a required field. |  [optional] |
|**gclid** | **String** | The Google click ID. This field is mutually exclusive with encryptedUserId, encryptedUserIdCandidates[], matchId and mobileDeviceId. This or encryptedUserId or encryptedUserIdCandidates[] or matchId or mobileDeviceId is a required field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#conversion\&quot;. |  [optional] |
|**limitAdTracking** | **Boolean** | Whether Limit Ad Tracking is enabled. When set to true, the conversion will be used for reporting but not targeting. This will prevent remarketing. |  [optional] |
|**matchId** | **String** | The match ID field. A match ID is your own first-party identifier that has been synced with Google using the match ID feature in Floodlight. This field is mutually exclusive with encryptedUserId, encryptedUserIdCandidates[],mobileDeviceId and gclid. This or encryptedUserId or encryptedUserIdCandidates[] or mobileDeviceId or gclid is a required field. |  [optional] |
|**mobileDeviceId** | **String** | The mobile device ID. This field is mutually exclusive with encryptedUserId, encryptedUserIdCandidates[], matchId and gclid. This or encryptedUserId or encryptedUserIdCandidates[] or matchId or gclid is a required field. |  [optional] |
|**nonPersonalizedAd** | **Boolean** | Whether the conversion was for a non personalized ad. |  [optional] |
|**ordinal** | **String** | The ordinal of the conversion. Use this field to control how conversions of the same user and day are de-duplicated. This is a required field. |  [optional] |
|**quantity** | **String** | The quantity of the conversion. |  [optional] |
|**timestampMicros** | **String** | The timestamp of conversion, in Unix epoch micros. This is a required field. |  [optional] |
|**treatmentForUnderage** | **Boolean** | Whether this particular request may come from a user under the age of 16 (may differ by country), under compliance with the European Union&#39;s General Data Protection Regulation (GDPR). |  [optional] |
|**value** | **Double** | The value of the conversion. |  [optional] |



