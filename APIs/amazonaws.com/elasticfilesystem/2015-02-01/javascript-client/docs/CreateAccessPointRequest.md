# AmazonElasticFileSystem.CreateAccessPointRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation. | 
**tags** | [**[Tag]**](Tag.md) | Creates tags associated with the access point. Each tag is a key-value pair, each key must be unique. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference Guide&lt;/i&gt;. | [optional] 
**fileSystemId** | **String** | The ID of the EFS file system that the access point provides access to. | 
**posixUser** | [**CreateAccessPointRequestPosixUser**](CreateAccessPointRequestPosixUser.md) |  | [optional] 
**rootDirectory** | [**CreateAccessPointRequestRootDirectory**](CreateAccessPointRequestRootDirectory.md) |  | [optional] 


