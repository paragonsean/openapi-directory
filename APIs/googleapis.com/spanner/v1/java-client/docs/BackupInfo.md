

# BackupInfo

Information about a backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backup** | **String** | Name of the backup. |  [optional] |
|**createTime** | **String** | The time the CreateBackup request was received. |  [optional] |
|**sourceDatabase** | **String** | Name of the database the backup was created from. |  [optional] |
|**versionTime** | **String** | The backup contains an externally consistent copy of &#x60;source_database&#x60; at the timestamp specified by &#x60;version_time&#x60;. If the CreateBackup request did not specify &#x60;version_time&#x60;, the &#x60;version_time&#x60; of the backup is equivalent to the &#x60;create_time&#x60;. |  [optional] |



