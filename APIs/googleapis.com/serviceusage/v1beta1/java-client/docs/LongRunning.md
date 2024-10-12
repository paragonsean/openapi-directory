

# LongRunning

Describes settings to use when generating API methods that use the long-running operation pattern. All default values below are from those used in the client library generators (e.g. [Java](https://github.com/googleapis/gapic-generator-java/blob/04c2faa191a9b5a10b92392fe8482279c4404803/src/main/java/com/google/api/generator/gapic/composer/common/RetrySettingsComposer.java)).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**initialPollDelay** | **String** | Initial delay after which the first poll request will be made. Default value: 5 seconds. |  [optional] |
|**maxPollDelay** | **String** | Maximum time between two subsequent poll requests. Default value: 45 seconds. |  [optional] |
|**pollDelayMultiplier** | **Float** | Multiplier to gradually increase delay between subsequent polls until it reaches max_poll_delay. Default value: 1.5. |  [optional] |
|**totalPollTimeout** | **String** | Total polling timeout. Default value: 5 minutes. |  [optional] |



