

# StorageType

StorageTypes represents the list of storage related types and their attributes that are available for given InstanceType. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storageTypeName** | **String** |  Type of the storage. List of available storage options: &lt;ol&gt; &lt;li&gt;instance&lt;/li&gt; Inbuilt storage available for the given Instance &lt;li&gt;ebs&lt;/li&gt; Elastic block storage that would be attached to the given Instance &lt;/ol&gt;  |  [optional] |
|**storageSubTypeName** | **String** |  SubType of the given storage type. List of available sub-storage options: For \&quot;instance\&quot; storageType we wont have any storageSubType, in case of \&quot;ebs\&quot; storageType we will have following valid storageSubTypes &lt;ol&gt; &lt;li&gt;standard&lt;/li&gt; &lt;li&gt;gp2&lt;/li&gt; &lt;li&gt;gp3&lt;/li&gt; &lt;li&gt;io1&lt;/li&gt; &lt;/ol&gt; Refer &lt;code&gt;&lt;a&gt;VolumeType&lt;/a&gt;&lt;/code&gt; for more information regarding above EBS storage options.  |  [optional] |
|**storageTypeLimits** | [**List**](List.md) |  |  [optional] |



