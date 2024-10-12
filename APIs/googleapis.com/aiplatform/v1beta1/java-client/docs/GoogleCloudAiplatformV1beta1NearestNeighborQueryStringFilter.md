

# GoogleCloudAiplatformV1beta1NearestNeighborQueryStringFilter

String filter is used to search a subset of the entities by using boolean rules on string columns. For example: if a query specifies string filter with 'name = color, allow_tokens = {red, blue}, deny_tokens = {purple}',' then that query will match entities that are red or blue, but if those points are also purple, then they will be excluded even if they are red/blue. Only string filter is supported for now, numeric filter will be supported in the near future.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowTokens** | **List&lt;String&gt;** | Optional. The allowed tokens. |  [optional] |
|**denyTokens** | **List&lt;String&gt;** | Optional. The denied tokens. |  [optional] |
|**name** | **String** | Required. Column names in BigQuery that used as filters. |  [optional] |



