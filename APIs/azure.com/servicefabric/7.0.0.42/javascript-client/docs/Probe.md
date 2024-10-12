# ServiceFabricClientApis.Probe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exec** | [**ProbeExec**](ProbeExec.md) |  | [optional] 
**failureThreshold** | **Number** | The count of failures after which probe is considered failed. | [optional] 
**httpGet** | [**ProbeHttpGet**](ProbeHttpGet.md) |  | [optional] 
**initialDelaySeconds** | **Number** | The initial delay in seconds to start executing probe once code package has started. | [optional] 
**periodSeconds** | **Number** | Periodic seconds to execute probe. | [optional] 
**successThreshold** | **Number** | The count of successful probe executions after which probe is considered success. | [optional] 
**tcpSocket** | [**ProbeTcpSocket**](ProbeTcpSocket.md) |  | [optional] 
**timeoutSeconds** | **Number** | Period after which probe is considered as failed if it hasn&#39;t completed successfully. | [optional] 


