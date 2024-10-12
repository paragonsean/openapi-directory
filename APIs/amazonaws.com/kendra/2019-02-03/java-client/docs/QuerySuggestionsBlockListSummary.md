

# QuerySuggestionsBlockListSummary

<p>Summary information on a query suggestions block list.</p> <p>This includes information on the block list ID, block list name, when the block list was created, when the block list was last updated, and the count of block words/phrases in the block list.</p> <p>For information on the current quota limits for block lists, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/quotas.html\">Quotas for Amazon Kendra</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**status** | [**QuerySuggestionsBlockListStatus**](QuerySuggestionsBlockListStatus.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**itemCount** | [**Integer**](Integer.md) |  |  [optional] |



