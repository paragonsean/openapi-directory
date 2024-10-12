

# AutoTuneMaintenanceSchedule

<note> <p>This object is deprecated. Use the domain's <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html\">off-peak window</a> to schedule Auto-Tune optimizations. For migration instructions, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html#off-peak-migrate\">Migrating from Auto-Tune maintenance windows</a>.</p> </note> <p>The Auto-Tune maintenance schedule. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/auto-tune.html\">Auto-Tune for Amazon OpenSearch Service</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**duration** | [**AutoTuneMaintenanceScheduleDuration**](AutoTuneMaintenanceScheduleDuration.md) |  |  [optional] |
|**cronExpressionForRecurrence** | [**String**](String.md) |  |  [optional] |



