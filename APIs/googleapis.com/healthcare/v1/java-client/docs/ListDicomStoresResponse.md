

# ListDicomStoresResponse

Lists the DICOM stores in the given dataset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dicomStores** | [**List&lt;DicomStore&gt;**](DicomStore.md) | The returned DICOM stores. Won&#39;t be more DICOM stores than the value of page_size in the request. |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results or empty if there are no more results in the list. |  [optional] |



