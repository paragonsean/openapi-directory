# AmazonFsx.CreateVolumeFromBackupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupId** | **String** | The ID of the source backup. Specifies the backup that you are copying. | 
**clientRequestToken** | **String** | (Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK. | [optional] 
**name** | **String** |  | 
**ontapConfiguration** | [**CreateVolumeFromBackupRequestOntapConfiguration**](CreateVolumeFromBackupRequestOntapConfiguration.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. | [optional] 


