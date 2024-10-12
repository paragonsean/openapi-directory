

# Edge

Information about a connection between two services. An edge can be a synchronous connection, such as typical call between client and service, or an asynchronous link, such as a Lambda function which retrieves an event from an SNS queue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**referenceId** | [**Integer**](Integer.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**summaryStatistics** | [**EdgeSummaryStatistics**](EdgeSummaryStatistics.md) |  |  [optional] |
|**responseTimeHistogram** | [**List**](List.md) |  |  [optional] |
|**aliases** | [**List**](List.md) |  |  [optional] |
|**edgeType** | [**String**](String.md) |  |  [optional] |
|**receivedEventAgeHistogram** | [**List**](List.md) |  |  [optional] |



