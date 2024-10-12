

# DescribeDomainHealthResponse

The result of a <code>DescribeDomainHealth</code> request. Contains health information for the requested domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainState** | [**DomainState**](DomainState.md) |  |  [optional] |
|**availabilityZoneCount** | [**String**](String.md) |  |  [optional] |
|**activeAvailabilityZoneCount** | [**String**](String.md) |  |  [optional] |
|**standByAvailabilityZoneCount** | [**String**](String.md) |  |  [optional] |
|**dataNodeCount** | [**String**](String.md) |  |  [optional] |
|**dedicatedMaster** | [**Boolean**](Boolean.md) |  |  [optional] |
|**masterEligibleNodeCount** | [**String**](String.md) |  |  [optional] |
|**warmNodeCount** | [**String**](String.md) |  |  [optional] |
|**masterNode** | [**MasterNodeStatus**](MasterNodeStatus.md) |  |  [optional] |
|**clusterHealth** | [**DomainHealth**](DomainHealth.md) |  |  [optional] |
|**totalShards** | [**String**](String.md) |  |  [optional] |
|**totalUnAssignedShards** | [**String**](String.md) |  |  [optional] |
|**environmentInformation** | [**List**](List.md) |  |  [optional] |



