

# ContentKeyPolicyPlayReadyPlayRight

Configures the Play Right in the PlayReady license.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agcAndColorStripeRestriction** | **Integer** | Configures Automatic Gain Control (AGC) and Color Stripe in the license. Must be between 0 and 3 inclusive. |  [optional] |
|**allowPassingVideoContentToUnknownOutput** | [**AllowPassingVideoContentToUnknownOutputEnum**](#AllowPassingVideoContentToUnknownOutputEnum) | Configures Unknown output handling settings of the license. |  |
|**analogVideoOpl** | **Integer** | Specifies the output protection level for compressed digital audio. |  [optional] |
|**compressedDigitalAudioOpl** | **Integer** | Specifies the output protection level for compressed digital audio. |  [optional] |
|**compressedDigitalVideoOpl** | **Integer** | Specifies the output protection level for compressed digital video. |  [optional] |
|**digitalVideoOnlyContentRestriction** | **Boolean** | Enables the Image Constraint For Analog Component Video Restriction in the license. |  |
|**explicitAnalogTelevisionOutputRestriction** | [**ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction**](ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction.md) |  |  [optional] |
|**firstPlayExpiration** | **String** | The amount of time that the license is valid after the license is first used to play content. |  [optional] |
|**imageConstraintForAnalogComponentVideoRestriction** | **Boolean** | Enables the Image Constraint For Analog Component Video Restriction in the license. |  |
|**imageConstraintForAnalogComputerMonitorRestriction** | **Boolean** | Enables the Image Constraint For Analog Component Video Restriction in the license. |  |
|**scmsRestriction** | **Integer** | Configures the Serial Copy Management System (SCMS) in the license. Must be between 0 and 3 inclusive. |  [optional] |
|**uncompressedDigitalAudioOpl** | **Integer** | Specifies the output protection level for uncompressed digital audio. |  [optional] |
|**uncompressedDigitalVideoOpl** | **Integer** | Specifies the output protection level for uncompressed digital video. |  [optional] |



## Enum: AllowPassingVideoContentToUnknownOutputEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| NOT_ALLOWED | &quot;NotAllowed&quot; |
| ALLOWED | &quot;Allowed&quot; |
| ALLOWED_WITH_VIDEO_CONSTRICTION | &quot;AllowedWithVideoConstriction&quot; |



