# AmazonFsx.CreateFileSystemRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRequestToken** | **String** |  | [optional] 
**fileSystemType** | [**FileSystemType**](FileSystemType.md) |  | 
**storageCapacity** | **Number** |  | 
**storageType** | [**StorageType**](StorageType.md) |  | [optional] 
**subnetIds** | **Array** |  | 
**securityGroupIds** | **Array** |  | [optional] 
**tags** | **Array** |  | [optional] 
**kmsKeyId** | **String** | &lt;p&gt;Specifies the ID of the Key Management Service (KMS) key to use for encrypting data on Amazon FSx file systems, as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for Lustre &lt;code&gt;PERSISTENT_1&lt;/code&gt; and &lt;code&gt;PERSISTENT_2&lt;/code&gt; deployment types only.&lt;/p&gt; &lt;p&gt; &lt;code&gt;SCRATCH_1&lt;/code&gt; and &lt;code&gt;SCRATCH_2&lt;/code&gt; types are encrypted using the Amazon FSx service KMS key for your account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for NetApp ONTAP&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for OpenZFS&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon FSx for Windows File Server&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If a &lt;code&gt;KmsKeyId&lt;/code&gt; isn&#39;t specified, the Amazon FSx-managed KMS key for your account is used. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html\&quot;&gt;Encrypt&lt;/a&gt; in the &lt;i&gt;Key Management Service API Reference&lt;/i&gt;.&lt;/p&gt; | [optional] 
**windowsConfiguration** | [**CreateFileSystemRequestWindowsConfiguration**](CreateFileSystemRequestWindowsConfiguration.md) |  | [optional] 
**lustreConfiguration** | [**CreateFileSystemLustreConfiguration**](CreateFileSystemLustreConfiguration.md) |  | [optional] 
**ontapConfiguration** | [**CreateFileSystemOntapConfiguration**](CreateFileSystemOntapConfiguration.md) |  | [optional] 
**fileSystemTypeVersion** | **String** |  | [optional] 
**openZFSConfiguration** | [**CreateFileSystemRequestOpenZFSConfiguration**](CreateFileSystemRequestOpenZFSConfiguration.md) |  | [optional] 


