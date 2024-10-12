# AwsBackup.StartBackupJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupVaultName** | **String** | The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens. | 
**resourceArn** | **String** | An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type. | 
**iamRoleArn** | **String** | Specifies the IAM role ARN used to create the target recovery point; for example, &lt;code&gt;arn:aws:iam::123456789012:role/S3Access&lt;/code&gt;. | 
**idempotencyToken** | **String** | A customer-chosen string that you can use to distinguish between otherwise identical calls to &lt;code&gt;StartBackupJob&lt;/code&gt;. Retrying a successful request with the same idempotency token results in a success message with no action taken. | [optional] 
**startWindowMinutes** | **Number** | &lt;p&gt;A value in minutes after a backup is scheduled before a job will be canceled if it doesn&#39;t start successfully. This value is optional, and the default is 8 hours. If this value is included, it must be at least 60 minutes to avoid errors.&lt;/p&gt; &lt;p&gt;During the start window, the backup job status remains in &lt;code&gt;CREATED&lt;/code&gt; status until it has successfully begun or until the start window time has run out. If within the start window time Backup receives an error that allows the job to be retried, Backup will automatically retry to begin the job at least every 10 minutes until the backup successfully begins (the job status changes to &lt;code&gt;RUNNING&lt;/code&gt;) or until the job status changes to &lt;code&gt;EXPIRED&lt;/code&gt; (which is expected to occur when the start window time is over).&lt;/p&gt; | [optional] 
**completeWindowMinutes** | **Number** | A value in minutes during which a successfully started backup must complete, or else Backup will cancel the job. This value is optional. This value begins counting down from when the backup was scheduled. It does not add additional time for &lt;code&gt;StartWindowMinutes&lt;/code&gt;, or if the backup started later than scheduled. | [optional] 
**lifecycle** | [**UpdateRecoveryPointLifecycleRequestLifecycle**](UpdateRecoveryPointLifecycleRequestLifecycle.md) |  | [optional] 
**recoveryPointTags** | **{String: String}** | To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. | [optional] 
**backupOptions** | **{String: String}** | &lt;p&gt;Specifies the backup option for a selected resource. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs.&lt;/p&gt; &lt;p&gt;Valid values: Set to &lt;code&gt;\&quot;WindowsVSS\&quot;:\&quot;enabled\&quot;&lt;/code&gt; to enable the &lt;code&gt;WindowsVSS&lt;/code&gt; backup option and create a Windows VSS backup. Set to &lt;code&gt;\&quot;WindowsVSS\&quot;\&quot;disabled\&quot;&lt;/code&gt; to create a regular backup. The &lt;code&gt;WindowsVSS&lt;/code&gt; option is not enabled by default.&lt;/p&gt; | [optional] 


