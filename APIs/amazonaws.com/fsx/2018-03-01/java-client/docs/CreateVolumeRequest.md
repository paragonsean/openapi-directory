

# CreateVolumeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRequestToken** | **String** | (Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK. |  [optional] |
|**volumeType** | [**VolumeType**](VolumeType.md) |  |  |
|**name** | [**String**](String.md) |  |  |
|**ontapConfiguration** | [**CreateVolumeRequestOntapConfiguration**](CreateVolumeRequestOntapConfiguration.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. |  [optional] |
|**openZFSConfiguration** | [**CreateVolumeRequestOpenZFSConfiguration**](CreateVolumeRequestOpenZFSConfiguration.md) |  |  [optional] |



