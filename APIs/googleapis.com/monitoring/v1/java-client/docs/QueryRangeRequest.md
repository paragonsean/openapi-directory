

# QueryRangeRequest

QueryRangeRequest holds all parameters of the Prometheus upstream range query API plus GCM specific parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**end** | **String** | The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp. |  [optional] |
|**query** | **String** | A PromQL query string. Query lanauge documentation: https://prometheus.io/docs/prometheus/latest/querying/basics/. |  [optional] |
|**start** | **String** | The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp. |  [optional] |
|**step** | **String** | The resolution of query result. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field. |  [optional] |
|**timeout** | **String** | An upper bound timeout for the query. Either a Prometheus duration string (https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field. |  [optional] |



