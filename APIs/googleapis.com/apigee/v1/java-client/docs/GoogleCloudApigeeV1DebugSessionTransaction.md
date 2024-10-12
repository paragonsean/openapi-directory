

# GoogleCloudApigeeV1DebugSessionTransaction

A transaction contains all of the debug information of the entire message flow of an API call processed by the runtime plane. The information is collected and recorded at critical points of the message flow in the runtime apiproxy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completed** | **Boolean** | Flag indicating whether a transaction is completed or not |  [optional] |
|**point** | [**List&lt;GoogleCloudApigeeV1Point&gt;**](GoogleCloudApigeeV1Point.md) | List of debug data collected by runtime plane at various defined points in the flow. |  [optional] |



