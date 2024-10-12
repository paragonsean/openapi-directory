

# StreamingPath

Class of paths for streaming

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionScheme** | [**EncryptionSchemeEnum**](#EncryptionSchemeEnum) | Encryption scheme |  |
|**paths** | **List&lt;String&gt;** | Streaming paths for each protocol and encryptionScheme pair |  [optional] |
|**streamingProtocol** | [**StreamingProtocolEnum**](#StreamingProtocolEnum) | Streaming protocol |  |



## Enum: EncryptionSchemeEnum

| Name | Value |
|---- | -----|
| NO_ENCRYPTION | &quot;NoEncryption&quot; |
| ENVELOPE_ENCRYPTION | &quot;EnvelopeEncryption&quot; |
| COMMON_ENCRYPTION_CENC | &quot;CommonEncryptionCenc&quot; |
| COMMON_ENCRYPTION_CBCS | &quot;CommonEncryptionCbcs&quot; |



## Enum: StreamingProtocolEnum

| Name | Value |
|---- | -----|
| HLS | &quot;Hls&quot; |
| DASH | &quot;Dash&quot; |
| SMOOTH_STREAMING | &quot;SmoothStreaming&quot; |
| DOWNLOAD | &quot;Download&quot; |



