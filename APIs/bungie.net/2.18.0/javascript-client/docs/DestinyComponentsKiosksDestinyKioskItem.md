# BungieNetApi.DestinyComponentsKiosksDestinyKioskItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canAcquire** | **Boolean** | If true, the user can not only see the item, but they can acquire it. It is possible that a user can see a kiosk item and not be able to acquire it. | [optional] 
**failureIndexes** | **[Number]** | Indexes into failureStrings for the Vendor, indicating the reasons why it failed if any. | [optional] 
**flavorObjective** | [**DestinyQuestsDestinyObjectiveProgress**](DestinyQuestsDestinyObjectiveProgress.md) | I may regret naming it this way - but this represents when an item has an objective that doesn&#39;t serve a beneficial purpose, but rather is used for \&quot;flavor\&quot; or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item. | [optional] 
**index** | **Number** | The index of the item in the related DestinyVendorDefintion&#39;s itemList property, representing the sale. | [optional] 


