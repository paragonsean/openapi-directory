# AnthosOnPremApi.BareMetalBgpPeerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **String** | Required. BGP autonomous system number (ASN) for the network that contains the external peer device. | [optional] 
**controlPlaneNodes** | **[String]** | The IP address of the control plane node that connects to the external peer. If you don&#39;t specify any control plane nodes, all control plane nodes can connect to the external peer. If you specify one or more IP addresses, only the nodes specified participate in peering sessions. | [optional] 
**ipAddress** | **String** | Required. The IP address of the external peer device. | [optional] 


