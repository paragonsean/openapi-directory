

# DescribeOrganizationOverviewRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromTime** | **OffsetDateTime** |  The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day.  |  |
|**toTime** | **OffsetDateTime** |  The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used.  |  [optional] |
|**accountIds** | **List&lt;String&gt;** | The ID of the Amazon Web Services account. |  [optional] |
|**organizationalUnitIds** | **List&lt;String&gt;** | The ID of the organizational unit. |  [optional] |



