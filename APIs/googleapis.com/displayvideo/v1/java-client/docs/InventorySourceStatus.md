

# InventorySourceStatus

The status related settings of the inventory source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configStatus** | [**ConfigStatusEnum**](#ConfigStatusEnum) | Output only. The configuration status of the inventory source. Only applicable for guaranteed inventory sources. Acceptable values are &#x60;INVENTORY_SOURCE_CONFIG_STATUS_PENDING&#x60; and &#x60;INVENTORY_SOURCE_CONFIG_STATUS_COMPLETED&#x60;. An inventory source must be configured (fill in the required fields, choose creatives, and select a default campaign) before it can serve. |  [optional] [readonly] |
|**entityPauseReason** | **String** | The user-provided reason for pausing this inventory source. Must not exceed 100 characters. Only applicable when entity_status is set to &#x60;ENTITY_STATUS_PAUSED&#x60;. |  [optional] |
|**entityStatus** | [**EntityStatusEnum**](#EntityStatusEnum) | Whether or not the inventory source is servable. Acceptable values are &#x60;ENTITY_STATUS_ACTIVE&#x60;, &#x60;ENTITY_STATUS_ARCHIVED&#x60;, and &#x60;ENTITY_STATUS_PAUSED&#x60;. Default value is &#x60;ENTITY_STATUS_ACTIVE&#x60;. |  [optional] |
|**sellerPauseReason** | **String** | Output only. The seller-provided reason for pausing this inventory source. Only applicable for inventory sources synced directly from the publishers and when seller_status is set to &#x60;ENTITY_STATUS_PAUSED&#x60;. |  [optional] [readonly] |
|**sellerStatus** | [**SellerStatusEnum**](#SellerStatusEnum) | Output only. The status set by the seller for the inventory source. Only applicable for inventory sources synced directly from the publishers. Acceptable values are &#x60;ENTITY_STATUS_ACTIVE&#x60; and &#x60;ENTITY_STATUS_PAUSED&#x60;. |  [optional] [readonly] |



## Enum: ConfigStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INVENTORY_SOURCE_CONFIG_STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;INVENTORY_SOURCE_CONFIG_STATUS_PENDING&quot; |
| COMPLETED | &quot;INVENTORY_SOURCE_CONFIG_STATUS_COMPLETED&quot; |



## Enum: EntityStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ENTITY_STATUS_ACTIVE&quot; |
| ARCHIVED | &quot;ENTITY_STATUS_ARCHIVED&quot; |
| DRAFT | &quot;ENTITY_STATUS_DRAFT&quot; |
| PAUSED | &quot;ENTITY_STATUS_PAUSED&quot; |
| SCHEDULED_FOR_DELETION | &quot;ENTITY_STATUS_SCHEDULED_FOR_DELETION&quot; |



## Enum: SellerStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ENTITY_STATUS_ACTIVE&quot; |
| ARCHIVED | &quot;ENTITY_STATUS_ARCHIVED&quot; |
| DRAFT | &quot;ENTITY_STATUS_DRAFT&quot; |
| PAUSED | &quot;ENTITY_STATUS_PAUSED&quot; |
| SCHEDULED_FOR_DELETION | &quot;ENTITY_STATUS_SCHEDULED_FOR_DELETION&quot; |



