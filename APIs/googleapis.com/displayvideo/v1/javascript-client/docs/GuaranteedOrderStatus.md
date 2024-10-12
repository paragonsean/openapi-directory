# DisplayVideo360Api.GuaranteedOrderStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configStatus** | **String** | Output only. The configuration status of the guaranteed order. Acceptable values are &#x60;PENDING&#x60; and &#x60;COMPLETED&#x60;. A guaranteed order must be configured (fill in the required fields, choose creatives, and select a default campaign) before it can serve. Currently the configuration action can only be performed via UI. | [optional] [readonly] 
**entityPauseReason** | **String** | The user-provided reason for pausing this guaranteed order. Must be UTF-8 encoded with a maximum length of 100 bytes. Only applicable when entity_status is set to &#x60;ENTITY_STATUS_PAUSED&#x60;. | [optional] 
**entityStatus** | **String** | Whether or not the guaranteed order is servable. Acceptable values are &#x60;ENTITY_STATUS_ACTIVE&#x60;, &#x60;ENTITY_STATUS_ARCHIVED&#x60;, and &#x60;ENTITY_STATUS_PAUSED&#x60;. Default value is &#x60;ENTITY_STATUS_ACTIVE&#x60;. | [optional] 



## Enum: ConfigStatusEnum


* `GUARANTEED_ORDER_CONFIG_STATUS_UNSPECIFIED` (value: `"GUARANTEED_ORDER_CONFIG_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `COMPLETED` (value: `"COMPLETED"`)





## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




