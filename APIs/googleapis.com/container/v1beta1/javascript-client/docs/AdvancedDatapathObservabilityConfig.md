# KubernetesEngineApi.AdvancedDatapathObservabilityConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableMetrics** | **Boolean** | Expose flow metrics on nodes | [optional] 
**enableRelay** | **Boolean** | Enable Relay component | [optional] 
**relayMode** | **String** | Method used to make Relay available | [optional] 



## Enum: RelayModeEnum


* `RELAY_MODE_UNSPECIFIED` (value: `"RELAY_MODE_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `INTERNAL_VPC_LB` (value: `"INTERNAL_VPC_LB"`)

* `EXTERNAL_LB` (value: `"EXTERNAL_LB"`)




