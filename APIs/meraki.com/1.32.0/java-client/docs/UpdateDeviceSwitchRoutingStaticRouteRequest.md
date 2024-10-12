

# UpdateDeviceSwitchRoutingStaticRouteRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiseViaOspfEnabled** | **Boolean** | Option to advertise static route via OSPF |  [optional] |
|**name** | **String** | Name or description for layer 3 static route |  [optional] |
|**nextHopIp** | **String** | IP address of the next hop device to which the device sends its traffic for the subnet |  [optional] |
|**preferOverOspfRoutesEnabled** | **Boolean** | Option to prefer static route over OSPF routes |  [optional] |
|**subnet** | **String** | The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24) |  [optional] |



