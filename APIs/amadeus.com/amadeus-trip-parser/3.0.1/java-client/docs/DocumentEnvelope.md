

# DocumentEnvelope

Data model to convey any kind of document, any format with associated meta data to help the identification and the decoding.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metaData** | [**DocumentEnvelopeMetaData**](DocumentEnvelopeMetaData.md) |  |  [optional] |
|**payload** | **String** | This contains the payload of the document. It can either be raw data or encoded data in b6se4. see details in metaData block. |  [optional] |



