# GoogleWorkspaceEventsApi.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority** | **String** | Output only. The user who authorized the creation of the subscription. Format: &#x60;users/{user}&#x60; For Google Workspace users, the &#x60;{user}&#x60; value is the [&#x60;user.id&#x60;](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users#User.FIELDS.ids) field from the Directory API. | [optional] [readonly] 
**createTime** | **String** | Output only. The time when the subscription is created. | [optional] [readonly] 
**etag** | **String** | Optional. This checksum is computed by the server based on the value of other fields, and might be sent on update requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**eventTypes** | **[String]** | Required. Immutable. Unordered list. Input for creating a subscription. Otherwise, output only. One or more types of events to receive about the target resource. Formatted according to the CloudEvents specification. The supported event types depend on the target resource of your subscription. For details, see [Supported Google Workspace events](https://developers.google.com/workspace/events/guides#supported-events). By default, you also receive events about the [lifecycle of your subscription](https://developers.google.com/workspace/events/guides/events-lifecycle). You don&#39;t need to specify lifecycle events for this field. If you specify an event type that doesn&#39;t exist for the target resource, the request returns an HTTP &#x60;400 Bad Request&#x60; status code. | [optional] 
**expireTime** | **String** | Non-empty default. The timestamp in UTC when the subscription expires. Always displayed on output, regardless of what was used on input. | [optional] 
**name** | **String** | Optional. Immutable. Identifier. Resource name of the subscription. Format: &#x60;subscriptions/{subscription}&#x60; | [optional] 
**notificationEndpoint** | [**NotificationEndpoint**](NotificationEndpoint.md) |  | [optional] 
**payloadOptions** | [**PayloadOptions**](PayloadOptions.md) |  | [optional] 
**reconciling** | **Boolean** | Output only. If &#x60;true&#x60;, the subscription is in the process of being updated. | [optional] [readonly] 
**state** | **String** | Output only. The state of the subscription. Determines whether the subscription can receive events and deliver them to the notification endpoint. | [optional] [readonly] 
**suspensionReason** | **String** | Output only. The error that suspended the subscription. To reactivate the subscription, resolve the error and call the &#x60;ReactivateSubscription&#x60; method. | [optional] [readonly] 
**targetResource** | **String** | Required. Immutable. The Google Workspace resource that&#39;s monitored for events, formatted as the [full resource name](https://google.aip.dev/122#full-resource-names). To learn about target resources and the events that they support, see [Supported Google Workspace events](https://developers.google.com/workspace/events#supported-events). A user can only authorize your app to create one subscription for a given target resource. If your app tries to create another subscription with the same user credentials, the request returns an &#x60;ALREADY_EXISTS&#x60; error. | [optional] 
**ttl** | **String** | Input only. The time-to-live (TTL) or duration for the subscription. If unspecified or set to &#x60;0&#x60;, uses the maximum possible duration. | [optional] 
**uid** | **String** | Output only. System-assigned unique identifier for the subscription. | [optional] [readonly] 
**updateTime** | **String** | Output only. The last time that the subscription is updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: SuspensionReasonEnum


* `ERROR_TYPE_UNSPECIFIED` (value: `"ERROR_TYPE_UNSPECIFIED"`)

* `USER_SCOPE_REVOKED` (value: `"USER_SCOPE_REVOKED"`)

* `RESOURCE_DELETED` (value: `"RESOURCE_DELETED"`)

* `USER_AUTHORIZATION_FAILURE` (value: `"USER_AUTHORIZATION_FAILURE"`)

* `ENDPOINT_PERMISSION_DENIED` (value: `"ENDPOINT_PERMISSION_DENIED"`)

* `ENDPOINT_NOT_FOUND` (value: `"ENDPOINT_NOT_FOUND"`)

* `ENDPOINT_RESOURCE_EXHAUSTED` (value: `"ENDPOINT_RESOURCE_EXHAUSTED"`)

* `OTHER` (value: `"OTHER"`)




