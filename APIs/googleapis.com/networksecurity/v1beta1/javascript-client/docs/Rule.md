# NetworkSecurityApi.Rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | [**[Destination]**](Destination.md) | Optional. List of attributes for the traffic destination. All of the destinations must match. A destination is a match if a request matches all the specified hosts, ports, methods and headers. If not set, the action specified in the &#39;action&#39; field will be applied without any rule checks for the destination. | [optional] 
**sources** | [**[Source]**](Source.md) | Optional. List of attributes for the traffic source. All of the sources must match. A source is a match if both principals and ip_blocks match. If not set, the action specified in the &#39;action&#39; field will be applied without any rule checks for the source. | [optional] 


