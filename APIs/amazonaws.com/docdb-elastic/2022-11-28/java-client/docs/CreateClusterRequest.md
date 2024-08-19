

# CreateClusterRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminUserName** | **String** | &lt;p&gt;The name of the Elastic DocumentDB cluster administrator.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Constraints&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must be from 1 to 63 letters or numbers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot be a reserved word.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**adminUserPassword** | **String** | &lt;p&gt;The password for the Elastic DocumentDB cluster administrator and can contain any printable ASCII characters.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Constraints&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 8 to 100 characters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot contain a forward slash (/), double quote (\&quot;), or the \&quot;at\&quot; symbol (@).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | The authentication type for the Elastic DocumentDB cluster. |  |
|**clientToken** | **String** | The client token for the Elastic DocumentDB cluster. |  [optional] |
|**clusterName** | **String** | &lt;p&gt;The name of the new Elastic DocumentDB cluster. This parameter is stored as a lowercase string.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Constraints&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Must contain from 1 to 63 letters, numbers, or hyphens.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The first character must be a letter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot end with a hyphen or contain two consecutive hyphens.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;i&gt;Example&lt;/i&gt;: &lt;code&gt;my-cluster&lt;/code&gt; &lt;/p&gt; |  |
|**kmsKeyId** | **String** | &lt;p&gt;The KMS key identifier to use to encrypt the new Elastic DocumentDB cluster.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.&lt;/p&gt; &lt;p&gt;If an encryption key is not specified, Elastic DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.&lt;/p&gt; |  [optional] |
|**preferredMaintenanceWindow** | **String** | &lt;p&gt;The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt; &lt;i&gt;Format&lt;/i&gt;: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;i&gt;Default&lt;/i&gt;: a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Valid days&lt;/i&gt;: Mon, Tue, Wed, Thu, Fri, Sat, Sun&lt;/p&gt; &lt;p&gt; &lt;i&gt;Constraints&lt;/i&gt;: Minimum 30-minute window.&lt;/p&gt; |  [optional] |
|**shardCapacity** | **Integer** | The capacity of each shard in the new Elastic DocumentDB cluster. |  |
|**shardCount** | **Integer** | The number of shards to create in the new Elastic DocumentDB cluster. |  |
|**subnetIds** | **List&lt;String&gt;** | The Amazon EC2 subnet IDs for the new Elastic DocumentDB cluster. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags to be assigned to the new Elastic DocumentDB cluster. |  [optional] |
|**vpcSecurityGroupIds** | **List&lt;String&gt;** | A list of EC2 VPC security groups to associate with the new Elastic DocumentDB cluster. |  [optional] |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| PLAIN_TEXT | &quot;PLAIN_TEXT&quot; |
| SECRET_ARN | &quot;SECRET_ARN&quot; |



