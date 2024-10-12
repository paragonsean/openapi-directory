

# PlaceActionLink

Represents a place action link and its attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the place action link was created. |  [optional] [readonly] |
|**isEditable** | **Boolean** | Output only. Indicates whether this link can be edited by the client. |  [optional] [readonly] |
|**isPreferred** | **Boolean** | Optional. Whether this link is preferred by the merchant. Only one link can be marked as preferred per place action type at a location. If a future request marks a different link as preferred for the same place action type, then the current preferred link (if any exists) will lose its preference. |  [optional] |
|**name** | **String** | Optional. The resource name, in the format &#x60;locations/{location_id}/placeActionLinks/{place_action_link_id}&#x60;. The name field will only be considered in UpdatePlaceActionLink and DeletePlaceActionLink requests for updating and deleting links respectively. However, it will be ignored in CreatePlaceActionLink request, where &#x60;place_action_link_id&#x60; will be assigned by the server on successful creation of a new link and returned as part of the response. |  [optional] |
|**placeActionType** | [**PlaceActionTypeEnum**](#PlaceActionTypeEnum) | Required. The type of place action that can be performed using this link. |  [optional] |
|**providerType** | [**ProviderTypeEnum**](#ProviderTypeEnum) | Output only. Specifies the provider type. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the place action link was last modified. |  [optional] [readonly] |
|**uri** | **String** | Required. The link uri. The same uri can be reused for different action types across different locations. However, only one place action link is allowed for each unique combination of (uri, place action type, location). |  [optional] |



## Enum: PlaceActionTypeEnum

| Name | Value |
|---- | -----|
| PLACE_ACTION_TYPE_UNSPECIFIED | &quot;PLACE_ACTION_TYPE_UNSPECIFIED&quot; |
| APPOINTMENT | &quot;APPOINTMENT&quot; |
| ONLINE_APPOINTMENT | &quot;ONLINE_APPOINTMENT&quot; |
| DINING_RESERVATION | &quot;DINING_RESERVATION&quot; |
| FOOD_ORDERING | &quot;FOOD_ORDERING&quot; |
| FOOD_DELIVERY | &quot;FOOD_DELIVERY&quot; |
| FOOD_TAKEOUT | &quot;FOOD_TAKEOUT&quot; |
| SHOP_ONLINE | &quot;SHOP_ONLINE&quot; |



## Enum: ProviderTypeEnum

| Name | Value |
|---- | -----|
| PROVIDER_TYPE_UNSPECIFIED | &quot;PROVIDER_TYPE_UNSPECIFIED&quot; |
| MERCHANT | &quot;MERCHANT&quot; |
| AGGREGATOR_3_P | &quot;AGGREGATOR_3P&quot; |



