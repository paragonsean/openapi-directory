# AmazonDevOpsGuru.DescribeOrganizationOverviewRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fromTime** | **Date** |  The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day.  | 
**toTime** | **Date** |  The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used.  | [optional] 
**accountIds** | **[String]** | The ID of the Amazon Web Services account. | [optional] 
**organizationalUnitIds** | **[String]** | The ID of the organizational unit. | [optional] 


