

# ListHcxActivationKeysResponse

Response message for VmwareEngine.ListHcxActivationKeys

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hcxActivationKeys** | [**List&lt;HcxActivationKey&gt;**](HcxActivationKey.md) | List of HCX activation keys. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached when making an aggregated query using wildcards. |  [optional] |



