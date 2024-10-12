

# DelegatedProvidersList200ResponseValueInner

List of supported operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delegatedProviderSubscriptionId** | **String** | Parent DelegatedProvider subscription identifier. |  [optional] |
|**displayName** | **String** | Subscription name. |  [optional] |
|**externalReferenceId** | **String** | External reference identifier. |  [optional] |
|**id** | **String** | Fully qualified identifier. |  [optional] |
|**offerId** | **String** | Identifier of the offer under the scope of a delegated provider. |  [optional] |
|**owner** | **String** | Subscription owner. |  [optional] |
|**routingResourceManagerType** | [**RoutingResourceManagerTypeEnum**](#RoutingResourceManagerTypeEnum) | Resource manager type. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Subscription notification state. |  [optional] |
|**subscriptionId** | **String** | Subscription identifier. |  [optional] |
|**tenantId** | **String** | Directory tenant identifier. |  [optional] |



## Enum: RoutingResourceManagerTypeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| ADMIN | &quot;Admin&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NOT_DEFINED | &quot;NotDefined&quot; |
| ENABLED | &quot;Enabled&quot; |
| WARNED | &quot;Warned&quot; |
| PAST_DUE | &quot;PastDue&quot; |
| DISABLED | &quot;Disabled&quot; |
| DELETED | &quot;Deleted&quot; |
| DELETING | &quot;Deleting&quot; |
| PARTIALLY_DELETED | &quot;PartiallyDeleted&quot; |



