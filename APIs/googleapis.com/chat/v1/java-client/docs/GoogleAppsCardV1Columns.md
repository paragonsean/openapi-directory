

# GoogleAppsCardV1Columns

The `Columns` widget displays up to 2 columns in a card or dialog. You can add widgets to each column; the widgets appear in the order that they are specified. For an example in Google Chat apps, see [Columns](https://developers.google.com/chat/ui/widgets/columns). The height of each column is determined by the taller column. For example, if the first column is taller than the second column, both columns have the height of the first column. Because each column can contain a different number of widgets, you can't define rows or align widgets between the columns. Columns are displayed side-by-side. You can customize the width of each column using the `HorizontalSizeStyle` field. If the user's screen width is too narrow, the second column wraps below the first: * On web, the second column wraps if the screen width is less than or equal to 480 pixels. * On iOS devices, the second column wraps if the screen width is less than or equal to 300 pt. * On Android devices, the second column wraps if the screen width is less than or equal to 320 dp. To include more than 2 columns, or to use rows, use the `Grid` widget. [Google Workspace Add-ons and Chat apps](https://developers.google.com/workspace/extend): Columns for Google Workspace Add-ons are in [Developer Preview](https://developers.google.com/workspace/preview).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnItems** | [**List&lt;GoogleAppsCardV1Column&gt;**](GoogleAppsCardV1Column.md) | An array of columns. You can include up to 2 columns in a card or dialog. |  [optional] |



