# CloudMonitoringApi.BasicSli

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | **Object** | Future parameters for the availability SLI. | [optional] 
**latency** | [**LatencyCriteria**](LatencyCriteria.md) |  | [optional] 
**location** | **[String]** | OPTIONAL: The set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don&#39;t support breaking down by location, setting this field will result in an error. | [optional] 
**method** | **[String]** | OPTIONAL: The set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service&#39;s methods. For service types that don&#39;t support breaking down by method, setting this field will result in an error. | [optional] 
**version** | **[String]** | OPTIONAL: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don&#39;t support breaking down by version, setting this field will result in an error. | [optional] 


