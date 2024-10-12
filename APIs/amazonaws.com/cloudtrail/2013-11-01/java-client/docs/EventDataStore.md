

# EventDataStore

A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 90 to 2557 days (about three months to up to seven years). To select events for an event data store, use <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced\">advanced event selectors</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventDataStoreArn** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**terminationProtectionEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**status** | [**EventDataStoreStatus**](EventDataStoreStatus.md) |  |  [optional] |
|**advancedEventSelectors** | [**List**](List.md) |  |  [optional] |
|**multiRegionEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**organizationEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**retentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**createdTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**updatedTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



