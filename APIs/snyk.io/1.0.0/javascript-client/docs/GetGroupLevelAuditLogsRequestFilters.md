# SnykApi.GetGroupLevelAuditLogsRequestFilters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | User email address. Will fetch only audit logs originated from this user&#39;s actions. Ignored if the userId filter is set. | [optional] 
**event** | **String** | Will return only logs for this specific event. Only one of event and excludeEvent may be specified in a request. | [optional] 
**excludeEvent** | **String** | Will return logs except logs for this event. Only one of event and excludeEvent may be specified in a request. | [optional] 
**projectId** | **String** | Will return only logs for this specific project. | [optional] 
**userId** | **String** | User public ID. Will fetch only audit logs originated from this user&#39;s actions. | [optional] 



## Enum: EventEnum


* `api.access` (value: `"api.access"`)

* `group.cloud_config.settings.edit` (value: `"group.cloud_config.settings.edit"`)

* `group.create` (value: `"group.create"`)

* `group.delete` (value: `"group.delete"`)

* `group.edit` (value: `"group.edit"`)

* `group.feature_flags.edit` (value: `"group.feature_flags.edit"`)

* `group.notification_settings.edit` (value: `"group.notification_settings.edit"`)

* `group.org.add` (value: `"group.org.add"`)

* `group.org.remove` (value: `"group.org.remove"`)

* `group.policy.create` (value: `"group.policy.create"`)

* `group.policy.delete` (value: `"group.policy.delete"`)

* `group.policy.edit` (value: `"group.policy.edit"`)

* `group.request_access_settings.edit` (value: `"group.request_access_settings.edit"`)

* `group.role.create` (value: `"group.role.create"`)

* `group.role.edit` (value: `"group.role.edit"`)

* `group.service_account.create` (value: `"group.service_account.create"`)

* `group.service_account.delete` (value: `"group.service_account.delete"`)

* `group.service_account.edit` (value: `"group.service_account.edit"`)

* `group.settings.edit` (value: `"group.settings.edit"`)

* `group.settings.feature_flag.edit` (value: `"group.settings.feature_flag.edit"`)

* `group.sso.auth0_connection.create` (value: `"group.sso.auth0_connection.create"`)

* `group.sso.auth0_connection.edit` (value: `"group.sso.auth0_connection.edit"`)

* `group.sso.add` (value: `"group.sso.add"`)

* `group.sso.create` (value: `"group.sso.create"`)

* `group.sso.delete` (value: `"group.sso.delete"`)

* `group.sso.edit` (value: `"group.sso.edit"`)

* `group.sso.membership.sync` (value: `"group.sso.membership.sync"`)

* `group.sso.remove` (value: `"group.sso.remove"`)

* `group.tag.create` (value: `"group.tag.create"`)

* `group.tag.delete` (value: `"group.tag.delete"`)

* `group.user.add` (value: `"group.user.add"`)

* `group.user.provision.accept` (value: `"group.user.provision.accept"`)

* `group.user.provision.create` (value: `"group.user.provision.create"`)

* `group.user.provision.delete` (value: `"group.user.provision.delete"`)

* `group.user.remove` (value: `"group.user.remove"`)

* `group.user.role.edit` (value: `"group.user.role.edit"`)





## Enum: ExcludeEventEnum


* `api.access` (value: `"api.access"`)

* `group.cloud_config.settings.edit` (value: `"group.cloud_config.settings.edit"`)

* `group.create` (value: `"group.create"`)

* `group.delete` (value: `"group.delete"`)

* `group.edit` (value: `"group.edit"`)

* `group.feature_flags.edit` (value: `"group.feature_flags.edit"`)

* `group.notification_settings.edit` (value: `"group.notification_settings.edit"`)

* `group.org.add` (value: `"group.org.add"`)

* `group.org.remove` (value: `"group.org.remove"`)

* `group.policy.create` (value: `"group.policy.create"`)

* `group.policy.delete` (value: `"group.policy.delete"`)

* `group.policy.edit` (value: `"group.policy.edit"`)

* `group.request_access_settings.edit` (value: `"group.request_access_settings.edit"`)

* `group.role.create` (value: `"group.role.create"`)

* `group.role.edit` (value: `"group.role.edit"`)

* `group.service_account.create` (value: `"group.service_account.create"`)

* `group.service_account.delete` (value: `"group.service_account.delete"`)

* `group.service_account.edit` (value: `"group.service_account.edit"`)

* `group.settings.edit` (value: `"group.settings.edit"`)

* `group.settings.feature_flag.edit` (value: `"group.settings.feature_flag.edit"`)

* `group.sso.auth0_connection.create` (value: `"group.sso.auth0_connection.create"`)

* `group.sso.auth0_connection.edit` (value: `"group.sso.auth0_connection.edit"`)

* `group.sso.add` (value: `"group.sso.add"`)

* `group.sso.create` (value: `"group.sso.create"`)

* `group.sso.delete` (value: `"group.sso.delete"`)

* `group.sso.edit` (value: `"group.sso.edit"`)

* `group.sso.membership.sync` (value: `"group.sso.membership.sync"`)

* `group.sso.remove` (value: `"group.sso.remove"`)

* `group.tag.create` (value: `"group.tag.create"`)

* `group.tag.delete` (value: `"group.tag.delete"`)

* `group.user.add` (value: `"group.user.add"`)

* `group.user.provision.accept` (value: `"group.user.provision.accept"`)

* `group.user.provision.create` (value: `"group.user.provision.create"`)

* `group.user.provision.delete` (value: `"group.user.provision.delete"`)

* `group.user.remove` (value: `"group.user.remove"`)

* `group.user.role.edit` (value: `"group.user.role.edit"`)




