

# PutLKEClusterRequestControlPlane

Defines settings for the Kubernetes Control Plane. Allows for the enabling of High Availability (HA) for Control Plane Components.  Enabling High Availability for LKE is an **irreversible** change.  When upgrading pre-existing LKE clusters to use the HA Control Plane, the following changes will additionally occur:  - All nodes will be deleted and new nodes will be created to replace them.  - Any local storage (such as `hostPath` volumes) will be erased.  - The upgrade process may take several minutes to complete, as nodes will be replaced on a rolling basis. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**highAvailability** | **Boolean** | Defines whether High Availability is enabled for the Control Plane Components of the cluster. Defaults to &#x60;false&#x60;.  |  [optional] |



