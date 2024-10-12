# RocketServices.NavEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**[NavEntry]**](NavEntry.md) | Child nav entries. | [optional] 
**content** | [**NavContent**](NavContent.md) |  | [optional] 
**customFields** | **{String: Object}** | A map of custom fields defined by a curator for a nav entry. | [optional] 
**depth** | **Number** | The depth of the NavEntry (top level is 0) | 
**featured** | **Boolean** | True if this is a featured menu item.  Featured menu items may have a more prominent presentation than others in the navigation.  | [optional] 
**icon** | **String** | The icon for this nav entry. | [optional] 
**label** | **String** | The text label for this nav entry. | [optional] 
**path** | **String** | The path this nav entry links to. May be undefined if the nav entry is not clickable e.g. a nav heading. If the value begins with &#x60;http&#x60; then it&#39;s an external url.  | [optional] 


