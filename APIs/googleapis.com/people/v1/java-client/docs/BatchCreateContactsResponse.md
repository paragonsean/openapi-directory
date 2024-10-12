

# BatchCreateContactsResponse

If not successful, returns BatchCreateContactsErrorDetails which contains a list of errors for each invalid contact. The response to a request to create a batch of contacts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdPeople** | [**List&lt;PersonResponse&gt;**](PersonResponse.md) | The contacts that were created, unless the request &#x60;read_mask&#x60; is empty. |  [optional] |



