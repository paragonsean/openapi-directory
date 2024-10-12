

# Blobstore2Info

Information to read/write to blobstore2.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobGeneration** | **String** | The blob generation id. |  [optional] |
|**blobId** | **String** | The blob id, e.g., /blobstore/prod/playground/scotty |  [optional] |
|**downloadReadHandle** | **byte[]** | Read handle passed from Bigstore -&gt; Scotty for a GCS download. This is a signed, serialized blobstore2.ReadHandle proto which must never be set outside of Bigstore, and is not applicable to non-GCS media downloads. |  [optional] |
|**readToken** | **String** | The blob read token. Needed to read blobs that have not been replicated. Might not be available until the final call. |  [optional] |
|**uploadMetadataContainer** | **byte[]** | Metadata passed from Blobstore -&gt; Scotty for a new GCS upload. This is a signed, serialized blobstore2.BlobMetadataContainer proto which must never be consumed outside of Bigstore, and is not applicable to non-GCS media uploads. |  [optional] |



