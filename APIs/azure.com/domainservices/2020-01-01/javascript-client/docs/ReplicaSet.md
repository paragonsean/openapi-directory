# DomainServicesResourceProvider.ReplicaSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainControllerIpAddress** | **[String]** | List of Domain Controller IP Address | [optional] [readonly] 
**externalAccessIpAddress** | **String** | External access ip address. | [optional] [readonly] 
**healthAlerts** | [**[HealthAlert]**](HealthAlert.md) | List of Domain Health Alerts | [optional] [readonly] 
**healthLastEvaluated** | **Date** | Last domain evaluation run DateTime | [optional] [readonly] 
**healthMonitors** | [**[HealthMonitor]**](HealthMonitor.md) | List of Domain Health Monitors | [optional] [readonly] 
**location** | **String** | Virtual network location | [optional] 
**replicaSetId** | **String** | ReplicaSet Id | [optional] [readonly] 
**serviceStatus** | **String** | Status of Domain Service instance | [optional] [readonly] 
**subnetId** | **String** | The name of the virtual network that Domain Services will be deployed on. The id of the subnet that Domain Services will be deployed on. /virtualNetwork/vnetName/subnets/subnetName. | [optional] 
**vnetSiteId** | **String** | Virtual network site id | [optional] [readonly] 


