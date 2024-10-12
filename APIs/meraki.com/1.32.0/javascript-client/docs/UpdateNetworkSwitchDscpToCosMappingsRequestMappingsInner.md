# MerakiDashboardApi.UpdateNetworkSwitchDscpToCosMappingsRequestMappingsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cos** | **Number** | The actual layer-2 CoS queue the DSCP value is mapped to. These are not bits set on outgoing frames. Value can be in the range of 0 to 5 inclusive. | 
**dscp** | **Number** | The Differentiated Services Code Point (DSCP) tag in the IP header that will be mapped to a particular Class-of-Service (CoS) queue. Value can be in the range of 0 to 63 inclusive. | 
**title** | **String** | Label for the mapping (optional). | [optional] 


