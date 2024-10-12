

# GoogleCloudDiscoveryengineV1betaPanelInfo

Detailed panel information associated with a user event.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The display name of the panel. |  [optional] |
|**panelId** | **String** | Required. The panel ID. |  [optional] |
|**panelPosition** | **Integer** | The ordered position of the panel, if shown to the user with other panels. If set, then total_panels must also be set. |  [optional] |
|**totalPanels** | **Integer** | The total number of panels, including this one, shown to the user. Must be set if panel_position is set. |  [optional] |



