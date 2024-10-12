

# Quota

Limits associated with a Project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsKeysPerManagedZone** | **Integer** | Maximum allowed number of DnsKeys per ManagedZone. |  [optional] |
|**gkeClustersPerManagedZone** | **Integer** | Maximum allowed number of GKE clusters to which a privately scoped zone can be attached. |  [optional] |
|**gkeClustersPerPolicy** | **Integer** | Maximum allowed number of GKE clusters per policy. |  [optional] |
|**gkeClustersPerResponsePolicy** | **Integer** | Maximum allowed number of GKE clusters per response policy. |  [optional] |
|**itemsPerRoutingPolicy** | **Integer** | Maximum allowed number of items per routing policy. |  [optional] |
|**kind** | **String** |  |  [optional] |
|**managedZones** | **Integer** | Maximum allowed number of managed zones in the project. |  [optional] |
|**managedZonesPerGkeCluster** | **Integer** | Maximum allowed number of managed zones which can be attached to a GKE cluster. |  [optional] |
|**managedZonesPerNetwork** | **Integer** | Maximum allowed number of managed zones which can be attached to a network. |  [optional] |
|**nameserversPerDelegation** | **Integer** | Maximum number of nameservers per delegation, meant to prevent abuse |  [optional] |
|**networksPerManagedZone** | **Integer** | Maximum allowed number of networks to which a privately scoped zone can be attached. |  [optional] |
|**networksPerPolicy** | **Integer** | Maximum allowed number of networks per policy. |  [optional] |
|**networksPerResponsePolicy** | **Integer** | Maximum allowed number of networks per response policy. |  [optional] |
|**peeringZonesPerTargetNetwork** | **Integer** | Maximum allowed number of consumer peering zones per target network owned by this producer project |  [optional] |
|**policies** | **Integer** | Maximum allowed number of policies per project. |  [optional] |
|**resourceRecordsPerRrset** | **Integer** | Maximum allowed number of ResourceRecords per ResourceRecordSet. |  [optional] |
|**responsePolicies** | **Integer** | Maximum allowed number of response policies per project. |  [optional] |
|**responsePolicyRulesPerResponsePolicy** | **Integer** | Maximum allowed number of rules per response policy. |  [optional] |
|**rrsetAdditionsPerChange** | **Integer** | Maximum allowed number of ResourceRecordSets to add per ChangesCreateRequest. |  [optional] |
|**rrsetDeletionsPerChange** | **Integer** | Maximum allowed number of ResourceRecordSets to delete per ChangesCreateRequest. |  [optional] |
|**rrsetsPerManagedZone** | **Integer** | Maximum allowed number of ResourceRecordSets per zone in the project. |  [optional] |
|**targetNameServersPerManagedZone** | **Integer** | Maximum allowed number of target name servers per managed forwarding zone. |  [optional] |
|**targetNameServersPerPolicy** | **Integer** | Maximum allowed number of alternative target name servers per policy. |  [optional] |
|**totalRrdataSizePerChange** | **Integer** | Maximum allowed size for total rrdata in one ChangesCreateRequest in bytes. |  [optional] |
|**whitelistedKeySpecs** | [**List&lt;DnsKeySpec&gt;**](DnsKeySpec.md) | DNSSEC algorithm and key length types that can be used for DnsKeys. |  [optional] |



