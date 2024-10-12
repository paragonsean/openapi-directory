

# TranscoderProperty


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The key of the property. For &lt;strong&gt;rtsp&lt;/strong&gt;, valid values are &lt;strong&gt;debugRtspSession&lt;/strong&gt;, &lt;strong&gt;maxRtcpWaitTime&lt;/strong&gt;, &lt;strong&gt;avSyncMethod&lt;/strong&gt;, &lt;strong&gt;rtspValidationFrequency&lt;/strong&gt;, &lt;strong&gt;rtpTransportMode&lt;/strong&gt;, &lt;strong&gt;rtspFilterUnknownTracks&lt;/strong&gt;, &lt;strong&gt;rtpIgnoreSpropParameterSets&lt;/strong&gt;, and &lt;strong&gt;rtpIgnoreProfileLevelId&lt;/strong&gt;. For &lt;strong&gt;cupertino&lt;/strong&gt;, valid values are &lt;strong&gt;cupertinoEnableProgramDateTime&lt;/strong&gt;, &lt;strong&gt;cupertinoEnableId3ProgramDateTime&lt;/strong&gt;, and &lt;strong&gt;cupertinoProgramDateTimeOffset&lt;/strong&gt;. |  [optional] |
|**section** | **String** | The section of the transcoder configuration table that contains the property. Valid values are &lt;strong&gt;rtsp&lt;/strong&gt; and &lt;strong&gt;cupertino&lt;/strong&gt;. |  [optional] |
|**transcoderId** | **String** | The unique alphanumeric string that identifies the transcoder. |  [optional] |
|**value** | **String** | The value of the property. For &lt;strong&gt;debugRtspSession&lt;/strong&gt;, &lt;strong&gt;avSyncMethod&lt;/strong&gt;, &lt;strong&gt;rtspFilterUnknownTracks&lt;/strong&gt;, &lt;strong&gt;rtpIgnoreSpropParameterSets&lt;/strong&gt;, &lt;strong&gt;rtpIgnoreProfileLevelId&lt;/strong&gt;, &lt;strong&gt;cupertinoEnableProgramDateTime&lt;/strong&gt;, and &lt;strong&gt;cupertinoEnableId3ProgramDateTime&lt;/strong&gt;, valid values are &lt;strong&gt;true&lt;/strong&gt; or &lt;strong&gt;false&lt;/strong&gt;. &lt;strong&gt;maxRtcpWaitTime&lt;/strong&gt; must be &lt;strong&gt;0&lt;/strong&gt; (ms, off) or greater. The default is &lt;strong&gt;2000&lt;/strong&gt;. Valid values for &lt;strong&gt;rtpTransportMode&lt;/strong&gt; are &lt;strong&gt;udp&lt;/strong&gt; or &lt;strong&gt;interleave&lt;/strong&gt; (the default). &lt;strong&gt;rtspValidationFrequency&lt;/strong&gt; must be &lt;strong&gt;0&lt;/strong&gt; (ms, off) or greater. The default is &lt;strong&gt;15000&lt;/strong&gt;. &lt;strong&gt;cupertinoProgramDateTimeOffset&lt;/strong&gt; must be an integer, positive or negative. The default is &lt;strong&gt;0&lt;/strong&gt; (ms). |  [optional] |



