

# PutPlaybackConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adDecisionServerUrl** | **String** | The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters. |  [optional] |
|**availSuppression** | [**PutPlaybackConfigurationRequestAvailSuppression**](PutPlaybackConfigurationRequestAvailSuppression.md) |  |  [optional] |
|**bumper** | [**PutPlaybackConfigurationRequestBumper**](PutPlaybackConfigurationRequestBumper.md) |  |  [optional] |
|**cdnConfiguration** | [**PutPlaybackConfigurationRequestCdnConfiguration**](PutPlaybackConfigurationRequestCdnConfiguration.md) |  |  [optional] |
|**configurationAliases** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | The predefined aliases for dynamic variables. |  [optional] |
|**dashConfiguration** | [**PutPlaybackConfigurationRequestDashConfiguration**](PutPlaybackConfigurationRequestDashConfiguration.md) |  |  [optional] |
|**livePreRollConfiguration** | [**PutPlaybackConfigurationRequestLivePreRollConfiguration**](PutPlaybackConfigurationRequestLivePreRollConfiguration.md) |  |  [optional] |
|**manifestProcessingRules** | [**PutPlaybackConfigurationRequestManifestProcessingRules**](PutPlaybackConfigurationRequestManifestProcessingRules.md) |  |  [optional] |
|**name** | **String** | The identifier for the playback configuration. |  |
|**personalizationThresholdSeconds** | **Integer** | Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to &lt;i&gt;ad replacement&lt;/i&gt; in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html\&quot;&gt;Ad Behavior in AWS Elemental MediaTailor&lt;/a&gt;. |  [optional] |
|**slateAdUrl** | **String** | The URL for a high-quality video asset to transcode and use to fill in time that&#39;s not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\&quot;&gt;Tagging AWS Elemental MediaTailor Resources&lt;/a&gt;. |  [optional] |
|**transcodeProfileName** | **String** | The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support. |  [optional] |
|**videoContentSourceUrl** | **String** | The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters. |  [optional] |



