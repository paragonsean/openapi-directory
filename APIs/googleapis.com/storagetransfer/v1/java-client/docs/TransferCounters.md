

# TransferCounters

A collection of counters that report the progress of a transfer operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesCopiedToSink** | **String** | Bytes that are copied to the data sink. |  [optional] |
|**bytesDeletedFromSink** | **String** | Bytes that are deleted from the data sink. |  [optional] |
|**bytesDeletedFromSource** | **String** | Bytes that are deleted from the data source. |  [optional] |
|**bytesFailedToDeleteFromSink** | **String** | Bytes that failed to be deleted from the data sink. |  [optional] |
|**bytesFoundFromSource** | **String** | Bytes found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync. |  [optional] |
|**bytesFoundOnlyFromSink** | **String** | Bytes found only in the data sink that are scheduled to be deleted. |  [optional] |
|**bytesFromSourceFailed** | **String** | Bytes in the data source that failed to be transferred or that failed to be deleted after being transferred. |  [optional] |
|**bytesFromSourceSkippedBySync** | **String** | Bytes in the data source that are not transferred because they already exist in the data sink. |  [optional] |
|**directoriesFailedToListFromSource** | **String** | For transfers involving PosixFilesystem only. Number of listing failures for each directory found at the source. Potential failures when listing a directory include permission failure or block failure. If listing a directory fails, no files in the directory are transferred. |  [optional] |
|**directoriesFoundFromSource** | **String** | For transfers involving PosixFilesystem only. Number of directories found while listing. For example, if the root directory of the transfer is &#x60;base/&#x60; and there are two other directories, &#x60;a/&#x60; and &#x60;b/&#x60; under this directory, the count after listing &#x60;base/&#x60;, &#x60;base/a/&#x60; and &#x60;base/b/&#x60; is 3. |  [optional] |
|**directoriesSuccessfullyListedFromSource** | **String** | For transfers involving PosixFilesystem only. Number of successful listings for each directory found at the source. |  [optional] |
|**intermediateObjectsCleanedUp** | **String** | Number of successfully cleaned up intermediate objects. |  [optional] |
|**intermediateObjectsFailedCleanedUp** | **String** | Number of intermediate objects failed cleaned up. |  [optional] |
|**objectsCopiedToSink** | **String** | Objects that are copied to the data sink. |  [optional] |
|**objectsDeletedFromSink** | **String** | Objects that are deleted from the data sink. |  [optional] |
|**objectsDeletedFromSource** | **String** | Objects that are deleted from the data source. |  [optional] |
|**objectsFailedToDeleteFromSink** | **String** | Objects that failed to be deleted from the data sink. |  [optional] |
|**objectsFoundFromSource** | **String** | Objects found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync. |  [optional] |
|**objectsFoundOnlyFromSink** | **String** | Objects found only in the data sink that are scheduled to be deleted. |  [optional] |
|**objectsFromSourceFailed** | **String** | Objects in the data source that failed to be transferred or that failed to be deleted after being transferred. |  [optional] |
|**objectsFromSourceSkippedBySync** | **String** | Objects in the data source that are not transferred because they already exist in the data sink. |  [optional] |



