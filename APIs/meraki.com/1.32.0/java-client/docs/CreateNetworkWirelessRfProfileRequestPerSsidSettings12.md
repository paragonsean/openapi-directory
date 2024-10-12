

# CreateNetworkWirelessRfProfileRequestPerSsidSettings12

Settings for SSID 12

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandOperationMode** | [**BandOperationModeEnum**](#BandOperationModeEnum) | Choice between &#39;dual&#39;, &#39;2.4ghz&#39; or &#39;5ghz&#39;. |  [optional] |
|**bandSteeringEnabled** | **Boolean** | Steers client to most open band between 2.4 GHz and 5 GHz. Can be either true or false. |  [optional] |
|**minBitrate** | **Float** | Sets min bitrate (Mbps) of this SSID. Can be one of &#39;1&#39;, &#39;2&#39;, &#39;5.5&#39;, &#39;6&#39;, &#39;9&#39;, &#39;11&#39;, &#39;12&#39;, &#39;18&#39;, &#39;24&#39;, &#39;36&#39;, &#39;48&#39; or &#39;54&#39;. |  [optional] |



## Enum: BandOperationModeEnum

| Name | Value |
|---- | -----|
| _2_4GHZ | &quot;2.4ghz&quot; |
| _5GHZ | &quot;5ghz&quot; |
| DUAL | &quot;dual&quot; |



