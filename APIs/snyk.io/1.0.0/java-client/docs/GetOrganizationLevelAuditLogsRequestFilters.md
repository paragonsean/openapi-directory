

# GetOrganizationLevelAuditLogsRequestFilters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | User email address. Will fetch only audit logs originated from this user&#39;s actions. Ignored if the userId filter is set. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) | Will return only logs for this specific event. Only one of event and excludeEvent may be specified in a request. |  [optional] |
|**excludeEvent** | [**ExcludeEventEnum**](#ExcludeEventEnum) | Will return logs except logs for this event. Only one of event and excludeEvent may be specified in a request. |  [optional] |
|**projectId** | **String** | Will return only logs for this specific project. |  [optional] |
|**userId** | **String** | User public ID. Will fetch only audit logs originated from this user&#39;s actions. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| API_ACCESS | &quot;api.access&quot; |
| ORG_CLOUD_CONFIG_SETTINGS_EDIT | &quot;org.cloud_config.settings.edit&quot; |
| ORG_CREATE | &quot;org.create&quot; |
| ORG_DELETE | &quot;org.delete&quot; |
| ORG_EDIT | &quot;org.edit&quot; |
| ORG_IGNORE_POLICY_EDIT | &quot;org.ignore_policy.edit&quot; |
| ORG_INTEGRATION_CREATE | &quot;org.integration.create&quot; |
| ORG_INTEGRATION_DELETE | &quot;org.integration.delete&quot; |
| ORG_INTEGRATION_EDIT | &quot;org.integration.edit&quot; |
| ORG_INTEGRATION_SETTINGS_EDIT | &quot;org.integration.settings.edit&quot; |
| ORG_LANGUAGE_SETTINGS_EDIT | &quot;org.language_settings.edit&quot; |
| ORG_LICENSE_RULE_CREATE | &quot;org.license_rule.create&quot; |
| ORG_LICENSE_RULE_DELETE | &quot;org.license_rule.delete&quot; |
| ORG_LICENSE_RULE_EDIT | &quot;org.license_rule.edit&quot; |
| ORG_NOTIFICATION_SETTINGS_EDIT | &quot;org.notification_settings.edit&quot; |
| ORG_ORG_SOURCE_CREATE | &quot;org.org_source.create&quot; |
| ORG_ORG_SOURCE_DELETE | &quot;org.org_source.delete&quot; |
| ORG_ORG_SOURCE_EDIT | &quot;org.org_source.edit&quot; |
| ORG_POLICY_EDIT | &quot;org.policy.edit&quot; |
| ORG_PROJECT_ADD | &quot;org.project.add&quot; |
| ORG_PROJECT_ATTRIBUTES_EDIT | &quot;org.project.attributes.edit&quot; |
| ORG_PROJECT_DELETE | &quot;org.project.delete&quot; |
| ORG_PROJECT_EDIT | &quot;org.project.edit&quot; |
| ORG_PROJECT_FIX_PR_AUTO_OPEN | &quot;org.project.fix_pr.auto_open&quot; |
| ORG_PROJECT_FIX_PR_MANUAL_OPEN | &quot;org.project.fix_pr.manual_open&quot; |
| ORG_PROJECT_IGNORE_CREATE | &quot;org.project.ignore.create&quot; |
| ORG_PROJECT_IGNORE_DELETE | &quot;org.project.ignore.delete&quot; |
| ORG_PROJECT_IGNORE_EDIT | &quot;org.project.ignore.edit&quot; |
| ORG_PROJECT_MONITOR | &quot;org.project.monitor&quot; |
| ORG_PROJECT_PR_CHECK_EDIT | &quot;org.project.pr_check.edit&quot; |
| ORG_PROJECT_REMOVE | &quot;org.project.remove&quot; |
| ORG_PROJECT_SETTINGS_DELETE | &quot;org.project.settings.delete&quot; |
| ORG_PROJECT_SETTINGS_EDIT | &quot;org.project.settings.edit&quot; |
| ORG_PROJECT_STOP_MONITOR | &quot;org.project.stop_monitor&quot; |
| ORG_PROJECT_TAG_ADD | &quot;org.project.tag.add&quot; |
| ORG_PROJECT_TAG_REMOVE | &quot;org.project.tag.remove&quot; |
| ORG_PROJECT_TEST | &quot;org.project.test&quot; |
| ORG_REQUEST_ACCESS_SETTINGS_EDIT | &quot;org.request_access_settings.edit&quot; |
| ORG_SAST_SETTINGS_EDIT | &quot;org.sast_settings.edit&quot; |
| ORG_SERVICE_ACCOUNT_CREATE | &quot;org.service_account.create&quot; |
| ORG_SERVICE_ACCOUNT_DELETE | &quot;org.service_account.delete&quot; |
| ORG_SERVICE_ACCOUNT_EDIT | &quot;org.service_account.edit&quot; |
| ORG_SERVICE_ACCOUNT_MEMBERSHIP_UPSERT | &quot;org.service_account.membership.upsert&quot; |
| ORG_SETTINGS_FEATURE_FLAG_EDIT | &quot;org.settings.feature_flag.edit&quot; |
| ORG_TARGET_CREATE | &quot;org.target.create&quot; |
| ORG_TARGET_DELETE | &quot;org.target.delete&quot; |
| ORG_USER_ADD | &quot;org.user.add&quot; |
| ORG_USER_INVITE | &quot;org.user.invite&quot; |
| ORG_USER_INVITE_ACCEPT | &quot;org.user.invite.accept&quot; |
| ORG_USER_INVITE_REVOKE | &quot;org.user.invite.revoke&quot; |
| ORG_USER_INVITE_LINK_ACCEPT | &quot;org.user.invite_link.accept&quot; |
| ORG_USER_INVITE_LINK_CREATE | &quot;org.user.invite_link.create&quot; |
| ORG_USER_INVITE_LINK_REVOKE | &quot;org.user.invite_link.revoke&quot; |
| ORG_USER_LEAVE | &quot;org.user.leave&quot; |
| ORG_USER_PROVISION_ACCEPT | &quot;org.user.provision.accept&quot; |
| ORG_USER_PROVISION_CREATE | &quot;org.user.provision.create&quot; |
| ORG_USER_PROVISION_DELETE | &quot;org.user.provision.delete&quot; |
| ORG_USER_REMOVE | &quot;org.user.remove&quot; |
| ORG_USER_ROLE_CREATE | &quot;org.user.role.create&quot; |
| ORG_USER_ROLE_DELETE | &quot;org.user.role.delete&quot; |
| ORG_USER_ROLE_DETAILS_EDIT | &quot;org.user.role.details.edit&quot; |
| ORG_USER_ROLE_EDIT | &quot;org.user.role.edit&quot; |
| ORG_USER_ROLE_PERMISSIONS_EDIT | &quot;org.user.role.permissions.edit&quot; |
| ORG_WEBHOOK_ADD | &quot;org.webhook.add&quot; |
| ORG_WEBHOOK_DELETE | &quot;org.webhook.delete&quot; |



## Enum: ExcludeEventEnum

| Name | Value |
|---- | -----|
| API_ACCESS | &quot;api.access&quot; |
| ORG_CLOUD_CONFIG_SETTINGS_EDIT | &quot;org.cloud_config.settings.edit&quot; |
| ORG_CREATE | &quot;org.create&quot; |
| ORG_DELETE | &quot;org.delete&quot; |
| ORG_EDIT | &quot;org.edit&quot; |
| ORG_IGNORE_POLICY_EDIT | &quot;org.ignore_policy.edit&quot; |
| ORG_INTEGRATION_CREATE | &quot;org.integration.create&quot; |
| ORG_INTEGRATION_DELETE | &quot;org.integration.delete&quot; |
| ORG_INTEGRATION_EDIT | &quot;org.integration.edit&quot; |
| ORG_INTEGRATION_SETTINGS_EDIT | &quot;org.integration.settings.edit&quot; |
| ORG_LANGUAGE_SETTINGS_EDIT | &quot;org.language_settings.edit&quot; |
| ORG_LICENSE_RULE_CREATE | &quot;org.license_rule.create&quot; |
| ORG_LICENSE_RULE_DELETE | &quot;org.license_rule.delete&quot; |
| ORG_LICENSE_RULE_EDIT | &quot;org.license_rule.edit&quot; |
| ORG_NOTIFICATION_SETTINGS_EDIT | &quot;org.notification_settings.edit&quot; |
| ORG_ORG_SOURCE_CREATE | &quot;org.org_source.create&quot; |
| ORG_ORG_SOURCE_DELETE | &quot;org.org_source.delete&quot; |
| ORG_ORG_SOURCE_EDIT | &quot;org.org_source.edit&quot; |
| ORG_POLICY_EDIT | &quot;org.policy.edit&quot; |
| ORG_PROJECT_ADD | &quot;org.project.add&quot; |
| ORG_PROJECT_ATTRIBUTES_EDIT | &quot;org.project.attributes.edit&quot; |
| ORG_PROJECT_DELETE | &quot;org.project.delete&quot; |
| ORG_PROJECT_EDIT | &quot;org.project.edit&quot; |
| ORG_PROJECT_FIX_PR_AUTO_OPEN | &quot;org.project.fix_pr.auto_open&quot; |
| ORG_PROJECT_FIX_PR_MANUAL_OPEN | &quot;org.project.fix_pr.manual_open&quot; |
| ORG_PROJECT_IGNORE_CREATE | &quot;org.project.ignore.create&quot; |
| ORG_PROJECT_IGNORE_DELETE | &quot;org.project.ignore.delete&quot; |
| ORG_PROJECT_IGNORE_EDIT | &quot;org.project.ignore.edit&quot; |
| ORG_PROJECT_MONITOR | &quot;org.project.monitor&quot; |
| ORG_PROJECT_PR_CHECK_EDIT | &quot;org.project.pr_check.edit&quot; |
| ORG_PROJECT_REMOVE | &quot;org.project.remove&quot; |
| ORG_PROJECT_SETTINGS_DELETE | &quot;org.project.settings.delete&quot; |
| ORG_PROJECT_SETTINGS_EDIT | &quot;org.project.settings.edit&quot; |
| ORG_PROJECT_STOP_MONITOR | &quot;org.project.stop_monitor&quot; |
| ORG_PROJECT_TAG_ADD | &quot;org.project.tag.add&quot; |
| ORG_PROJECT_TAG_REMOVE | &quot;org.project.tag.remove&quot; |
| ORG_PROJECT_TEST | &quot;org.project.test&quot; |
| ORG_REQUEST_ACCESS_SETTINGS_EDIT | &quot;org.request_access_settings.edit&quot; |
| ORG_SAST_SETTINGS_EDIT | &quot;org.sast_settings.edit&quot; |
| ORG_SERVICE_ACCOUNT_CREATE | &quot;org.service_account.create&quot; |
| ORG_SERVICE_ACCOUNT_DELETE | &quot;org.service_account.delete&quot; |
| ORG_SERVICE_ACCOUNT_EDIT | &quot;org.service_account.edit&quot; |
| ORG_SERVICE_ACCOUNT_MEMBERSHIP_UPSERT | &quot;org.service_account.membership.upsert&quot; |
| ORG_SETTINGS_FEATURE_FLAG_EDIT | &quot;org.settings.feature_flag.edit&quot; |
| ORG_TARGET_CREATE | &quot;org.target.create&quot; |
| ORG_TARGET_DELETE | &quot;org.target.delete&quot; |
| ORG_USER_ADD | &quot;org.user.add&quot; |
| ORG_USER_INVITE | &quot;org.user.invite&quot; |
| ORG_USER_INVITE_ACCEPT | &quot;org.user.invite.accept&quot; |
| ORG_USER_INVITE_REVOKE | &quot;org.user.invite.revoke&quot; |
| ORG_USER_INVITE_LINK_ACCEPT | &quot;org.user.invite_link.accept&quot; |
| ORG_USER_INVITE_LINK_CREATE | &quot;org.user.invite_link.create&quot; |
| ORG_USER_INVITE_LINK_REVOKE | &quot;org.user.invite_link.revoke&quot; |
| ORG_USER_LEAVE | &quot;org.user.leave&quot; |
| ORG_USER_PROVISION_ACCEPT | &quot;org.user.provision.accept&quot; |
| ORG_USER_PROVISION_CREATE | &quot;org.user.provision.create&quot; |
| ORG_USER_PROVISION_DELETE | &quot;org.user.provision.delete&quot; |
| ORG_USER_REMOVE | &quot;org.user.remove&quot; |
| ORG_USER_ROLE_CREATE | &quot;org.user.role.create&quot; |
| ORG_USER_ROLE_DELETE | &quot;org.user.role.delete&quot; |
| ORG_USER_ROLE_DETAILS_EDIT | &quot;org.user.role.details.edit&quot; |
| ORG_USER_ROLE_EDIT | &quot;org.user.role.edit&quot; |
| ORG_USER_ROLE_PERMISSIONS_EDIT | &quot;org.user.role.permissions.edit&quot; |
| ORG_WEBHOOK_ADD | &quot;org.webhook.add&quot; |
| ORG_WEBHOOK_DELETE | &quot;org.webhook.delete&quot; |



