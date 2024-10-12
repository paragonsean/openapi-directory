

# Epoch

An Epoch is a configuration number for the partition as a whole. When the configuration of the replica set changes, for example when the Primary replica changes, the operations that are replicated from the new Primary replica are said to be a new Epoch from the ones which were sent by the old Primary replica.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationVersion** | **String** | The current configuration number of this Epoch. The configuration number is an increasing value that is updated whenever the configuration of this replica set changes. |  [optional] |
|**dataLossVersion** | **String** | The current data loss number of this Epoch. The data loss number property is an increasing value which is updated whenever data loss is suspected, as when loss of a quorum of replicas in the replica set that includes the Primary replica. |  [optional] |



