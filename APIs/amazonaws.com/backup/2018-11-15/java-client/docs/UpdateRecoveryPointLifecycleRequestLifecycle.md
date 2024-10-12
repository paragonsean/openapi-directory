

# UpdateRecoveryPointLifecycleRequestLifecycle

<p>Contains an array of <code>Transition</code> objects specifying how long in days before a recovery point transitions to cold storage or is deleted.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.</p> <p>Resource types that are able to be transitioned to cold storage are listed in the \"Lifecycle to cold storage\" section of the <a href=\"https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource\"> Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**moveToColdStorageAfterDays** | [**Integer**](Integer.md) |  |  [optional] |
|**deleteAfterDays** | [**Integer**](Integer.md) |  |  [optional] |



