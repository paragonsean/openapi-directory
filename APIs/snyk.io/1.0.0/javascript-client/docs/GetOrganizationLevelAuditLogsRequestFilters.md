# SnykApi.GetOrganizationLevelAuditLogsRequestFilters

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

* `org.cloud_config.settings.edit` (value: `"org.cloud_config.settings.edit"`)

* `org.create` (value: `"org.create"`)

* `org.delete` (value: `"org.delete"`)

* `org.edit` (value: `"org.edit"`)

* `org.ignore_policy.edit` (value: `"org.ignore_policy.edit"`)

* `org.integration.create` (value: `"org.integration.create"`)

* `org.integration.delete` (value: `"org.integration.delete"`)

* `org.integration.edit` (value: `"org.integration.edit"`)

* `org.integration.settings.edit` (value: `"org.integration.settings.edit"`)

* `org.language_settings.edit` (value: `"org.language_settings.edit"`)

* `org.license_rule.create` (value: `"org.license_rule.create"`)

* `org.license_rule.delete` (value: `"org.license_rule.delete"`)

* `org.license_rule.edit` (value: `"org.license_rule.edit"`)

* `org.notification_settings.edit` (value: `"org.notification_settings.edit"`)

* `org.org_source.create` (value: `"org.org_source.create"`)

* `org.org_source.delete` (value: `"org.org_source.delete"`)

* `org.org_source.edit` (value: `"org.org_source.edit"`)

* `org.policy.edit` (value: `"org.policy.edit"`)

* `org.project.add` (value: `"org.project.add"`)

* `org.project.attributes.edit` (value: `"org.project.attributes.edit"`)

* `org.project.delete` (value: `"org.project.delete"`)

* `org.project.edit` (value: `"org.project.edit"`)

* `org.project.fix_pr.auto_open` (value: `"org.project.fix_pr.auto_open"`)

* `org.project.fix_pr.manual_open` (value: `"org.project.fix_pr.manual_open"`)

* `org.project.ignore.create` (value: `"org.project.ignore.create"`)

* `org.project.ignore.delete` (value: `"org.project.ignore.delete"`)

* `org.project.ignore.edit` (value: `"org.project.ignore.edit"`)

* `org.project.monitor` (value: `"org.project.monitor"`)

* `org.project.pr_check.edit` (value: `"org.project.pr_check.edit"`)

* `org.project.remove` (value: `"org.project.remove"`)

* `org.project.settings.delete` (value: `"org.project.settings.delete"`)

* `org.project.settings.edit` (value: `"org.project.settings.edit"`)

* `org.project.stop_monitor` (value: `"org.project.stop_monitor"`)

* `org.project.tag.add` (value: `"org.project.tag.add"`)

* `org.project.tag.remove` (value: `"org.project.tag.remove"`)

* `org.project.test` (value: `"org.project.test"`)

* `org.request_access_settings.edit` (value: `"org.request_access_settings.edit"`)

* `org.sast_settings.edit` (value: `"org.sast_settings.edit"`)

* `org.service_account.create` (value: `"org.service_account.create"`)

* `org.service_account.delete` (value: `"org.service_account.delete"`)

* `org.service_account.edit` (value: `"org.service_account.edit"`)

* `org.service_account.membership.upsert` (value: `"org.service_account.membership.upsert"`)

* `org.settings.feature_flag.edit` (value: `"org.settings.feature_flag.edit"`)

* `org.target.create` (value: `"org.target.create"`)

* `org.target.delete` (value: `"org.target.delete"`)

* `org.user.add` (value: `"org.user.add"`)

* `org.user.invite` (value: `"org.user.invite"`)

* `org.user.invite.accept` (value: `"org.user.invite.accept"`)

* `org.user.invite.revoke` (value: `"org.user.invite.revoke"`)

* `org.user.invite_link.accept` (value: `"org.user.invite_link.accept"`)

* `org.user.invite_link.create` (value: `"org.user.invite_link.create"`)

* `org.user.invite_link.revoke` (value: `"org.user.invite_link.revoke"`)

* `org.user.leave` (value: `"org.user.leave"`)

* `org.user.provision.accept` (value: `"org.user.provision.accept"`)

* `org.user.provision.create` (value: `"org.user.provision.create"`)

* `org.user.provision.delete` (value: `"org.user.provision.delete"`)

* `org.user.remove` (value: `"org.user.remove"`)

* `org.user.role.create` (value: `"org.user.role.create"`)

* `org.user.role.delete` (value: `"org.user.role.delete"`)

* `org.user.role.details.edit` (value: `"org.user.role.details.edit"`)

* `org.user.role.edit` (value: `"org.user.role.edit"`)

* `org.user.role.permissions.edit` (value: `"org.user.role.permissions.edit"`)

* `org.webhook.add` (value: `"org.webhook.add"`)

* `org.webhook.delete` (value: `"org.webhook.delete"`)





## Enum: ExcludeEventEnum


* `api.access` (value: `"api.access"`)

* `org.cloud_config.settings.edit` (value: `"org.cloud_config.settings.edit"`)

* `org.create` (value: `"org.create"`)

* `org.delete` (value: `"org.delete"`)

* `org.edit` (value: `"org.edit"`)

* `org.ignore_policy.edit` (value: `"org.ignore_policy.edit"`)

* `org.integration.create` (value: `"org.integration.create"`)

* `org.integration.delete` (value: `"org.integration.delete"`)

* `org.integration.edit` (value: `"org.integration.edit"`)

* `org.integration.settings.edit` (value: `"org.integration.settings.edit"`)

* `org.language_settings.edit` (value: `"org.language_settings.edit"`)

* `org.license_rule.create` (value: `"org.license_rule.create"`)

* `org.license_rule.delete` (value: `"org.license_rule.delete"`)

* `org.license_rule.edit` (value: `"org.license_rule.edit"`)

* `org.notification_settings.edit` (value: `"org.notification_settings.edit"`)

* `org.org_source.create` (value: `"org.org_source.create"`)

* `org.org_source.delete` (value: `"org.org_source.delete"`)

* `org.org_source.edit` (value: `"org.org_source.edit"`)

* `org.policy.edit` (value: `"org.policy.edit"`)

* `org.project.add` (value: `"org.project.add"`)

* `org.project.attributes.edit` (value: `"org.project.attributes.edit"`)

* `org.project.delete` (value: `"org.project.delete"`)

* `org.project.edit` (value: `"org.project.edit"`)

* `org.project.fix_pr.auto_open` (value: `"org.project.fix_pr.auto_open"`)

* `org.project.fix_pr.manual_open` (value: `"org.project.fix_pr.manual_open"`)

* `org.project.ignore.create` (value: `"org.project.ignore.create"`)

* `org.project.ignore.delete` (value: `"org.project.ignore.delete"`)

* `org.project.ignore.edit` (value: `"org.project.ignore.edit"`)

* `org.project.monitor` (value: `"org.project.monitor"`)

* `org.project.pr_check.edit` (value: `"org.project.pr_check.edit"`)

* `org.project.remove` (value: `"org.project.remove"`)

* `org.project.settings.delete` (value: `"org.project.settings.delete"`)

* `org.project.settings.edit` (value: `"org.project.settings.edit"`)

* `org.project.stop_monitor` (value: `"org.project.stop_monitor"`)

* `org.project.tag.add` (value: `"org.project.tag.add"`)

* `org.project.tag.remove` (value: `"org.project.tag.remove"`)

* `org.project.test` (value: `"org.project.test"`)

* `org.request_access_settings.edit` (value: `"org.request_access_settings.edit"`)

* `org.sast_settings.edit` (value: `"org.sast_settings.edit"`)

* `org.service_account.create` (value: `"org.service_account.create"`)

* `org.service_account.delete` (value: `"org.service_account.delete"`)

* `org.service_account.edit` (value: `"org.service_account.edit"`)

* `org.service_account.membership.upsert` (value: `"org.service_account.membership.upsert"`)

* `org.settings.feature_flag.edit` (value: `"org.settings.feature_flag.edit"`)

* `org.target.create` (value: `"org.target.create"`)

* `org.target.delete` (value: `"org.target.delete"`)

* `org.user.add` (value: `"org.user.add"`)

* `org.user.invite` (value: `"org.user.invite"`)

* `org.user.invite.accept` (value: `"org.user.invite.accept"`)

* `org.user.invite.revoke` (value: `"org.user.invite.revoke"`)

* `org.user.invite_link.accept` (value: `"org.user.invite_link.accept"`)

* `org.user.invite_link.create` (value: `"org.user.invite_link.create"`)

* `org.user.invite_link.revoke` (value: `"org.user.invite_link.revoke"`)

* `org.user.leave` (value: `"org.user.leave"`)

* `org.user.provision.accept` (value: `"org.user.provision.accept"`)

* `org.user.provision.create` (value: `"org.user.provision.create"`)

* `org.user.provision.delete` (value: `"org.user.provision.delete"`)

* `org.user.remove` (value: `"org.user.remove"`)

* `org.user.role.create` (value: `"org.user.role.create"`)

* `org.user.role.delete` (value: `"org.user.role.delete"`)

* `org.user.role.details.edit` (value: `"org.user.role.details.edit"`)

* `org.user.role.edit` (value: `"org.user.role.edit"`)

* `org.user.role.permissions.edit` (value: `"org.user.role.permissions.edit"`)

* `org.webhook.add` (value: `"org.webhook.add"`)

* `org.webhook.delete` (value: `"org.webhook.delete"`)




