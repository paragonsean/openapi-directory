

# Event

A collection of Event objects. An Event is an action taken against an entity related to your Account. For example, booting a Linode would create an Event. The Events returned depends on your grants. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The action that caused this Event. New actions may be added in the future.  |  [optional] [readonly] |
|**created** | **OffsetDateTime** | When this Event was created. |  [optional] [readonly] |
|**duration** | **BigDecimal** | The total duration in seconds that it takes for the Event to complete.  |  [optional] [readonly] |
|**entity** | [**EventEntity**](EventEntity.md) |  |  [optional] |
|**id** | **Integer** | The unique ID of this Event. |  [optional] [readonly] |
|**message** | **String** | Provides additional information about the event. Additional information may include, but is not limited to, a more detailed representation of events which can help diagnose non-obvious failures.  |  [optional] |
|**percentComplete** | **Integer** | A percentage estimating the amount of time remaining for an Event. Returns &#x60;null&#x60; for notification events.  |  [optional] [readonly] |
|**rate** | **String** | The rate of completion of the Event. Only some Events will return rate; for example, migration and resize Events.  |  [optional] [readonly] |
|**read** | **Boolean** | If this Event has been read. |  [optional] [readonly] |
|**secondaryEntity** | [**EventSecondaryEntity**](EventSecondaryEntity.md) |  |  [optional] |
|**seen** | **Boolean** | If this Event has been seen. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of this Event. |  [optional] [readonly] |
|**timeRemaining** | **String** | The estimated time remaining until the completion of this Event. This value is only returned for some in-progress migration events. For all other in-progress events, the &#x60;percent_complete&#x60; attribute will indicate about how much more work is to be done.  |  [optional] [readonly] |
|**username** | **String** | The username of the User who caused the Event.  |  [optional] [readonly] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACCOUNT_UPDATE | &quot;account_update&quot; |
| ACCOUNT_SETTINGS_UPDATE | &quot;account_settings_update&quot; |
| BACKUPS_ENABLE | &quot;backups_enable&quot; |
| BACKUPS_CANCEL | &quot;backups_cancel&quot; |
| BACKUPS_RESTORE | &quot;backups_restore&quot; |
| COMMUNITY_QUESTION_REPLY | &quot;community_question_reply&quot; |
| COMMUNITY_LIKE | &quot;community_like&quot; |
| CREDIT_CARD_UPDATED | &quot;credit_card_updated&quot; |
| DISK_CREATE | &quot;disk_create&quot; |
| DISK_DELETE | &quot;disk_delete&quot; |
| DISK_UPDATE | &quot;disk_update&quot; |
| DISK_DUPLICATE | &quot;disk_duplicate&quot; |
| DISK_IMAGIZE | &quot;disk_imagize&quot; |
| DISK_RESIZE | &quot;disk_resize&quot; |
| DNS_RECORD_CREATE | &quot;dns_record_create&quot; |
| DNS_RECORD_DELETE | &quot;dns_record_delete&quot; |
| DNS_RECORD_UPDATE | &quot;dns_record_update&quot; |
| DNS_ZONE_CREATE | &quot;dns_zone_create&quot; |
| DNS_ZONE_DELETE | &quot;dns_zone_delete&quot; |
| DNS_ZONE_IMPORT | &quot;dns_zone_import&quot; |
| DNS_ZONE_UPDATE | &quot;dns_zone_update&quot; |
| ENTITY_TRANSFER_ACCEPT | &quot;entity_transfer_accept&quot; |
| ENTITY_TRANSFER_CANCEL | &quot;entity_transfer_cancel&quot; |
| ENTITY_TRANSFER_CREATE | &quot;entity_transfer_create&quot; |
| ENTITY_TRANSFER_FAIL | &quot;entity_transfer_fail&quot; |
| ENTITY_TRANSFER_STALE | &quot;entity_transfer_stale&quot; |
| FIREWALL_CREATE | &quot;firewall_create&quot; |
| FIREWALL_DELETE | &quot;firewall_delete&quot; |
| FIREWALL_DISABLE | &quot;firewall_disable&quot; |
| FIREWALL_ENABLE | &quot;firewall_enable&quot; |
| FIREWALL_UPDATE | &quot;firewall_update&quot; |
| FIREWALL_DEVICE_ADD | &quot;firewall_device_add&quot; |
| FIREWALL_DEVICE_REMOVE | &quot;firewall_device_remove&quot; |
| HOST_REBOOT | &quot;host_reboot&quot; |
| IMAGE_DELETE | &quot;image_delete&quot; |
| IMAGE_UPDATE | &quot;image_update&quot; |
| IMAGE_UPLOAD | &quot;image_upload&quot; |
| IPADDRESS_UPDATE | &quot;ipaddress_update&quot; |
| LASSIE_REBOOT | &quot;lassie_reboot&quot; |
| LISH_BOOT | &quot;lish_boot&quot; |
| LINODE_ADDIP | &quot;linode_addip&quot; |
| LINODE_BOOT | &quot;linode_boot&quot; |
| LINODE_CLONE | &quot;linode_clone&quot; |
| LINODE_CREATE | &quot;linode_create&quot; |
| LINODE_DELETE | &quot;linode_delete&quot; |
| LINODE_UPDATE | &quot;linode_update&quot; |
| LINODE_DELETEIP | &quot;linode_deleteip&quot; |
| LINODE_MIGRATE | &quot;linode_migrate&quot; |
| LINODE_MIGRATE_DATACENTER | &quot;linode_migrate_datacenter&quot; |
| LINODE_MIGRATE_DATACENTER_CREATE | &quot;linode_migrate_datacenter_create&quot; |
| LINODE_MUTATE | &quot;linode_mutate&quot; |
| LINODE_MUTATE_CREATE | &quot;linode_mutate_create&quot; |
| LINODE_REBOOT | &quot;linode_reboot&quot; |
| LINODE_REBUILD | &quot;linode_rebuild&quot; |
| LINODE_RESIZE | &quot;linode_resize&quot; |
| LINODE_RESIZE_CREATE | &quot;linode_resize_create&quot; |
| LINODE_SHUTDOWN | &quot;linode_shutdown&quot; |
| LINODE_SNAPSHOT | &quot;linode_snapshot&quot; |
| LINODE_CONFIG_CREATE | &quot;linode_config_create&quot; |
| LINODE_CONFIG_DELETE | &quot;linode_config_delete&quot; |
| LINODE_CONFIG_UPDATE | &quot;linode_config_update&quot; |
| LKE_NODE_CREATE | &quot;lke_node_create&quot; |
| LONGVIEWCLIENT_CREATE | &quot;longviewclient_create&quot; |
| LONGVIEWCLIENT_DELETE | &quot;longviewclient_delete&quot; |
| LONGVIEWCLIENT_UPDATE | &quot;longviewclient_update&quot; |
| MANAGED_DISABLED | &quot;managed_disabled&quot; |
| MANAGED_ENABLED | &quot;managed_enabled&quot; |
| MANAGED_SERVICE_CREATE | &quot;managed_service_create&quot; |
| MANAGED_SERVICE_DELETE | &quot;managed_service_delete&quot; |
| NODEBALANCER_CREATE | &quot;nodebalancer_create&quot; |
| NODEBALANCER_DELETE | &quot;nodebalancer_delete&quot; |
| NODEBALANCER_UPDATE | &quot;nodebalancer_update&quot; |
| NODEBALANCER_CONFIG_CREATE | &quot;nodebalancer_config_create&quot; |
| NODEBALANCER_CONFIG_DELETE | &quot;nodebalancer_config_delete&quot; |
| NODEBALANCER_CONFIG_UPDATE | &quot;nodebalancer_config_update&quot; |
| NODEBALANCER_NODE_CREATE | &quot;nodebalancer_node_create&quot; |
| NODEBALANCER_NODE_DELETE | &quot;nodebalancer_node_delete&quot; |
| NODEBALANCER_NODE_UPDATE | &quot;nodebalancer_node_update&quot; |
| OAUTH_CLIENT_CREATE | &quot;oauth_client_create&quot; |
| OAUTH_CLIENT_DELETE | &quot;oauth_client_delete&quot; |
| OAUTH_CLIENT_SECRET_RESET | &quot;oauth_client_secret_reset&quot; |
| OAUTH_CLIENT_UPDATE | &quot;oauth_client_update&quot; |
| PASSWORD_RESET | &quot;password_reset&quot; |
| PAYMENT_METHOD_ADD | &quot;payment_method_add&quot; |
| PAYMENT_SUBMITTED | &quot;payment_submitted&quot; |
| PROFILE_UPDATE | &quot;profile_update&quot; |
| STACKSCRIPT_CREATE | &quot;stackscript_create&quot; |
| STACKSCRIPT_DELETE | &quot;stackscript_delete&quot; |
| STACKSCRIPT_UPDATE | &quot;stackscript_update&quot; |
| STACKSCRIPT_PUBLICIZE | &quot;stackscript_publicize&quot; |
| STACKSCRIPT_REVISE | &quot;stackscript_revise&quot; |
| TAG_CREATE | &quot;tag_create&quot; |
| TAG_DELETE | &quot;tag_delete&quot; |
| TFA_DISABLED | &quot;tfa_disabled&quot; |
| TFA_ENABLED | &quot;tfa_enabled&quot; |
| TICKET_ATTACHMENT_UPLOAD | &quot;ticket_attachment_upload&quot; |
| TICKET_CREATE | &quot;ticket_create&quot; |
| TICKET_UPDATE | &quot;ticket_update&quot; |
| TOKEN_CREATE | &quot;token_create&quot; |
| TOKEN_DELETE | &quot;token_delete&quot; |
| TOKEN_UPDATE | &quot;token_update&quot; |
| USER_CREATE | &quot;user_create&quot; |
| USER_UPDATE | &quot;user_update&quot; |
| USER_DELETE | &quot;user_delete&quot; |
| USER_SSH_KEY_ADD | &quot;user_ssh_key_add&quot; |
| USER_SSH_KEY_DELETE | &quot;user_ssh_key_delete&quot; |
| USER_SSH_KEY_UPDATE | &quot;user_ssh_key_update&quot; |
| VLAN_ATTACH | &quot;vlan_attach&quot; |
| VLAN_DETACH | &quot;vlan_detach&quot; |
| VOLUME_ATTACH | &quot;volume_attach&quot; |
| VOLUME_CLONE | &quot;volume_clone&quot; |
| VOLUME_CREATE | &quot;volume_create&quot; |
| VOLUME_DELETE | &quot;volume_delete&quot; |
| VOLUME_UPDATE | &quot;volume_update&quot; |
| VOLUME_DETACH | &quot;volume_detach&quot; |
| VOLUME_RESIZE | &quot;volume_resize&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| FAILED | &quot;failed&quot; |
| FINISHED | &quot;finished&quot; |
| NOTIFICATION | &quot;notification&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| STARTED | &quot;started&quot; |



