# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaServingConfigMediaConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentFreshnessCutoffDays** | **Number** | Specifies the content freshness used for recommendation result. Contents will be demoted if contents were published for more than content freshness cutoff days. | [optional] 
**contentWatchedMinutesThreshold** | **Number** | Specifies the content watched minutes threshold for demotion. | [optional] 
**contentWatchedPercentageThreshold** | **Number** | Specifies the content watched percentage threshold for demotion. Threshold value must be between [0, 1.0] inclusive. | [optional] 
**contentWatchedSecondsThreshold** | **Number** | Specifies the content watched minutes threshold for demotion. | [optional] 
**demotionEventType** | **String** | Specifies the event type used for demoting recommendation result. Currently supported values: * &#x60;view-item&#x60;: Item viewed. * &#x60;media-play&#x60;: Start/resume watching a video, playing a song, etc. * &#x60;media-complete&#x60;: Finished or stopped midway through a video, song, etc. If unset, watch history demotion will not be applied. Content freshness demotion will still be applied. | [optional] 


