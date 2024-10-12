

# QuantityBasedExpiry

A backup's position in a quantity-based retention queue, of backups with the same source cluster and type, with length, retention, specified by the backup's retention policy. Once the position is greater than the retention, the backup is eligible to be garbage collected. Example: 5 backups from the same source cluster and type with a quantity-based retention of 3 and denoted by backup_id (position, retention). Safe: backup_5 (1, 3), backup_4, (2, 3), backup_3 (3, 3). Awaiting garbage collection: backup_2 (4, 3), backup_1 (5, 3)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retentionCount** | **Integer** | Output only. The backup&#39;s position among its backups with the same source cluster and type, by descending chronological order create time(i.e. newest first). |  [optional] [readonly] |
|**totalRetentionCount** | **Integer** | Output only. The length of the quantity-based queue, specified by the backup&#39;s retention policy. |  [optional] [readonly] |



