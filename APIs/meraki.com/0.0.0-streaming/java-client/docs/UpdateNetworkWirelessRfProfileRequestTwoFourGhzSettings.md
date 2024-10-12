

# UpdateNetworkWirelessRfProfileRequestTwoFourGhzSettings

Settings related to 2.4Ghz band

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**axEnabled** | **Boolean** | Determines whether ax radio on 2.4Ghz band is on or off. Can be either true or false. If false, we highly recommend disabling band steering. |  [optional] |
|**maxPower** | **Integer** | Sets max power (dBm) of 2.4Ghz band. Can be integer between 2 and 30. |  [optional] |
|**minBitrate** | **Float** | Sets min bitrate (Mbps) of 2.4Ghz band. Can be one of &#39;1&#39;, &#39;2&#39;, &#39;5.5&#39;, &#39;6&#39;, &#39;9&#39;, &#39;11&#39;, &#39;12&#39;, &#39;18&#39;, &#39;24&#39;, &#39;36&#39;, &#39;48&#39; or &#39;54&#39;. |  [optional] |
|**minPower** | **Integer** | Sets min power (dBm) of 2.4Ghz band. Can be integer between 2 and 30. |  [optional] |
|**rxsop** | **Integer** | The RX-SOP level controls the sensitivity of the radio. It is strongly recommended to use RX-SOP only after consulting a wireless expert. RX-SOP can be configured in the range of -65 to -95 (dBm). A value of null will reset this to the default. |  [optional] |
|**validAutoChannels** | **List&lt;Integer&gt;** | Sets valid auto channels for 2.4Ghz band. Can be one of &#39;1&#39;, &#39;6&#39; or &#39;11&#39;. |  [optional] |



