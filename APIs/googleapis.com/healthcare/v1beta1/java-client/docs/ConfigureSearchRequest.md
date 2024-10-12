

# ConfigureSearchRequest

Request to configure the search parameters for the specified FHIR store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canonicalUrls** | **List&lt;String&gt;** | The canonical URLs of the search parameters that are intended to be used for the FHIR store. See https://www.hl7.org/fhir/references.html#canonical for explanation on FHIR canonical urls |  [optional] |
|**validateOnly** | **Boolean** | If &#x60;validate_only&#x60; is set to true, the method will compile all the search parameters without actually setting the search config for the store and triggering the reindex. |  [optional] |



