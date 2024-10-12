

# Widget

Widget contains a single dashboard component and configuration of how to present the component in the dashboard.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertChart** | [**AlertChart**](AlertChart.md) |  |  [optional] |
|**blank** | **Object** | A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  |  [optional] |
|**collapsibleGroup** | [**CollapsibleGroup**](CollapsibleGroup.md) |  |  [optional] |
|**errorReportingPanel** | [**ErrorReportingPanel**](ErrorReportingPanel.md) |  |  [optional] |
|**id** | **String** | Optional. The widget id. Ids may be made up of alphanumerics, dashes and underscores. Widget ids are optional. |  [optional] |
|**incidentList** | [**IncidentList**](IncidentList.md) |  |  [optional] |
|**logsPanel** | [**LogsPanel**](LogsPanel.md) |  |  [optional] |
|**pieChart** | [**PieChart**](PieChart.md) |  |  [optional] |
|**scorecard** | [**Scorecard**](Scorecard.md) |  |  [optional] |
|**sectionHeader** | [**SectionHeader**](SectionHeader.md) |  |  [optional] |
|**singleViewGroup** | **Object** | A widget that groups the other widgets by using a dropdown menu. All widgets that are within the area spanned by the grouping widget are considered member widgets. |  [optional] |
|**text** | [**Text**](Text.md) |  |  [optional] |
|**timeSeriesTable** | [**TimeSeriesTable**](TimeSeriesTable.md) |  |  [optional] |
|**title** | **String** | Optional. The title of the widget. |  [optional] |
|**xyChart** | [**XyChart**](XyChart.md) |  |  [optional] |



