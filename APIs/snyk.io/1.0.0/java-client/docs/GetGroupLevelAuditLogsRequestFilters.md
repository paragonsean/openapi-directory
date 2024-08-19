

# GetGroupLevelAuditLogsRequestFilters


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
| GROUP_CLOUD_CONFIG_SETTINGS_EDIT | &quot;group.cloud_config.settings.edit&quot; |
| GROUP_CREATE | &quot;group.create&quot; |
| GROUP_DELETE | &quot;group.delete&quot; |
| GROUP_EDIT | &quot;group.edit&quot; |
| GROUP_FEATURE_FLAGS_EDIT | &quot;group.feature_flags.edit&quot; |
| GROUP_NOTIFICATION_SETTINGS_EDIT | &quot;group.notification_settings.edit&quot; |
| GROUP_ORG_ADD | &quot;group.org.add&quot; |
| GROUP_ORG_REMOVE | &quot;group.org.remove&quot; |
| GROUP_POLICY_CREATE | &quot;group.policy.create&quot; |
| GROUP_POLICY_DELETE | &quot;group.policy.delete&quot; |
| GROUP_POLICY_EDIT | &quot;group.policy.edit&quot; |
| GROUP_REQUEST_ACCESS_SETTINGS_EDIT | &quot;group.request_access_settings.edit&quot; |
| GROUP_ROLE_CREATE | &quot;group.role.create&quot; |
| GROUP_ROLE_EDIT | &quot;group.role.edit&quot; |
| GROUP_SERVICE_ACCOUNT_CREATE | &quot;group.service_account.create&quot; |
| GROUP_SERVICE_ACCOUNT_DELETE | &quot;group.service_account.delete&quot; |
| GROUP_SERVICE_ACCOUNT_EDIT | &quot;group.service_account.edit&quot; |
| GROUP_SETTINGS_EDIT | &quot;group.settings.edit&quot; |
| GROUP_SETTINGS_FEATURE_FLAG_EDIT | &quot;group.settings.feature_flag.edit&quot; |
| GROUP_SSO_AUTH0_CONNECTION_CREATE | &quot;group.sso.auth0_connection.create&quot; |
| GROUP_SSO_AUTH0_CONNECTION_EDIT | &quot;group.sso.auth0_connection.edit&quot; |
| GROUP_SSO_ADD | &quot;group.sso.add&quot; |
| GROUP_SSO_CREATE | &quot;group.sso.create&quot; |
| GROUP_SSO_DELETE | &quot;group.sso.delete&quot; |
| GROUP_SSO_EDIT | &quot;group.sso.edit&quot; |
| GROUP_SSO_MEMBERSHIP_SYNC | &quot;group.sso.membership.sync&quot; |
| GROUP_SSO_REMOVE | &quot;group.sso.remove&quot; |
| GROUP_TAG_CREATE | &quot;group.tag.create&quot; |
| GROUP_TAG_DELETE | &quot;group.tag.delete&quot; |
| GROUP_USER_ADD | &quot;group.user.add&quot; |
| GROUP_USER_PROVISION_ACCEPT | &quot;group.user.provision.accept&quot; |
| GROUP_USER_PROVISION_CREATE | &quot;group.user.provision.create&quot; |
| GROUP_USER_PROVISION_DELETE | &quot;group.user.provision.delete&quot; |
| GROUP_USER_REMOVE | &quot;group.user.remove&quot; |
| GROUP_USER_ROLE_EDIT | &quot;group.user.role.edit&quot; |



## Enum: ExcludeEventEnum

| Name | Value |
|---- | -----|
| API_ACCESS | &quot;api.access&quot; |
| GROUP_CLOUD_CONFIG_SETTINGS_EDIT | &quot;group.cloud_config.settings.edit&quot; |
| GROUP_CREATE | &quot;group.create&quot; |
| GROUP_DELETE | &quot;group.delete&quot; |
| GROUP_EDIT | &quot;group.edit&quot; |
| GROUP_FEATURE_FLAGS_EDIT | &quot;group.feature_flags.edit&quot; |
| GROUP_NOTIFICATION_SETTINGS_EDIT | &quot;group.notification_settings.edit&quot; |
| GROUP_ORG_ADD | &quot;group.org.add&quot; |
| GROUP_ORG_REMOVE | &quot;group.org.remove&quot; |
| GROUP_POLICY_CREATE | &quot;group.policy.create&quot; |
| GROUP_POLICY_DELETE | &quot;group.policy.delete&quot; |
| GROUP_POLICY_EDIT | &quot;group.policy.edit&quot; |
| GROUP_REQUEST_ACCESS_SETTINGS_EDIT | &quot;group.request_access_settings.edit&quot; |
| GROUP_ROLE_CREATE | &quot;group.role.create&quot; |
| GROUP_ROLE_EDIT | &quot;group.role.edit&quot; |
| GROUP_SERVICE_ACCOUNT_CREATE | &quot;group.service_account.create&quot; |
| GROUP_SERVICE_ACCOUNT_DELETE | &quot;group.service_account.delete&quot; |
| GROUP_SERVICE_ACCOUNT_EDIT | &quot;group.service_account.edit&quot; |
| GROUP_SETTINGS_EDIT | &quot;group.settings.edit&quot; |
| GROUP_SETTINGS_FEATURE_FLAG_EDIT | &quot;group.settings.feature_flag.edit&quot; |
| GROUP_SSO_AUTH0_CONNECTION_CREATE | &quot;group.sso.auth0_connection.create&quot; |
| GROUP_SSO_AUTH0_CONNECTION_EDIT | &quot;group.sso.auth0_connection.edit&quot; |
| GROUP_SSO_ADD | &quot;group.sso.add&quot; |
| GROUP_SSO_CREATE | &quot;group.sso.create&quot; |
| GROUP_SSO_DELETE | &quot;group.sso.delete&quot; |
| GROUP_SSO_EDIT | &quot;group.sso.edit&quot; |
| GROUP_SSO_MEMBERSHIP_SYNC | &quot;group.sso.membership.sync&quot; |
| GROUP_SSO_REMOVE | &quot;group.sso.remove&quot; |
| GROUP_TAG_CREATE | &quot;group.tag.create&quot; |
| GROUP_TAG_DELETE | &quot;group.tag.delete&quot; |
| GROUP_USER_ADD | &quot;group.user.add&quot; |
| GROUP_USER_PROVISION_ACCEPT | &quot;group.user.provision.accept&quot; |
| GROUP_USER_PROVISION_CREATE | &quot;group.user.provision.create&quot; |
| GROUP_USER_PROVISION_DELETE | &quot;group.user.provision.delete&quot; |
| GROUP_USER_REMOVE | &quot;group.user.remove&quot; |
| GROUP_USER_ROLE_EDIT | &quot;group.user.role.edit&quot; |



