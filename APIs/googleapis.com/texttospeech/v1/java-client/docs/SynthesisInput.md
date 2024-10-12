

# SynthesisInput

Contains text input to be synthesized. Either `text` or `ssml` must be supplied. Supplying both or neither returns google.rpc.Code.INVALID_ARGUMENT. The input size is limited to 5000 bytes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ssml** | **String** | The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return google.rpc.Code.INVALID_ARGUMENT. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml). |  [optional] |
|**text** | **String** | The raw text to be synthesized. |  [optional] |



