# MyBusinessPlaceActionsApi.PlaceActionLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the place action link was created. | [optional] [readonly] 
**isEditable** | **Boolean** | Output only. Indicates whether this link can be edited by the client. | [optional] [readonly] 
**isPreferred** | **Boolean** | Optional. Whether this link is preferred by the merchant. Only one link can be marked as preferred per place action type at a location. If a future request marks a different link as preferred for the same place action type, then the current preferred link (if any exists) will lose its preference. | [optional] 
**name** | **String** | Optional. The resource name, in the format &#x60;locations/{location_id}/placeActionLinks/{place_action_link_id}&#x60;. The name field will only be considered in UpdatePlaceActionLink and DeletePlaceActionLink requests for updating and deleting links respectively. However, it will be ignored in CreatePlaceActionLink request, where &#x60;place_action_link_id&#x60; will be assigned by the server on successful creation of a new link and returned as part of the response. | [optional] 
**placeActionType** | **String** | Required. The type of place action that can be performed using this link. | [optional] 
**providerType** | **String** | Output only. Specifies the provider type. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the place action link was last modified. | [optional] [readonly] 
**uri** | **String** | Required. The link uri. The same uri can be reused for different action types across different locations. However, only one place action link is allowed for each unique combination of (uri, place action type, location). | [optional] 



## Enum: PlaceActionTypeEnum


* `PLACE_ACTION_TYPE_UNSPECIFIED` (value: `"PLACE_ACTION_TYPE_UNSPECIFIED"`)

* `APPOINTMENT` (value: `"APPOINTMENT"`)

* `ONLINE_APPOINTMENT` (value: `"ONLINE_APPOINTMENT"`)

* `DINING_RESERVATION` (value: `"DINING_RESERVATION"`)

* `FOOD_ORDERING` (value: `"FOOD_ORDERING"`)

* `FOOD_DELIVERY` (value: `"FOOD_DELIVERY"`)

* `FOOD_TAKEOUT` (value: `"FOOD_TAKEOUT"`)

* `SHOP_ONLINE` (value: `"SHOP_ONLINE"`)





## Enum: ProviderTypeEnum


* `PROVIDER_TYPE_UNSPECIFIED` (value: `"PROVIDER_TYPE_UNSPECIFIED"`)

* `MERCHANT` (value: `"MERCHANT"`)

* `AGGREGATOR_3P` (value: `"AGGREGATOR_3P"`)




