

# ApplicationGatewayOnDemandProbe

Details of on demand test probe request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddressPool** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**backendHttpSettings** | [**ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet**](ApplicationGatewayPathRulePropertiesFormatRewriteRuleSet.md) |  |  [optional] |
|**host** | **String** | Host name to send the probe to. |  [optional] |
|**match** | [**ApplicationGatewayProbeHealthResponseMatch**](ApplicationGatewayProbeHealthResponseMatch.md) |  |  [optional] |
|**path** | **String** | Relative path of probe. Valid path starts from &#39;/&#39;. Probe is sent to &lt;Protocol&gt;://&lt;host&gt;:&lt;port&gt;&lt;path&gt; |  [optional] |
|**pickHostNameFromBackendHttpSettings** | **Boolean** | Whether the host header should be picked from the backend http settings. Default value is false. |  [optional] |
|**protocol** | **ApplicationGatewayProtocol** |  |  [optional] |
|**timeout** | **Integer** | The probe timeout in seconds. Probe marked as failed if valid response is not received with this timeout period. Acceptable values are from 1 second to 86400 seconds. |  [optional] |



