

# UpdateNetworkWirelessRfProfileRequestFiveGhzSettings

Settings related to 5Ghz band

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelWidth** | **String** | Sets channel width (MHz) for 5Ghz band. Can be one of &#39;auto&#39;, &#39;20&#39;, &#39;40&#39; or &#39;80&#39;. |  [optional] |
|**maxPower** | **Integer** | Sets max power (dBm) of 5Ghz band. Can be integer between 2 and 30. |  [optional] |
|**minBitrate** | **Integer** | Sets min bitrate (Mbps) of 5Ghz band. Can be one of &#39;6&#39;, &#39;9&#39;, &#39;12&#39;, &#39;18&#39;, &#39;24&#39;, &#39;36&#39;, &#39;48&#39; or &#39;54&#39;. |  [optional] |
|**minPower** | **Integer** | Sets min power (dBm) of 5Ghz band. Can be integer between 2 and 30. |  [optional] |
|**rxsop** | **Integer** | The RX-SOP level controls the sensitivity of the radio. It is strongly recommended to use RX-SOP only after consulting a wireless expert. RX-SOP can be configured in the range of -65 to -95 (dBm). A value of null will reset this to the default. |  [optional] |
|**validAutoChannels** | **List&lt;Integer&gt;** | Sets valid auto channels for 5Ghz band. Can be one of &#39;36&#39;, &#39;40&#39;, &#39;44&#39;, &#39;48&#39;, &#39;52&#39;, &#39;56&#39;, &#39;60&#39;, &#39;64&#39;, &#39;100&#39;, &#39;104&#39;, &#39;108&#39;, &#39;112&#39;, &#39;116&#39;, &#39;120&#39;, &#39;124&#39;, &#39;128&#39;, &#39;132&#39;, &#39;136&#39;, &#39;140&#39;, &#39;144&#39;, &#39;149&#39;, &#39;153&#39;, &#39;157&#39;, &#39;161&#39; or &#39;165&#39;. |  [optional] |



