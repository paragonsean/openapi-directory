# AwsGroundStation.CreateDataflowEndpointGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactPostPassDurationSeconds** | **Number** | Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a &lt;code&gt;POSTPASS&lt;/code&gt; state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the &lt;code&gt;POSTPASS&lt;/code&gt; state. | [optional] 
**contactPrePassDurationSeconds** | **Number** | Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a &lt;code&gt;PREPASS&lt;/code&gt; state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the &lt;code&gt;PREPASS&lt;/code&gt; state. | [optional] 
**endpointDetails** | [**[EndpointDetails]**](EndpointDetails.md) | Endpoint details of each endpoint in the dataflow endpoint group. | 
**tags** | **{String: String}** | Tags of a dataflow endpoint group. | [optional] 


