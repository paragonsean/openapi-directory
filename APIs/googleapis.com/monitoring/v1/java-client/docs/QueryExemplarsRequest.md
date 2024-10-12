

# QueryExemplarsRequest

QueryExemplarsRequest holds all parameters of the Prometheus upstream API for querying exemplars.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**end** | **String** | The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp. |  [optional] |
|**query** | **String** | A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/. |  [optional] |
|**start** | **String** | The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp. |  [optional] |



