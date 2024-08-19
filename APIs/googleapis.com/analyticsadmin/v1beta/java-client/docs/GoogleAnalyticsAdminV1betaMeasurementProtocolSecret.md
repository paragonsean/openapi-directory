

# GoogleAnalyticsAdminV1betaMeasurementProtocolSecret

A secret value used for sending hits to Measurement Protocol.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Required. Human-readable display name for this secret. |  [optional] |
|**name** | **String** | Output only. Resource name of this secret. This secret may be a child of any type of stream. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret} |  [optional] [readonly] |
|**secretValue** | **String** | Output only. The measurement protocol secret value. Pass this value to the api_secret field of the Measurement Protocol API when sending hits to this secret&#39;s parent property. |  [optional] [readonly] |



