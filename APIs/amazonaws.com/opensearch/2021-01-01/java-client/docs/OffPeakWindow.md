

# OffPeakWindow

<p>A custom 10-hour, low-traffic window during which OpenSearch Service can perform mandatory configuration changes on the domain. These actions can include scheduled service software updates and blue/green Auto-Tune enhancements. OpenSearch Service will schedule these actions during the window that you specify.</p> <p>If you don't specify a window start time, it defaults to 10:00 P.M. local time.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html\">Defining off-peak maintenance windows for Amazon OpenSearch Service</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**windowStartTime** | [**OffPeakWindowWindowStartTime**](OffPeakWindowWindowStartTime.md) |  |  [optional] |



