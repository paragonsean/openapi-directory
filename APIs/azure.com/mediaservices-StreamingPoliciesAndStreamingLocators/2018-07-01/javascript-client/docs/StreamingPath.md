# AzureMediaServices.StreamingPath

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionScheme** | **String** | Encryption scheme | 
**paths** | **[String]** | Streaming paths for each protocol and encryptionScheme pair | [optional] 
**streamingProtocol** | **String** | Streaming protocol | 



## Enum: EncryptionSchemeEnum


* `NoEncryption` (value: `"NoEncryption"`)

* `EnvelopeEncryption` (value: `"EnvelopeEncryption"`)

* `CommonEncryptionCenc` (value: `"CommonEncryptionCenc"`)

* `CommonEncryptionCbcs` (value: `"CommonEncryptionCbcs"`)





## Enum: StreamingProtocolEnum


* `Hls` (value: `"Hls"`)

* `Dash` (value: `"Dash"`)

* `SmoothStreaming` (value: `"SmoothStreaming"`)

* `Download` (value: `"Download"`)




