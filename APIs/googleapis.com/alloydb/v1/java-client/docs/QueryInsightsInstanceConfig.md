

# QueryInsightsInstanceConfig

QueryInsights Instance specific configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**queryPlansPerMinute** | **Integer** | Number of query execution plans captured by Insights per minute for all queries combined. The default value is 5. Any integer between 0 and 20 is considered valid. |  [optional] |
|**queryStringLength** | **Integer** | Query string length. The default value is 1024. Any integer between 256 and 4500 is considered valid. |  [optional] |
|**recordApplicationTags** | **Boolean** | Record application tags for an instance. This flag is turned \&quot;on\&quot; by default. |  [optional] |
|**recordClientAddress** | **Boolean** | Record client address for an instance. Client address is PII information. This flag is turned \&quot;on\&quot; by default. |  [optional] |



