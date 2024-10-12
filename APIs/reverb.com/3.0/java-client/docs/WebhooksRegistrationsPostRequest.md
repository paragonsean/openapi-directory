

# WebhooksRegistrationsPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topic** | [**TopicEnum**](#TopicEnum) | Valid values: listings/update, listings/publish, listings/bumps-ran-out, orders/create, orders/update, payments/create, payments/update, app/uninstalled |  |
|**url** | **String** |  |  |



## Enum: TopicEnum

| Name | Value |
|---- | -----|
| LISTINGS_UPDATE | &quot;listings/update&quot; |
| LISTINGS_PUBLISH | &quot;listings/publish&quot; |
| LISTINGS_BUMPS_RAN_OUT | &quot;listings/bumps-ran-out&quot; |
| ORDERS_CREATE | &quot;orders/create&quot; |
| ORDERS_UPDATE | &quot;orders/update&quot; |
| PAYMENTS_CREATE | &quot;payments/create&quot; |
| PAYMENTS_UPDATE | &quot;payments/update&quot; |
| APP_UNINSTALLED | &quot;app/uninstalled&quot; |



