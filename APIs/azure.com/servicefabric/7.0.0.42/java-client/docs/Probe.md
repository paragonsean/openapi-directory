

# Probe

Probes have a number of fields that you can use to control their behavior.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exec** | [**ProbeExec**](ProbeExec.md) |  |  [optional] |
|**failureThreshold** | **Integer** | The count of failures after which probe is considered failed. |  [optional] |
|**httpGet** | [**ProbeHttpGet**](ProbeHttpGet.md) |  |  [optional] |
|**initialDelaySeconds** | **Integer** | The initial delay in seconds to start executing probe once code package has started. |  [optional] |
|**periodSeconds** | **Integer** | Periodic seconds to execute probe. |  [optional] |
|**successThreshold** | **Integer** | The count of successful probe executions after which probe is considered success. |  [optional] |
|**tcpSocket** | [**ProbeTcpSocket**](ProbeTcpSocket.md) |  |  [optional] |
|**timeoutSeconds** | **Integer** | Period after which probe is considered as failed if it hasn&#39;t completed successfully. |  [optional] |



