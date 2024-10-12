

# PlaybackMetricCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**downloadedBytesHTTP** | **BigDecimal** | How many bytes were downloaded with HTTP since the last metric creation |  |
|**downloadedBytesP2P** | **BigDecimal** | How many bytes were downloaded with P2P since the last metric creation |  |
|**errors** | **BigDecimal** | How many errors occured since the last metric creation |  |
|**fps** | **BigDecimal** | Current player video fps |  [optional] |
|**playerMode** | [**PlayerModeEnum**](#PlayerModeEnum) |  |  |
|**resolution** | **BigDecimal** | Current player video resolution |  [optional] |
|**resolutionChanges** | **BigDecimal** | How many resolution changes occured since the last metric creation |  |
|**uploadedBytesP2P** | **BigDecimal** | How many bytes were uploaded with P2P since the last metric creation |  |
|**videoId** | [**GetLiveIdIdParameter**](GetLiveIdIdParameter.md) |  |  |



## Enum: PlayerModeEnum

| Name | Value |
|---- | -----|
| P2P_MEDIA_LOADER | &quot;p2p-media-loader&quot; |
| WEBTORRENT | &quot;webtorrent&quot; |



