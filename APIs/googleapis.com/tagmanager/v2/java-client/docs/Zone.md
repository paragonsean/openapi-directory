

# Zone

Represents a Google Tag Manager Zone's contents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**boundary** | [**ZoneBoundary**](ZoneBoundary.md) |  |  [optional] |
|**childContainer** | [**List&lt;ZoneChildContainer&gt;**](ZoneChildContainer.md) | Containers that are children of this Zone. |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Zone as computed at storage time. This value is recomputed whenever the zone is modified. |  [optional] |
|**name** | **String** | Zone display name. |  [optional] |
|**notes** | **String** | User notes on how to apply this zone in the container. |  [optional] |
|**path** | **String** | GTM Zone&#39;s API relative path. |  [optional] |
|**tagManagerUrl** | **String** | Auto generated link to the tag manager UI |  [optional] |
|**typeRestriction** | [**ZoneTypeRestriction**](ZoneTypeRestriction.md) |  |  [optional] |
|**workspaceId** | **String** | GTM Workspace ID. |  [optional] |
|**zoneId** | **String** | The Zone ID uniquely identifies the GTM Zone. |  [optional] |



