# MerakiDashboardApi.UpdateNetworkWirelessSsidRequestRadiusAccountingServersInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caCertificate** | **String** | Certificate used for authorization for the RADSEC Server | [optional] 
**host** | **String** | IP address to which the APs will send RADIUS accounting messages | 
**port** | **Number** | Port on the RADIUS server that is listening for accounting messages | [optional] 
**radsecEnabled** | **Boolean** | Use RADSEC (TLS over TCP) to connect to this RADIUS accounting server. Requires radiusProxyEnabled. | [optional] 
**secret** | **String** | Shared key used to authenticate messages between the APs and RADIUS server | [optional] 


