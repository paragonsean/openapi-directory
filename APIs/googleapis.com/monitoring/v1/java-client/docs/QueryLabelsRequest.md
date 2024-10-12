

# QueryLabelsRequest

QueryLabelsRequest holds all parameters of the Prometheus upstream API for returning a list of label names.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**end** | **String** | The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp. |  [optional] |
|**match** | **String** | A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them. |  [optional] |
|**start** | **String** | The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp. |  [optional] |



