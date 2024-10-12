

# CreateBackupVaultRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupVaultTags** | **Map&lt;String, String&gt;** | Metadata that you can assign to help organize the resources that you create. Each tag is a key-value pair. |  [optional] |
|**encryptionKeyArn** | **String** | The server-side encryption key that is used to protect your backups; for example, &lt;code&gt;arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab&lt;/code&gt;. |  [optional] |
|**creatorRequestId** | **String** | &lt;p&gt;A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.&lt;/p&gt; &lt;p&gt;If used, this parameter must contain 1 to 50 alphanumeric or &#39;-_.&#39; characters.&lt;/p&gt; |  [optional] |



