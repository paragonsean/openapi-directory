

# StartCopyJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recoveryPointArn** | **String** | An ARN that uniquely identifies a recovery point to use for the copy job; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.  |  |
|**sourceBackupVaultName** | **String** | The name of a logical source container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. |  |
|**destinationBackupVaultArn** | **String** | An Amazon Resource Name (ARN) that uniquely identifies a destination backup vault to copy to; for example, &lt;code&gt;arn:aws:backup:us-east-1:123456789012:vault:aBackupVault&lt;/code&gt;. |  |
|**iamRoleArn** | **String** | Specifies the IAM role ARN used to copy the target recovery point; for example, &lt;code&gt;arn:aws:iam::123456789012:role/S3Access&lt;/code&gt;. |  |
|**idempotencyToken** | **String** | A customer-chosen string that you can use to distinguish between otherwise identical calls to &lt;code&gt;StartCopyJob&lt;/code&gt;. Retrying a successful request with the same idempotency token results in a success message with no action taken. |  [optional] |
|**lifecycle** | [**UpdateRecoveryPointLifecycleRequestLifecycle**](UpdateRecoveryPointLifecycleRequestLifecycle.md) |  |  [optional] |



