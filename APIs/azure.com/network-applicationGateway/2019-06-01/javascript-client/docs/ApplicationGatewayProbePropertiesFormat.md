# NetworkManagementClient.ApplicationGatewayProbePropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **String** | Host name to send the probe to. | [optional] 
**interval** | **Number** | The probing interval in seconds. This is the time interval between two consecutive probes. Acceptable values are from 1 second to 86400 seconds. | [optional] 
**match** | [**ApplicationGatewayProbeHealthResponseMatch**](ApplicationGatewayProbeHealthResponseMatch.md) |  | [optional] 
**minServers** | **Number** | Minimum number of servers that are always marked healthy. Default value is 0. | [optional] 
**path** | **String** | Relative path of probe. Valid path starts from &#39;/&#39;. Probe is sent to &lt;Protocol&gt;://&lt;host&gt;:&lt;port&gt;&lt;path&gt;. | [optional] 
**pickHostNameFromBackendHttpSettings** | **Boolean** | Whether the host header should be picked from the backend http settings. Default value is false. | [optional] 
**port** | **Number** | Custom port which will be used for probing the backend servers. The valid value ranges from 1 to 65535. In case not set, port from http settings will be used. This property is valid for Standard_v2 and WAF_v2 only. | [optional] 
**protocol** | [**ApplicationGatewayProtocol**](ApplicationGatewayProtocol.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the backend http settings resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**timeout** | **Number** | The probe timeout in seconds. Probe marked as failed if valid response is not received with this timeout period. Acceptable values are from 1 second to 86400 seconds. | [optional] 
**unhealthyThreshold** | **Number** | The probe retry count. Backend server is marked down after consecutive probe failure count reaches UnhealthyThreshold. Acceptable values are from 1 second to 20. | [optional] 


