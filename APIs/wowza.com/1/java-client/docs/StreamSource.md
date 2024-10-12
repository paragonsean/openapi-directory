

# StreamSource


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupIpAddress** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;ip_address&lt;/strong&gt;, specify the backup IP address of the source encoder. |  [optional] |
|**backupUrl** | **String** | The backup RTMP playback URL of the transcoded stream. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time that the stream source was created. |  [optional] |
|**id** | **String** | The unique alphanumeric string that identifies the stream source. |  [optional] |
|**ipAddress** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;ip_address&lt;/strong&gt;, specify the primary IP address of the source encoder. |  [optional] |
|**location** | [**LocationEnum**](#LocationEnum) | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;region&lt;/strong&gt;, specify a location as close as possible to the source encoder. |  [optional] |
|**locationMethod** | [**LocationMethodEnum**](#LocationMethodEnum) | The method used to determine the location of the stream source, either by &lt;strong&gt;region&lt;/strong&gt; or based on the source encoder&#39;s &lt;strong&gt;ip_address&lt;/strong&gt;. |  [optional] |
|**name** | **String** | A descriptive name for the stream source. Maximum 255 characters. |  [optional] |
|**password** | **String** | The password that you can use to configure the source encoder to authenticate to the stream source. |  [optional] |
|**playbackUrl** | **String** | The full RTMP playback URL. |  [optional] |
|**primaryUrl** | **String** | The primary RTMP playback URL of the transcoded stream. |  [optional] |
|**provider** | **String** | The provider of the Wowza Streaming Cloud stream source. |  [optional] |
|**streamName** | **String** | The name of the stream that you can use to configure the source encoder to connect to the stream source. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time that the stream source was updated. |  [optional] |
|**username** | **String** | The username that you can use to configure the source encoder to authenticate to the stream source. |  [optional] |



## Enum: LocationEnum

| Name | Value |
|---- | -----|
| ASIA_PACIFIC_AUSTRALIA | &quot;asia_pacific_australia&quot; |
| ASIA_PACIFIC_JAPAN | &quot;asia_pacific_japan&quot; |
| ASIA_PACIFIC_SINGAPORE | &quot;asia_pacific_singapore&quot; |
| ASIA_PACIFIC_TAIWAN | &quot;asia_pacific_taiwan&quot; |
| EU_BELGIUM | &quot;eu_belgium&quot; |
| EU_GERMANY | &quot;eu_germany&quot; |
| EU_IRELAND | &quot;eu_ireland&quot; |
| SOUTH_AMERICA_BRAZIL | &quot;south_america_brazil&quot; |
| US_CENTRAL_IOWA | &quot;us_central_iowa&quot; |
| US_EAST_S_CAROLINA | &quot;us_east_s_carolina&quot; |
| US_EAST_VIRGINIA | &quot;us_east_virginia&quot; |
| US_WEST_CALIFORNIA | &quot;us_west_california&quot; |
| US_WEST_OREGON | &quot;us_west_oregon&quot; |



## Enum: LocationMethodEnum

| Name | Value |
|---- | -----|
| REGION | &quot;region&quot; |
| IP_ADDRESS | &quot;ip_address&quot; |



