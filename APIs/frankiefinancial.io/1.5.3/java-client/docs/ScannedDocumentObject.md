

# ScannedDocumentObject

the document to be attached and optionally scanned (if supported)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scanDelete** | **Boolean** | Used as a way of indicating to the service that the original scanned document is not to be kept after it has been processed. We will retain any metadata and the results of processing (where required by regulation or the customer), but the original file uploaded will eventually be remnoved once processing is complete.   If ScanDelete is set to true, any call with /full at the end will still not return the file contents, regardless of whether the file has been deleted yet (the deletion process is a background task that can take a few minutes to occur)  |  [optional] |
|**scanCreated** | **OffsetDateTime** | The date and time the scan was created. Not the date of the scanned document, which should be in the idIssued attribute of the document that owns this scan.  |  [optional] |
|**scanData** | **byte[]** | Base64 encoded string of a photo or scan of an ID document to be verified. If supplied and of a supported type, the Frankie service will attempt to use OCR tech to extract the data from the scanned doc/image.  In a result message, this field will be left blank, unless the \&quot;full\&quot; action is requested.  |  [optional] |
|**scanDataRetrievalState** | **EnumScanDataRetrievalState** |  |  [optional] |
|**scanDocId** | **UUID** | When an document scan is created/uploaded, it is assigned a scanDocId. You&#39;ll see this in a successful response or successfully accepted response. This can then be referenced in subsequent calls if you&#39;re uploading more/updated data.  |  [optional] |
|**scanFilename** | **String** | If you&#39;re uploading a file where it&#39;s important to keep the original filename, then you can provide that here. Otherwise the Frankie service will assign an arbitrary name based on the scanDocIdand an extension based on the MIME type  |  [optional] |
|**scanMIME** | **EnumMIMEType** |  |  [optional] |
|**scanPageNum** | **Integer** | If uploading multiple pages - it&#39;s handy to keep a track of these. There is no enforcement of these numbers at all. You can have 10 page 1&#39;s and a page 29 if you wish.  |  [optional] |
|**scanSide** | **EnumScanSide** |  |  [optional] |
|**scanType** | **EnumScanType** |  |  [optional] |



