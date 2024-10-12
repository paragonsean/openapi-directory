

# ListFhirStoresResponse

Lists the FHIR stores in the given dataset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fhirStores** | [**List&lt;FhirStore&gt;**](FhirStore.md) | The returned FHIR stores. Won&#39;t be more FHIR stores than the value of page_size in the request. |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results or empty if there are no more results in the list. |  [optional] |



