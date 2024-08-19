

# VerifyChallengeResponseResult

Result message for VerifiedAccess.VerifyChallengeResponse.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attestedDeviceId** | **String** | Attested device ID (ADID). |  [optional] |
|**customerId** | **String** | Unique customer id that this device belongs to, as defined by the Google Admin SDK at https://developers.google.com/admin-sdk/directory/v1/guides/manage-customers |  [optional] |
|**deviceEnrollmentId** | **String** | Device enrollment id for ChromeOS devices. |  [optional] |
|**devicePermanentId** | **String** | Device permanent id is returned in this field (for the machine response only). |  [optional] |
|**deviceSignal** | **String** | Deprecated. Device signal in json string representation. Prefer using &#x60;device_signals&#x60; instead. |  [optional] |
|**deviceSignals** | [**DeviceSignals**](DeviceSignals.md) |  |  [optional] |
|**keyTrustLevel** | [**KeyTrustLevelEnum**](#KeyTrustLevelEnum) | Device attested key trust level. |  [optional] |
|**profileCustomerId** | **String** | Unique customer id that this profile belongs to, as defined by the Google Admin SDK at https://developers.google.com/admin-sdk/directory/v1/guides/manage-customers |  [optional] |
|**profileKeyTrustLevel** | [**ProfileKeyTrustLevelEnum**](#ProfileKeyTrustLevelEnum) | Profile attested key trust level. |  [optional] |
|**signedPublicKeyAndChallenge** | **String** | Certificate Signing Request (in the SPKAC format, base64 encoded) is returned in this field. This field will be set only if device has included CSR in its challenge response. (the option to include CSR is now available for both user and machine responses) |  [optional] |
|**virtualDeviceId** | **String** | Virtual device id of the device. The definition of virtual device id is platform-specific. |  [optional] |
|**virtualProfileId** | **String** | The ID of a profile on the device. |  [optional] |



## Enum: KeyTrustLevelEnum

| Name | Value |
|---- | -----|
| KEY_TRUST_LEVEL_UNSPECIFIED | &quot;KEY_TRUST_LEVEL_UNSPECIFIED&quot; |
| CHROME_OS_VERIFIED_MODE | &quot;CHROME_OS_VERIFIED_MODE&quot; |
| CHROME_OS_DEVELOPER_MODE | &quot;CHROME_OS_DEVELOPER_MODE&quot; |
| CHROME_BROWSER_HW_KEY | &quot;CHROME_BROWSER_HW_KEY&quot; |
| CHROME_BROWSER_OS_KEY | &quot;CHROME_BROWSER_OS_KEY&quot; |
| CHROME_BROWSER_NO_KEY | &quot;CHROME_BROWSER_NO_KEY&quot; |



## Enum: ProfileKeyTrustLevelEnum

| Name | Value |
|---- | -----|
| KEY_TRUST_LEVEL_UNSPECIFIED | &quot;KEY_TRUST_LEVEL_UNSPECIFIED&quot; |
| CHROME_OS_VERIFIED_MODE | &quot;CHROME_OS_VERIFIED_MODE&quot; |
| CHROME_OS_DEVELOPER_MODE | &quot;CHROME_OS_DEVELOPER_MODE&quot; |
| CHROME_BROWSER_HW_KEY | &quot;CHROME_BROWSER_HW_KEY&quot; |
| CHROME_BROWSER_OS_KEY | &quot;CHROME_BROWSER_OS_KEY&quot; |
| CHROME_BROWSER_NO_KEY | &quot;CHROME_BROWSER_NO_KEY&quot; |



