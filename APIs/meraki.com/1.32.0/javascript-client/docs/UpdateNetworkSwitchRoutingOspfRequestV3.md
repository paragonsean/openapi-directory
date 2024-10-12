# MerakiDashboardApi.UpdateNetworkSwitchRoutingOspfRequestV3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areas** | [**[UpdateNetworkSwitchRoutingOspfRequestAreasInner]**](UpdateNetworkSwitchRoutingOspfRequestAreasInner.md) | OSPF v3 areas | [optional] 
**deadTimerInSeconds** | **Number** | Time interval to determine when the peer will be declared inactive/dead. Value must be between 1 and 65535 | [optional] 
**enabled** | **Boolean** | Boolean value to enable or disable V3 OSPF routing. OSPF V3 routing is disabled by default. | [optional] 
**helloTimerInSeconds** | **Number** | Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds. | [optional] 


