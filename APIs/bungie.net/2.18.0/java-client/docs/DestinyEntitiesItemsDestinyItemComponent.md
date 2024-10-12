

# DestinyEntitiesItemsDestinyItemComponent

The base item component, filled with properties that are generally useful to know in any item request or that don't feel worthwhile to put in their own component.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindStatus** | **Integer** | If the item is bound to a location, it will be specified in this enum. |  [optional] |
|**bucketHash** | **Integer** | The hash identifier for the specific inventory bucket in which the item is located. |  [optional] |
|**expirationDate** | **OffsetDateTime** | If the item can expire, this is the date at which it will/did expire. |  [optional] |
|**isWrapper** | **Boolean** | If this is true, the object is actually a \&quot;wrapper\&quot; of the object it&#39;s representing. This means that it&#39;s not the actual item itself, but rather an item that must be \&quot;opened\&quot; in game before you have and can use the item.   Wrappers are an evolution of \&quot;bundles\&quot;, which give an easy way to let you preview the contents of what you purchased while still letting you get a refund before you \&quot;open\&quot; it. |  [optional] |
|**itemHash** | **Integer** | The identifier for the item&#39;s definition, which is where most of the useful static information for the item can be found. |  [optional] |
|**itemInstanceId** | **Long** | If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size. |  [optional] |
|**itemValueVisibility** | **List&lt;Boolean&gt;** | If available, a list that describes which item values (rewards) should be shown (true) or hidden (false). |  [optional] |
|**location** | **Integer** | An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items. |  [optional] |
|**lockable** | **Boolean** | If the item can be locked, this will indicate that state. |  [optional] |
|**metricHash** | **Integer** | The identifier for the currently-selected metric definition, to be displayed on the emblem nameplate. |  [optional] |
|**metricObjective** | [**DestinyQuestsDestinyObjectiveProgress**](DestinyQuestsDestinyObjectiveProgress.md) | The objective progress for the currently-selected metric definition, to be displayed on the emblem nameplate. |  [optional] |
|**overrideStyleItemHash** | **Integer** | If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.  If you don&#39;t do this, certain items whose styles are being overridden by socketed items - such as the \&quot;Recycle Shader\&quot; item - would show whatever their default icon/style is, and it wouldn&#39;t be pretty or look accurate. |  [optional] |
|**quantity** | **Integer** | The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it) |  [optional] |
|**state** | **Integer** | A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it&#39;s tracked or locked for example, or whether it has a masterwork plug inserted. |  [optional] |
|**tooltipNotificationIndexes** | **List&lt;Integer&gt;** | If this is populated, it is a list of indexes into DestinyInventoryItemDefinition.tooltipNotifications for any special tooltip messages that need to be shown for this item. |  [optional] |
|**transferStatus** | **Integer** | If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer). |  [optional] |
|**versionNumber** | **Integer** | The version of this item, used to index into the versions list in the item definition quality block. |  [optional] |



