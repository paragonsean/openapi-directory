

# CalculatedLifecycle

<p>Contains <code>DeleteAt</code> and <code>MoveToColdStorageAt</code> timestamps, which are used to specify a lifecycle for a recovery point.</p> <p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.</p> <p>Resource types that are able to be transitioned to cold storage are listed in the \"Lifecycle to cold storage\" section of the <a href=\"https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource\"> Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**moveToColdStorageAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**deleteAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



