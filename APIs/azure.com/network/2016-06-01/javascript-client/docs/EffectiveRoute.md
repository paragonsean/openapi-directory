# NetworkManagementClient.EffectiveRoute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressPrefix** | **[String]** | Gets address prefixes of the effective routes in CIDR notation. | [optional] 
**name** | **String** | Gets the name of the user defined route. This is optional. | [optional] 
**nextHopIpAddress** | **[String]** | Gets the IP address of the next hop of the effective route | [optional] 
**nextHopType** | **String** | Gets or sets the type of Azure hop the packet should be sent to. | [optional] 
**source** | **String** | Gets who created the route | [optional] 
**state** | **String** | Gets value of effective route | [optional] 



## Enum: NextHopTypeEnum


* `VirtualNetworkGateway` (value: `"VirtualNetworkGateway"`)

* `VnetLocal` (value: `"VnetLocal"`)

* `Internet` (value: `"Internet"`)

* `VirtualAppliance` (value: `"VirtualAppliance"`)

* `None` (value: `"None"`)





## Enum: SourceEnum


* `Unknown` (value: `"Unknown"`)

* `User` (value: `"User"`)

* `VirtualNetworkGateway` (value: `"VirtualNetworkGateway"`)

* `Default` (value: `"Default"`)





## Enum: StateEnum


* `Active` (value: `"Active"`)

* `Invalid` (value: `"Invalid"`)




