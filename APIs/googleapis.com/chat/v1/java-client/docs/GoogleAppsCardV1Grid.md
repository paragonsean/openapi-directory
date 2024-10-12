

# GoogleAppsCardV1Grid

Displays a grid with a collection of items. Items can only include text or images. For responsive columns, or to include more than text or images, use `Columns`. For an example in Google Chat apps, see [Grid](https://developers.google.com/chat/ui/widgets/grid). A grid supports any number of columns and items. The number of rows is determined by items divided by columns. A grid with 10 items and 2 columns has 5 rows. A grid with 11 items and 2 columns has 6 rows. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend): For example, the following JSON creates a 2 column grid with a single item: ``` \"grid\": { \"title\": \"A fine collection of items\", \"columnCount\": 2, \"borderStyle\": { \"type\": \"STROKE\", \"cornerRadius\": 4 }, \"items\": [ { \"image\": { \"imageUri\": \"https://www.example.com/image.png\", \"cropStyle\": { \"type\": \"SQUARE\" }, \"borderStyle\": { \"type\": \"STROKE\" } }, \"title\": \"An item\", \"textAlignment\": \"CENTER\" } ], \"onClick\": { \"openLink\": { \"url\": \"https://www.example.com\" } } } ```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**borderStyle** | [**GoogleAppsCardV1BorderStyle**](GoogleAppsCardV1BorderStyle.md) |  |  [optional] |
|**columnCount** | **Integer** | The number of columns to display in the grid. A default value is used if this field isn&#39;t specified, and that default value is different depending on where the grid is shown (dialog versus companion). |  [optional] |
|**items** | [**List&lt;GoogleAppsCardV1GridItem&gt;**](GoogleAppsCardV1GridItem.md) | The items to display in the grid. |  [optional] |
|**onClick** | [**GoogleAppsCardV1OnClick**](GoogleAppsCardV1OnClick.md) |  |  [optional] |
|**title** | **String** | The text that displays in the grid header. |  [optional] |



