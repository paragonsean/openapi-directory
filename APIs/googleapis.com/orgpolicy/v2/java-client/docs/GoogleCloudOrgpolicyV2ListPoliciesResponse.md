

# GoogleCloudOrgpolicyV2ListPoliciesResponse

The response returned from the ListPolicies method. It will be empty if no policies are set on the resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token. |  [optional] |
|**policies** | [**List&lt;GoogleCloudOrgpolicyV2Policy&gt;**](GoogleCloudOrgpolicyV2Policy.md) | All policies that exist on the resource. It will be empty if no policies are set. |  [optional] |



