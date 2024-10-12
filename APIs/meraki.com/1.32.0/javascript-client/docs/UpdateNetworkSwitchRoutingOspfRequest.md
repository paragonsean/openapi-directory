# MerakiDashboardApi.UpdateNetworkSwitchRoutingOspfRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areas** | [**[UpdateNetworkSwitchRoutingOspfRequestAreasInner]**](UpdateNetworkSwitchRoutingOspfRequestAreasInner.md) | OSPF areas | [optional] 
**deadTimerInSeconds** | **Number** | Time interval to determine when the peer will be declared inactive/dead. Value must be between 1 and 65535 | [optional] 
**enabled** | **Boolean** | Boolean value to enable or disable OSPF routing. OSPF routing is disabled by default. | [optional] 
**helloTimerInSeconds** | **Number** | Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds. | [optional] 
**md5AuthenticationEnabled** | **Boolean** | Boolean value to enable or disable MD5 authentication. MD5 authentication is disabled by default. | [optional] 
**md5AuthenticationKey** | [**UpdateNetworkSwitchRoutingOspfRequestMd5AuthenticationKey**](UpdateNetworkSwitchRoutingOspfRequestMd5AuthenticationKey.md) |  | [optional] 
**v3** | [**UpdateNetworkSwitchRoutingOspfRequestV3**](UpdateNetworkSwitchRoutingOspfRequestV3.md) |  | [optional] 


