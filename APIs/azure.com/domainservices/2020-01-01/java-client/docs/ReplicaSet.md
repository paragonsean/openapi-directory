

# ReplicaSet

Replica Set Definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainControllerIpAddress** | **List&lt;String&gt;** | List of Domain Controller IP Address |  [optional] [readonly] |
|**externalAccessIpAddress** | **String** | External access ip address. |  [optional] [readonly] |
|**healthAlerts** | [**List&lt;HealthAlert&gt;**](HealthAlert.md) | List of Domain Health Alerts |  [optional] [readonly] |
|**healthLastEvaluated** | **OffsetDateTime** | Last domain evaluation run DateTime |  [optional] [readonly] |
|**healthMonitors** | [**List&lt;HealthMonitor&gt;**](HealthMonitor.md) | List of Domain Health Monitors |  [optional] [readonly] |
|**location** | **String** | Virtual network location |  [optional] |
|**replicaSetId** | **String** | ReplicaSet Id |  [optional] [readonly] |
|**serviceStatus** | **String** | Status of Domain Service instance |  [optional] [readonly] |
|**subnetId** | **String** | The name of the virtual network that Domain Services will be deployed on. The id of the subnet that Domain Services will be deployed on. /virtualNetwork/vnetName/subnets/subnetName. |  [optional] |
|**vnetSiteId** | **String** | Virtual network site id |  [optional] [readonly] |



