# ContentApiForShopping.AccountItemUpdatesSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowAvailabilityUpdates** | **Boolean** | If availability updates are enabled, any previous availability values get overwritten if Google finds an out-of-stock annotation on the offer&#39;s page. If additionally &#x60;allow_availability_updates&#x60; field is set to true, values get overwritten if Google finds an in-stock annotation on the offer’s page. | [optional] 
**allowConditionUpdates** | **Boolean** | If condition updates are enabled, Google always updates item condition with the condition detected from the details of your product. | [optional] 
**allowPriceUpdates** | **Boolean** | If price updates are enabled, Google always updates the active price with the crawled information. | [optional] 
**allowStrictAvailabilityUpdates** | **Boolean** | If allow_availability_updates is enabled, items are automatically updated in all your Shopping target countries. By default, availability updates will only be applied to items that are &#39;out of stock&#39; on your website but &#39;in stock&#39; on Shopping. Set this to true to also update items that are &#39;in stock&#39; on your website, but &#39;out of stock&#39; on Google Shopping. In order for this field to have an effect, you must also allow availability updates. | [optional] 


