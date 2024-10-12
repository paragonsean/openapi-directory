

# PagedSecretValueResourceDescriptionList

The list of values of a secret resource, paged if the number of results exceeds the limits of a single message. The next set of results can be obtained by executing the same query with the continuation token provided in the previous page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuationToken** | **String** | The continuation token parameter is used to obtain next set of results. The continuation token is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token is not included in the response. |  [optional] |
|**items** | [**List&lt;SecretValueResourceDescription&gt;**](SecretValueResourceDescription.md) | One page of the list. |  [optional] |



