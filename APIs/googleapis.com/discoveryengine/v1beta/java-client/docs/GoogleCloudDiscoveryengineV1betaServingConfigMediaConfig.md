

# GoogleCloudDiscoveryengineV1betaServingConfigMediaConfig

Specifies the configurations needed for Media Discovery. Currently we support: * `demote_content_watched`: Threshold for watched content demotion. Customers can specify if using watched content demotion or use viewed detail page. Using the content watched demotion, customers need to specify the watched minutes or percentage exceeds the threshold, the content will be demoted in the recommendation result. * `promote_fresh_content`: cutoff days for fresh content promotion. Customers can specify if using content freshness promotion. If the content was published within the cutoff days, the content will be promoted in the recommendation result. Can only be set if SolutionType is SOLUTION_TYPE_RECOMMENDATION.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentFreshnessCutoffDays** | **Integer** | Specifies the content freshness used for recommendation result. Contents will be demoted if contents were published for more than content freshness cutoff days. |  [optional] |
|**contentWatchedMinutesThreshold** | **Float** | Specifies the content watched minutes threshold for demotion. |  [optional] |
|**contentWatchedPercentageThreshold** | **Float** | Specifies the content watched percentage threshold for demotion. Threshold value must be between [0, 1.0] inclusive. |  [optional] |
|**contentWatchedSecondsThreshold** | **Float** | Specifies the content watched minutes threshold for demotion. |  [optional] |
|**demotionEventType** | **String** | Specifies the event type used for demoting recommendation result. Currently supported values: * &#x60;view-item&#x60;: Item viewed. * &#x60;media-play&#x60;: Start/resume watching a video, playing a song, etc. * &#x60;media-complete&#x60;: Finished or stopped midway through a video, song, etc. If unset, watch history demotion will not be applied. Content freshness demotion will still be applied. |  [optional] |



