

# OrganizationEvent

Summary information about an event, returned by the <a href=\"https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html\">DescribeEventsForOrganization</a> operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**service** | [**String**](String.md) |  |  [optional] |
|**eventTypeCode** | [**String**](String.md) |  |  [optional] |
|**eventTypeCategory** | [**EventTypeCategory**](EventTypeCategory.md) |  |  [optional] |
|**eventScopeCode** | [**EventScopeCode**](EventScopeCode.md) |  |  [optional] |
|**region** | [**String**](String.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**statusCode** | [**EventStatusCode**](EventStatusCode.md) |  |  [optional] |



