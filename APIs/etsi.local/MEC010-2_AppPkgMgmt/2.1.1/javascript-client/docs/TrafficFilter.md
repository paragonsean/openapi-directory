# EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.TrafficFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dSCP** | **Number** | Used to match all IPv4 packets that have the same DSCP. | [optional] 
**dstAddress** | **[String]** | A IP address or a range of IP addresses.For IPv4, the IP address could be an IP address plus mask, or an individual IP address, or a range of IP addresses.For IPv6, the IP address could be an IP prefix, or a range of IP prefixes. | [optional] 
**dstPort** | **[String]** | A port or a range of ports. | [optional] 
**dstTunnelPort** | **[String]** | Used for GTP tunnel based traffic rule. | [optional] 
**protocol** | **[String]** | Specify the protocol of the traffic filter. | [optional] 
**qCI** | **Number** | Used to match all packets that have the same QCI. | [optional] 
**srcAddress** | **[String]** | An IP address or a range of IP addresses.For IPv4, the IP address could be an IP address plus mask, or an individual IP address, or a range of IP addresses.For IPv6, the IP address could be an IP prefix, or a range of IP prefixes. | [optional] 
**srcPort** | **[String]** | A port or a range of ports. | [optional] 
**srcTunnelAddress** | **[String]** | Used for GTP tunnel based traffic rule. | [optional] 
**srcTunnelPort** | **[String]** | Used for GTP tunnel based traffic rule. | [optional] 
**tC** | **Number** | Used to match all IPv6 packets that have the same TC. | [optional] 
**tag** | **[String]** | Used for tag based traffic rule. | [optional] 
**tgtTunnelAddress** | **[String]** | Used for GTP tunnel based traffic rule. | [optional] 


