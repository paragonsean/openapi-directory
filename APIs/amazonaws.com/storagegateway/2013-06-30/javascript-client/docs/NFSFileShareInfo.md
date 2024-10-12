# AwsStorageGateway.NFSFileShareInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nFSFileShareDefaults** | [**NFSFileShareDefaults**](NFSFileShareDefaults.md) |  | [optional] 
**fileShareARN** | **String** | The Amazon Resource Name (ARN) of the file share. | [optional] 
**fileShareId** | **String** | The ID of the file share. | [optional] 
**fileShareStatus** | **String** | &lt;p&gt;The status of the file share.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;CREATING&lt;/code&gt; | &lt;code&gt;UPDATING&lt;/code&gt; | &lt;code&gt;AVAILABLE&lt;/code&gt; | &lt;code&gt;DELETING&lt;/code&gt; &lt;/p&gt; | [optional] 
**gatewayARN** | **String** | The Amazon Resource Name (ARN) of the gateway. Use the &lt;a&gt;ListGateways&lt;/a&gt; operation to return a list of gateways for your account and Amazon Web Services Region. | [optional] 
**kMSEncrypted** | **Boolean** |  | [optional] 
**kMSKey** | **String** | The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when &lt;code&gt;KMSEncrypted&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. Optional. | [optional] 
**path** | **String** | The file share path used by the NFS client to identify the mount point. | [optional] 
**role** | **String** | The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage. | [optional] 
**locationARN** | **String** | &lt;p&gt;A custom ARN for the backend storage used for storing data for file shares. It includes a resource ARN with an optional prefix concatenation. The prefix must end with a forward slash (/).&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can specify LocationARN as a bucket ARN, access point ARN or access point alias, as shown in the following examples.&lt;/p&gt; &lt;p&gt;Bucket ARN:&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:s3:::my-bucket/prefix/&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Access point ARN:&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:s3:region:account-id:accesspoint/access-point-name/prefix/&lt;/code&gt; &lt;/p&gt; &lt;p&gt;If you specify an access point, the bucket policy must be configured to delegate access control to the access point. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html#access-points-delegating-control\&quot;&gt;Delegating access control to access points&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Access point alias:&lt;/p&gt; &lt;p&gt; &lt;code&gt;test-ap-ab123cdef4gehijklmn5opqrstuvuse1a-s3alias&lt;/code&gt; &lt;/p&gt; &lt;/note&gt; | [optional] 
**defaultStorageClass** | **String** |  | [optional] 
**objectACL** | [**ObjectACL**](ObjectACL.md) |  | [optional] 
**clientList** | **[String]** | The list of clients that are allowed to access the S3 File Gateway. The list must contain either valid IP addresses or valid CIDR blocks. | [optional] 
**squash** | **String** | &lt;p&gt;The user mapped to anonymous user. Valid options are the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RootSquash&lt;/code&gt;: Only root is mapped to anonymous user.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NoSquash&lt;/code&gt;: No one is mapped to anonymous user.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AllSquash&lt;/code&gt;: Everyone is mapped to anonymous user.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**readOnly** | **Boolean** |  | [optional] 
**guessMIMETypeEnabled** | **Boolean** |  | [optional] 
**requesterPays** | **Boolean** |  | [optional] 
**tags** | **Array** |  | [optional] 
**fileShareName** | **String** |  | [optional] 
**cacheAttributes** | [**NFSFileShareInfoCacheAttributes**](NFSFileShareInfoCacheAttributes.md) |  | [optional] 
**notificationPolicy** | **String** |  | [optional] 
**vPCEndpointDNSName** | **String** |  | [optional] 
**bucketRegion** | **String** |  | [optional] 
**auditDestinationARN** | **String** |  | [optional] 


