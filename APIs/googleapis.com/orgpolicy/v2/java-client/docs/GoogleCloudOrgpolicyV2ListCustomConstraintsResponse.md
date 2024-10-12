

# GoogleCloudOrgpolicyV2ListCustomConstraintsResponse

The response returned from the ListCustomConstraints method. It will be empty if no custom constraints are set on the organization resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customConstraints** | [**List&lt;GoogleCloudOrgpolicyV2CustomConstraint&gt;**](GoogleCloudOrgpolicyV2CustomConstraint.md) | All custom constraints that exist on the organization resource. It will be empty if no custom constraints are set. |  [optional] |
|**nextPageToken** | **String** | Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token. |  [optional] |



