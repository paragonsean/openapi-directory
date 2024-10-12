

# LogsPanel

A widget that displays a stream of log.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **String** | A filter that chooses which log entries to return. See Advanced Logs Queries (https://cloud.google.com/logging/docs/view/advanced-queries). Only log entries that match the filter are returned. An empty filter matches all log entries. |  [optional] |
|**resourceNames** | **List&lt;String&gt;** | The names of logging resources to collect logs for. Currently only projects are supported. If empty, the widget will default to the host project. |  [optional] |



