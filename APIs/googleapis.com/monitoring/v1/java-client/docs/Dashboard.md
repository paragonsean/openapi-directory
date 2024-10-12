

# Dashboard

A Google Stackdriver dashboard. Dashboards define the content and layout of pages in the Stackdriver web application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnLayout** | [**ColumnLayout**](ColumnLayout.md) |  |  [optional] |
|**dashboardFilters** | [**List&lt;DashboardFilter&gt;**](DashboardFilter.md) | Filters to reduce the amount of data charted based on the filter criteria. |  [optional] |
|**displayName** | **String** | Required. The mutable, human-readable name. |  [optional] |
|**etag** | **String** | etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An etag is returned in the response to GetDashboard, and users are expected to put that etag in the request to UpdateDashboard to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation. |  [optional] |
|**gridLayout** | [**GridLayout**](GridLayout.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels applied to the dashboard |  [optional] |
|**mosaicLayout** | [**MosaicLayout**](MosaicLayout.md) |  |  [optional] |
|**name** | **String** | Identifier. The resource name of the dashboard. |  [optional] |
|**rowLayout** | [**RowLayout**](RowLayout.md) |  |  [optional] |



