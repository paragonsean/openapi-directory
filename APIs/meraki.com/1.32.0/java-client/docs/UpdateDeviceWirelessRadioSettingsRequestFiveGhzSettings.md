

# UpdateDeviceWirelessRadioSettingsRequestFiveGhzSettings

Manual radio settings for 5 GHz.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | Sets a manual channel for 5 GHz. Can be &#39;36&#39;, &#39;40&#39;, &#39;44&#39;, &#39;48&#39;, &#39;52&#39;, &#39;56&#39;, &#39;60&#39;, &#39;64&#39;, &#39;100&#39;, &#39;104&#39;, &#39;108&#39;, &#39;112&#39;, &#39;116&#39;, &#39;120&#39;, &#39;124&#39;, &#39;128&#39;, &#39;132&#39;, &#39;136&#39;, &#39;140&#39;, &#39;144&#39;, &#39;149&#39;, &#39;153&#39;, &#39;157&#39;, &#39;161&#39;, &#39;165&#39;, &#39;169&#39;, &#39;173&#39; or &#39;177&#39; or null for using auto channel. |  [optional] |
|**channelWidth** | [**ChannelWidthEnum**](#ChannelWidthEnum) | Sets a manual channel for 5 GHz. Can be &#39;0&#39;, &#39;20&#39;, &#39;40&#39;, &#39;80&#39; or &#39;160&#39; or null for using auto channel width. |  [optional] |
|**targetPower** | **Integer** | Set a manual target power for 5 GHz. Can be between &#39;8&#39; or &#39;30&#39; or null for using auto power range. |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| NUMBER_36 | 36 |
| NUMBER_40 | 40 |
| NUMBER_44 | 44 |
| NUMBER_48 | 48 |
| NUMBER_52 | 52 |
| NUMBER_56 | 56 |
| NUMBER_60 | 60 |
| NUMBER_64 | 64 |
| NUMBER_100 | 100 |
| NUMBER_104 | 104 |
| NUMBER_108 | 108 |
| NUMBER_112 | 112 |
| NUMBER_116 | 116 |
| NUMBER_120 | 120 |
| NUMBER_124 | 124 |
| NUMBER_128 | 128 |
| NUMBER_132 | 132 |
| NUMBER_136 | 136 |
| NUMBER_140 | 140 |
| NUMBER_144 | 144 |
| NUMBER_149 | 149 |
| NUMBER_153 | 153 |
| NUMBER_157 | 157 |
| NUMBER_161 | 161 |
| NUMBER_165 | 165 |
| NUMBER_169 | 169 |
| NUMBER_173 | 173 |
| NUMBER_177 | 177 |



## Enum: ChannelWidthEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_20 | 20 |
| NUMBER_40 | 40 |
| NUMBER_80 | 80 |
| NUMBER_160 | 160 |



