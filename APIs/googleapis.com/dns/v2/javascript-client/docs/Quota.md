# CloudDnsApi.Quota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsKeysPerManagedZone** | **Number** | Maximum allowed number of DnsKeys per ManagedZone. | [optional] 
**gkeClustersPerManagedZone** | **Number** | Maximum allowed number of GKE clusters to which a privately scoped zone can be attached. | [optional] 
**gkeClustersPerPolicy** | **Number** | Maximum allowed number of GKE clusters per policy. | [optional] 
**gkeClustersPerResponsePolicy** | **Number** | Maximum allowed number of GKE clusters per response policy. | [optional] 
**itemsPerRoutingPolicy** | **Number** | Maximum allowed number of items per routing policy. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#quota&#39;]
**managedZones** | **Number** | Maximum allowed number of managed zones in the project. | [optional] 
**managedZonesPerGkeCluster** | **Number** | Maximum allowed number of managed zones which can be attached to a GKE cluster. | [optional] 
**managedZonesPerNetwork** | **Number** | Maximum allowed number of managed zones which can be attached to a network. | [optional] 
**nameserversPerDelegation** | **Number** | Maximum number of nameservers per delegation, meant to prevent abuse | [optional] 
**networksPerManagedZone** | **Number** | Maximum allowed number of networks to which a privately scoped zone can be attached. | [optional] 
**networksPerPolicy** | **Number** | Maximum allowed number of networks per policy. | [optional] 
**networksPerResponsePolicy** | **Number** | Maximum allowed number of networks per response policy. | [optional] 
**peeringZonesPerTargetNetwork** | **Number** | Maximum allowed number of consumer peering zones per target network owned by this producer project | [optional] 
**policies** | **Number** | Maximum allowed number of policies per project. | [optional] 
**resourceRecordsPerRrset** | **Number** | Maximum allowed number of ResourceRecords per ResourceRecordSet. | [optional] 
**responsePolicies** | **Number** | Maximum allowed number of response policies per project. | [optional] 
**responsePolicyRulesPerResponsePolicy** | **Number** | Maximum allowed number of rules per response policy. | [optional] 
**rrsetAdditionsPerChange** | **Number** | Maximum allowed number of ResourceRecordSets to add per ChangesCreateRequest. | [optional] 
**rrsetDeletionsPerChange** | **Number** | Maximum allowed number of ResourceRecordSets to delete per ChangesCreateRequest. | [optional] 
**rrsetsPerManagedZone** | **Number** | Maximum allowed number of ResourceRecordSets per zone in the project. | [optional] 
**targetNameServersPerManagedZone** | **Number** | Maximum allowed number of target name servers per managed forwarding zone. | [optional] 
**targetNameServersPerPolicy** | **Number** | Maximum allowed number of alternative target name servers per policy. | [optional] 
**totalRrdataSizePerChange** | **Number** | Maximum allowed size for total rrdata in one ChangesCreateRequest in bytes. | [optional] 
**whitelistedKeySpecs** | [**[DnsKeySpec]**](DnsKeySpec.md) | DNSSEC algorithm and key length types that can be used for DnsKeys. | [optional] 


