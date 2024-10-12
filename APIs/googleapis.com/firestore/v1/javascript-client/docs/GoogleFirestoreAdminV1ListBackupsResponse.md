# CloudFirestoreApi.GoogleFirestoreAdminV1ListBackupsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups** | [**[GoogleFirestoreAdminV1Backup]**](GoogleFirestoreAdminV1Backup.md) | List of all backups for the project. Ordered by &#x60;location ASC, create_time DESC, name ASC&#x60;. | [optional] 
**unreachable** | **[String]** | List of locations that existing backups were not able to be fetched from. Instead of failing the entire requests when a single location is unreachable, this response returns a partial result set and list of locations unable to be reached here. The request can be retried against a single location to get a concrete error. | [optional] 


