# AwsBackup.PutBackupVaultNotificationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sNSTopicArn** | **String** | The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events; for example, &lt;code&gt;arn:aws:sns:us-west-2:111122223333:MyVaultTopic&lt;/code&gt;. | 
**backupVaultEvents** | [**[BackupVaultEvent]**](BackupVaultEvent.md) | &lt;p&gt;An array of events that indicate the status of jobs to back up resources to the backup vault.&lt;/p&gt; &lt;p&gt;For common use cases and code samples, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-backup/latest/devguide/sns-notifications.html\&quot;&gt;Using Amazon SNS to track Backup events&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following events are supported:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BACKUP_JOB_STARTED&lt;/code&gt; | &lt;code&gt;BACKUP_JOB_COMPLETED&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;COPY_JOB_STARTED&lt;/code&gt; | &lt;code&gt;COPY_JOB_SUCCESSFUL&lt;/code&gt; | &lt;code&gt;COPY_JOB_FAILED&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RESTORE_JOB_STARTED&lt;/code&gt; | &lt;code&gt;RESTORE_JOB_COMPLETED&lt;/code&gt; | &lt;code&gt;RECOVERY_POINT_MODIFIED&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;S3_BACKUP_OBJECT_FAILED&lt;/code&gt; | &lt;code&gt;S3_RESTORE_OBJECT_FAILED&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The list below shows items that are deprecated events (for reference) and are no longer in use. They are no longer supported and will not return statuses or notifications. Refer to the list above for current supported events.&lt;/p&gt; &lt;/note&gt; | 


