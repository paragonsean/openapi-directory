

# GoogleCloudDialogflowCxV3beta1AudioInput

Represents the natural speech audio to be processed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audio** | **byte[]** | The natural language speech audio to be processed. A single request can contain up to 2 minutes of speech audio data. The transcribed text cannot contain more than 256 bytes. For non-streaming audio detect intent, both &#x60;config&#x60; and &#x60;audio&#x60; must be provided. For streaming audio detect intent, &#x60;config&#x60; must be provided in the first request and &#x60;audio&#x60; must be provided in all following requests. |  [optional] |
|**config** | [**GoogleCloudDialogflowCxV3beta1InputAudioConfig**](GoogleCloudDialogflowCxV3beta1InputAudioConfig.md) |  |  [optional] |



