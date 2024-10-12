

# BatchUpdateContactsResponse

If not successful, returns BatchUpdateContactsErrorDetails, a list of errors corresponding to each contact. The response to a request to update a batch of contacts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**updateResult** | [**Map&lt;String, PersonResponse&gt;**](PersonResponse.md) | A map of resource names to the contacts that were updated, unless the request &#x60;read_mask&#x60; is empty. |  [optional] |



