

# GoogleCloudApigeeV1OptimizedStatsNode

Encapsulates a data node as represented below: ``` { \"identifier\": { \"names\": [ \"apiproxy\" ], \"values\": [ \"sirjee\" ] }, \"metric\": [ { \"env\": \"prod\", \"name\": \"sum(message_count)\", \"values\": [ 36.0 ] } ] }``` or ``` { \"env\": \"prod\", \"name\": \"sum(message_count)\", \"values\": [ 36.0 ] }``` Depending on whether a dimension is present in the query or not the data node type can be a simple metric value or dimension identifier with list of metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **List&lt;Object&gt;** |  |  [optional] |



