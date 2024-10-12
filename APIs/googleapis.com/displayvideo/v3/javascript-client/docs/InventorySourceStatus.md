# DisplayVideo360Api.InventorySourceStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configStatus** | **String** | Output only. The configuration status of the inventory source. Only applicable for guaranteed inventory sources. Acceptable values are &#x60;INVENTORY_SOURCE_CONFIG_STATUS_PENDING&#x60; and &#x60;INVENTORY_SOURCE_CONFIG_STATUS_COMPLETED&#x60;. An inventory source must be configured (fill in the required fields, choose creatives, and select a default campaign) before it can serve. | [optional] [readonly] 
**entityPauseReason** | **String** | The user-provided reason for pausing this inventory source. Must not exceed 100 characters. Only applicable when entity_status is set to &#x60;ENTITY_STATUS_PAUSED&#x60;. | [optional] 
**entityStatus** | **String** | Whether or not the inventory source is servable. Acceptable values are &#x60;ENTITY_STATUS_ACTIVE&#x60;, &#x60;ENTITY_STATUS_ARCHIVED&#x60;, and &#x60;ENTITY_STATUS_PAUSED&#x60;. Default value is &#x60;ENTITY_STATUS_ACTIVE&#x60;. | [optional] 
**sellerPauseReason** | **String** | Output only. The seller-provided reason for pausing this inventory source. Only applicable for inventory sources synced directly from the publishers and when seller_status is set to &#x60;ENTITY_STATUS_PAUSED&#x60;. | [optional] [readonly] 
**sellerStatus** | **String** | Output only. The status set by the seller for the inventory source. Only applicable for inventory sources synced directly from the publishers. Acceptable values are &#x60;ENTITY_STATUS_ACTIVE&#x60; and &#x60;ENTITY_STATUS_PAUSED&#x60;. | [optional] [readonly] 



## Enum: ConfigStatusEnum


* `UNSPECIFIED` (value: `"INVENTORY_SOURCE_CONFIG_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"INVENTORY_SOURCE_CONFIG_STATUS_PENDING"`)

* `COMPLETED` (value: `"INVENTORY_SOURCE_CONFIG_STATUS_COMPLETED"`)





## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)





## Enum: SellerStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




