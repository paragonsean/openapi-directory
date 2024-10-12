

# SearchAllIamPoliciesResponse

Search all IAM policies response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Set if there are more results than those appearing in this response; to get the next set of results, call this method again, using this value as the &#x60;page_token&#x60;. |  [optional] |
|**results** | [**List&lt;IamPolicySearchResult&gt;**](IamPolicySearchResult.md) | A list of IAM policies that match the search query. Related information such as the associated resource is returned along with the policy. |  [optional] |



