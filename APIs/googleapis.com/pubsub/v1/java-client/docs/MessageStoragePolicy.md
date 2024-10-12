

# MessageStoragePolicy

A policy constraining the storage of messages published to the topic.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedPersistenceRegions** | **List&lt;String&gt;** | Optional. A list of IDs of Google Cloud regions where messages that are published to the topic may be persisted in storage. Messages published by publishers running in non-allowed Google Cloud regions (or running outside of Google Cloud altogether) are routed for storage in one of the allowed regions. An empty list means that no regions are allowed, and is not a valid configuration. |  [optional] |
|**enforceInTransit** | **Boolean** | Optional. If true, &#x60;allowed_persistence_regions&#x60; is also used to enforce in-transit guarantees for messages. That is, Pub/Sub will fail Publish operations on this topic and subscribe operations on any subscription attached to this topic in any region that is not in &#x60;allowed_persistence_regions&#x60;. |  [optional] |



