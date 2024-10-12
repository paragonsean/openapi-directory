

# LabelList

A list of labels applied to a file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | This is always drive#labelList |  [optional] |
|**labels** | [**List&lt;Label&gt;**](Label.md) | The list of labels. |  [optional] |
|**nextPageToken** | **String** | The page token for the next page of labels. This field will be absent if the end of the list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. The page token is typically valid for several hours. However, if new items are added or removed, your expected results might differ. |  [optional] |



