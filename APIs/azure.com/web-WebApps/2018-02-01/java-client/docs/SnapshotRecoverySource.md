

# SnapshotRecoverySource

Specifies the web app that snapshot contents will be retrieved from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ARM resource ID of the source app.  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName} for production slots and  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName} for other slots. |  [optional] |
|**location** | **String** | Geographical location of the source web app, e.g. SouthEastAsia, SouthCentralUS |  [optional] |



