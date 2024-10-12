# TimeSeriesInsightsClient.Availability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribution** | **Object** |  | [optional] 
**intervalSize** | **String** | Interval size for the returned distribution of the events. Returned interval is selected to return a reasonable number of points. All intervals are the same size. On the wire interval is specified in ISO-8601 duration format. One month is always converted to 30 days, and one year is always 365 days. Examples: 1 minute is \&quot;PT1M\&quot;, 1 millisecond is \&quot;PT0.001S\&quot;. For more information, see https://www.w3.org/TR/xmlschema-2/#duration | [optional] [readonly] 
**range** | [**DateTimeRange**](DateTimeRange.md) |  | [optional] 


