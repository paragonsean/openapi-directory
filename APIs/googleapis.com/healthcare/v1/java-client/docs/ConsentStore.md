

# ConsentStore

Represents a consent store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultConsentTtl** | **String** | Optional. Default time to live for Consents created in this store. Must be at least 24 hours. Updating this field will not affect the expiration time of existing consents. |  [optional] |
|**enableConsentCreateOnUpdate** | **Boolean** | Optional. If &#x60;true&#x60;, UpdateConsent creates the Consent if it does not already exist. If unspecified, defaults to &#x60;false&#x60;. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-supplied key-value pairs used to organize consent stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \\p{Ll}\\p{Lo}{0,62}. Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\\p{Ll}\\p{Lo}\\p{N}_-]{0,63}. No more than 64 labels can be associated with a given store. For more information: https://cloud.google.com/healthcare/docs/how-tos/labeling-resources |  [optional] |
|**name** | **String** | Identifier. Resource name of the consent store, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}&#x60;. Cannot be changed after creation. |  [optional] |



