# AmazonDocumentDbElasticClusters.RestoreClusterFromSnapshotRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterName** | **String** | The name of the Elastic DocumentDB cluster. | 
**kmsKeyId** | **String** | &lt;p&gt;The KMS key identifier to use to encrypt the new Elastic DocumentDB cluster.&lt;/p&gt; &lt;p&gt;The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key.&lt;/p&gt; &lt;p&gt;If an encryption key is not specified here, Elastic DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.&lt;/p&gt; | [optional] 
**subnetIds** | **[String]** | The Amazon EC2 subnet IDs for the Elastic DocumentDB cluster. | [optional] 
**tags** | **{String: String}** | A list of the tag names to be assigned to the restored DB cluster, in the form of an array of key-value pairs in which the key is the tag name and the value is the key value. | [optional] 
**vpcSecurityGroupIds** | **[String]** | A list of EC2 VPC security groups to associate with the Elastic DocumentDB cluster. | [optional] 


