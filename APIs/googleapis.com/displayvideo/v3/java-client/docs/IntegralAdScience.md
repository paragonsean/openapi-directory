

# IntegralAdScience

Details of Integral Ad Science settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customSegmentId** | **List&lt;String&gt;** | The custom segment ID provided by Integral Ad Science. The ID must be between &#x60;1000001&#x60; and &#x60;1999999&#x60;, inclusive. |  [optional] |
|**displayViewability** | [**DisplayViewabilityEnum**](#DisplayViewabilityEnum) | Display Viewability section (applicable to display line items only). |  [optional] |
|**excludeUnrateable** | **Boolean** | Brand Safety - **Unrateable**. |  [optional] |
|**excludedAdFraudRisk** | [**ExcludedAdFraudRiskEnum**](#ExcludedAdFraudRiskEnum) | Ad Fraud settings. |  [optional] |
|**excludedAdultRisk** | [**ExcludedAdultRiskEnum**](#ExcludedAdultRiskEnum) | Brand Safety - **Adult content**. |  [optional] |
|**excludedAlcoholRisk** | [**ExcludedAlcoholRiskEnum**](#ExcludedAlcoholRiskEnum) | Brand Safety - **Alcohol**. |  [optional] |
|**excludedDrugsRisk** | [**ExcludedDrugsRiskEnum**](#ExcludedDrugsRiskEnum) | Brand Safety - **Drugs**. |  [optional] |
|**excludedGamblingRisk** | [**ExcludedGamblingRiskEnum**](#ExcludedGamblingRiskEnum) | Brand Safety - **Gambling**. |  [optional] |
|**excludedHateSpeechRisk** | [**ExcludedHateSpeechRiskEnum**](#ExcludedHateSpeechRiskEnum) | Brand Safety - **Hate speech**. |  [optional] |
|**excludedIllegalDownloadsRisk** | [**ExcludedIllegalDownloadsRiskEnum**](#ExcludedIllegalDownloadsRiskEnum) | Brand Safety - **Illegal downloads**. |  [optional] |
|**excludedOffensiveLanguageRisk** | [**ExcludedOffensiveLanguageRiskEnum**](#ExcludedOffensiveLanguageRiskEnum) | Brand Safety - **Offensive language**. |  [optional] |
|**excludedViolenceRisk** | [**ExcludedViolenceRiskEnum**](#ExcludedViolenceRiskEnum) | Brand Safety - **Violence**. |  [optional] |
|**traqScoreOption** | [**TraqScoreOptionEnum**](#TraqScoreOptionEnum) | True advertising quality (applicable to Display line items only). |  [optional] |
|**videoViewability** | [**VideoViewabilityEnum**](#VideoViewabilityEnum) | Video Viewability Section (applicable to video line items only). |  [optional] |



## Enum: DisplayViewabilityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PERFORMANCE_VIEWABILITY_UNSPECIFIED&quot; |
| _40 | &quot;PERFORMANCE_VIEWABILITY_40&quot; |
| _50 | &quot;PERFORMANCE_VIEWABILITY_50&quot; |
| _60 | &quot;PERFORMANCE_VIEWABILITY_60&quot; |
| _70 | &quot;PERFORMANCE_VIEWABILITY_70&quot; |



## Enum: ExcludedAdFraudRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SUSPICIOUS_ACTIVITY_UNSPECIFIED&quot; |
| HR | &quot;SUSPICIOUS_ACTIVITY_HR&quot; |
| HMR | &quot;SUSPICIOUS_ACTIVITY_HMR&quot; |



## Enum: ExcludedAdultRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ADULT_UNSPECIFIED&quot; |
| HR | &quot;ADULT_HR&quot; |
| HMR | &quot;ADULT_HMR&quot; |



## Enum: ExcludedAlcoholRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ALCOHOL_UNSPECIFIED&quot; |
| HR | &quot;ALCOHOL_HR&quot; |
| HMR | &quot;ALCOHOL_HMR&quot; |



## Enum: ExcludedDrugsRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DRUGS_UNSPECIFIED&quot; |
| HR | &quot;DRUGS_HR&quot; |
| HMR | &quot;DRUGS_HMR&quot; |



## Enum: ExcludedGamblingRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;GAMBLING_UNSPECIFIED&quot; |
| HR | &quot;GAMBLING_HR&quot; |
| HMR | &quot;GAMBLING_HMR&quot; |



## Enum: ExcludedHateSpeechRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;HATE_SPEECH_UNSPECIFIED&quot; |
| HR | &quot;HATE_SPEECH_HR&quot; |
| HMR | &quot;HATE_SPEECH_HMR&quot; |



## Enum: ExcludedIllegalDownloadsRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ILLEGAL_DOWNLOADS_UNSPECIFIED&quot; |
| HR | &quot;ILLEGAL_DOWNLOADS_HR&quot; |
| HMR | &quot;ILLEGAL_DOWNLOADS_HMR&quot; |



## Enum: ExcludedOffensiveLanguageRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OFFENSIVE_LANGUAGE_UNSPECIFIED&quot; |
| HR | &quot;OFFENSIVE_LANGUAGE_HR&quot; |
| HMR | &quot;OFFENSIVE_LANGUAGE_HMR&quot; |



## Enum: ExcludedViolenceRiskEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIOLENCE_UNSPECIFIED&quot; |
| HR | &quot;VIOLENCE_HR&quot; |
| HMR | &quot;VIOLENCE_HMR&quot; |



## Enum: TraqScoreOptionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TRAQ_UNSPECIFIED&quot; |
| _250 | &quot;TRAQ_250&quot; |
| _500 | &quot;TRAQ_500&quot; |
| _600 | &quot;TRAQ_600&quot; |
| _700 | &quot;TRAQ_700&quot; |
| _750 | &quot;TRAQ_750&quot; |
| _875 | &quot;TRAQ_875&quot; |
| _1000 | &quot;TRAQ_1000&quot; |



## Enum: VideoViewabilityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIDEO_VIEWABILITY_UNSPECIFIED&quot; |
| _40 | &quot;VIDEO_VIEWABILITY_40&quot; |
| _50 | &quot;VIDEO_VIEWABILITY_50&quot; |
| _60 | &quot;VIDEO_VIEWABILITY_60&quot; |
| _70 | &quot;VIDEO_VIEWABILITY_70&quot; |



