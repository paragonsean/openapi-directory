

# CreateDataflowEndpointGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactPostPassDurationSeconds** | **Integer** | Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a &lt;code&gt;POSTPASS&lt;/code&gt; state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the &lt;code&gt;POSTPASS&lt;/code&gt; state. |  [optional] |
|**contactPrePassDurationSeconds** | **Integer** | Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a &lt;code&gt;PREPASS&lt;/code&gt; state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the &lt;code&gt;PREPASS&lt;/code&gt; state. |  [optional] |
|**endpointDetails** | [**List&lt;EndpointDetails&gt;**](EndpointDetails.md) | Endpoint details of each endpoint in the dataflow endpoint group. |  |
|**tags** | **Map&lt;String, String&gt;** | Tags of a dataflow endpoint group. |  [optional] |



