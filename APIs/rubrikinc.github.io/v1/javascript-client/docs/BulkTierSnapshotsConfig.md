# RubrikRestApi.BulkTierSnapshotsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locationId** | **String** | Users can specify the archival location ID in order to tier snapshots in the specified archival location. When an archival location ID is not specified, snapshots in the archival location specified in the SLA Domain policy for protected objects will be tiered. Relic and unprotected object snapshots across all archival locations will be tiered. | [optional] 
**objectIds** | **[String]** | A list of object IDs to tier. | 


