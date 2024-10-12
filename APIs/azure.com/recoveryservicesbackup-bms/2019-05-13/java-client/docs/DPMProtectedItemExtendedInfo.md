

# DPMProtectedItemExtendedInfo

Additional information of DPM Protected item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskStorageUsedInBytes** | **String** | Used Disk storage in bytes. |  [optional] |
|**isCollocated** | **Boolean** | To check if backup item is collocated. |  [optional] |
|**isPresentOnCloud** | **Boolean** | To check if backup item is cloud protected. |  [optional] |
|**lastBackupStatus** | **String** | Last backup status information on backup item. |  [optional] |
|**lastRefreshedAt** | **OffsetDateTime** | Last refresh time on backup item. |  [optional] |
|**oldestRecoveryPoint** | **OffsetDateTime** | Oldest cloud recovery point time. |  [optional] |
|**onPremiseLatestRecoveryPoint** | **OffsetDateTime** | latest disk recovery point time. |  [optional] |
|**onPremiseOldestRecoveryPoint** | **OffsetDateTime** | Oldest disk recovery point time. |  [optional] |
|**onPremiseRecoveryPointCount** | **Integer** | disk recovery point count. |  [optional] |
|**protectableObjectLoadPath** | **Map&lt;String, String&gt;** | Attribute to provide information on various DBs. |  [optional] |
|**_protected** | **Boolean** | To check if backup item is disk protected. |  [optional] |
|**protectionGroupName** | **String** | Protection group name of the backup item. |  [optional] |
|**recoveryPointCount** | **Integer** | cloud recovery point count. |  [optional] |
|**totalDiskStorageSizeInBytes** | **String** | total Disk storage in bytes. |  [optional] |



