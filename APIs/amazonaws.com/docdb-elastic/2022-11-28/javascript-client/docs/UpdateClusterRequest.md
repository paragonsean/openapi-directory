# AmazonDocumentDbElasticClusters.UpdateClusterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminUserPassword** | **String** | &lt;p&gt;The password for the Elastic DocumentDB cluster administrator. This password can contain any printable ASCII character except forward slash (/), double quote (\&quot;), or the \&quot;at\&quot; symbol (@).&lt;/p&gt; &lt;p&gt; &lt;i&gt;Constraints&lt;/i&gt;: Must contain from 8 to 100 characters.&lt;/p&gt; | [optional] 
**authType** | **String** | The authentication type for the Elastic DocumentDB cluster. | [optional] 
**clientToken** | **String** | The client token for the Elastic DocumentDB cluster. | [optional] 
**preferredMaintenanceWindow** | **String** | &lt;p&gt;The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).&lt;/p&gt; &lt;p&gt; &lt;i&gt;Format&lt;/i&gt;: &lt;code&gt;ddd:hh24:mi-ddd:hh24:mi&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;i&gt;Default&lt;/i&gt;: a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Valid days&lt;/i&gt;: Mon, Tue, Wed, Thu, Fri, Sat, Sun&lt;/p&gt; &lt;p&gt; &lt;i&gt;Constraints&lt;/i&gt;: Minimum 30-minute window.&lt;/p&gt; | [optional] 
**shardCapacity** | **Number** | The capacity of each shard in the Elastic DocumentDB cluster. | [optional] 
**shardCount** | **Number** | The number of shards to create in the Elastic DocumentDB cluster. | [optional] 
**subnetIds** | **[String]** | The number of shards to create in the Elastic DocumentDB cluster. | [optional] 
**vpcSecurityGroupIds** | **[String]** | A list of EC2 VPC security groups to associate with the new Elastic DocumentDB cluster. | [optional] 



## Enum: AuthTypeEnum


* `PLAIN_TEXT` (value: `"PLAIN_TEXT"`)

* `SECRET_ARN` (value: `"SECRET_ARN"`)




