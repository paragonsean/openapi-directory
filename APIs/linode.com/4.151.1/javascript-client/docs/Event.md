# LinodeApi.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The action that caused this Event. New actions may be added in the future.  | [optional] [readonly] 
**created** | **Date** | When this Event was created. | [optional] [readonly] 
**duration** | **Number** | The total duration in seconds that it takes for the Event to complete.  | [optional] [readonly] 
**entity** | [**EventEntity**](EventEntity.md) |  | [optional] 
**id** | **Number** | The unique ID of this Event. | [optional] [readonly] 
**message** | **String** | Provides additional information about the event. Additional information may include, but is not limited to, a more detailed representation of events which can help diagnose non-obvious failures.  | [optional] 
**percentComplete** | **Number** | A percentage estimating the amount of time remaining for an Event. Returns &#x60;null&#x60; for notification events.  | [optional] [readonly] 
**rate** | **String** | The rate of completion of the Event. Only some Events will return rate; for example, migration and resize Events.  | [optional] [readonly] 
**read** | **Boolean** | If this Event has been read. | [optional] [readonly] 
**secondaryEntity** | [**EventSecondaryEntity**](EventSecondaryEntity.md) |  | [optional] 
**seen** | **Boolean** | If this Event has been seen. | [optional] [readonly] 
**status** | **String** | The current status of this Event. | [optional] [readonly] 
**timeRemaining** | **String** | The estimated time remaining until the completion of this Event. This value is only returned for some in-progress migration events. For all other in-progress events, the &#x60;percent_complete&#x60; attribute will indicate about how much more work is to be done.  | [optional] [readonly] 
**username** | **String** | The username of the User who caused the Event.  | [optional] [readonly] 



## Enum: ActionEnum


* `account_update` (value: `"account_update"`)

* `account_settings_update` (value: `"account_settings_update"`)

* `backups_enable` (value: `"backups_enable"`)

* `backups_cancel` (value: `"backups_cancel"`)

* `backups_restore` (value: `"backups_restore"`)

* `community_question_reply` (value: `"community_question_reply"`)

* `community_like` (value: `"community_like"`)

* `credit_card_updated` (value: `"credit_card_updated"`)

* `disk_create` (value: `"disk_create"`)

* `disk_delete` (value: `"disk_delete"`)

* `disk_update` (value: `"disk_update"`)

* `disk_duplicate` (value: `"disk_duplicate"`)

* `disk_imagize` (value: `"disk_imagize"`)

* `disk_resize` (value: `"disk_resize"`)

* `dns_record_create` (value: `"dns_record_create"`)

* `dns_record_delete` (value: `"dns_record_delete"`)

* `dns_record_update` (value: `"dns_record_update"`)

* `dns_zone_create` (value: `"dns_zone_create"`)

* `dns_zone_delete` (value: `"dns_zone_delete"`)

* `dns_zone_import` (value: `"dns_zone_import"`)

* `dns_zone_update` (value: `"dns_zone_update"`)

* `entity_transfer_accept` (value: `"entity_transfer_accept"`)

* `entity_transfer_cancel` (value: `"entity_transfer_cancel"`)

* `entity_transfer_create` (value: `"entity_transfer_create"`)

* `entity_transfer_fail` (value: `"entity_transfer_fail"`)

* `entity_transfer_stale` (value: `"entity_transfer_stale"`)

* `firewall_create` (value: `"firewall_create"`)

* `firewall_delete` (value: `"firewall_delete"`)

* `firewall_disable` (value: `"firewall_disable"`)

* `firewall_enable` (value: `"firewall_enable"`)

* `firewall_update` (value: `"firewall_update"`)

* `firewall_device_add` (value: `"firewall_device_add"`)

* `firewall_device_remove` (value: `"firewall_device_remove"`)

* `host_reboot` (value: `"host_reboot"`)

* `image_delete` (value: `"image_delete"`)

* `image_update` (value: `"image_update"`)

* `image_upload` (value: `"image_upload"`)

* `ipaddress_update` (value: `"ipaddress_update"`)

* `lassie_reboot` (value: `"lassie_reboot"`)

* `lish_boot` (value: `"lish_boot"`)

* `linode_addip` (value: `"linode_addip"`)

* `linode_boot` (value: `"linode_boot"`)

* `linode_clone` (value: `"linode_clone"`)

* `linode_create` (value: `"linode_create"`)

* `linode_delete` (value: `"linode_delete"`)

* `linode_update` (value: `"linode_update"`)

* `linode_deleteip` (value: `"linode_deleteip"`)

* `linode_migrate` (value: `"linode_migrate"`)

* `linode_migrate_datacenter` (value: `"linode_migrate_datacenter"`)

* `linode_migrate_datacenter_create` (value: `"linode_migrate_datacenter_create"`)

* `linode_mutate` (value: `"linode_mutate"`)

* `linode_mutate_create` (value: `"linode_mutate_create"`)

* `linode_reboot` (value: `"linode_reboot"`)

* `linode_rebuild` (value: `"linode_rebuild"`)

* `linode_resize` (value: `"linode_resize"`)

* `linode_resize_create` (value: `"linode_resize_create"`)

* `linode_shutdown` (value: `"linode_shutdown"`)

* `linode_snapshot` (value: `"linode_snapshot"`)

* `linode_config_create` (value: `"linode_config_create"`)

* `linode_config_delete` (value: `"linode_config_delete"`)

* `linode_config_update` (value: `"linode_config_update"`)

* `lke_node_create` (value: `"lke_node_create"`)

* `longviewclient_create` (value: `"longviewclient_create"`)

* `longviewclient_delete` (value: `"longviewclient_delete"`)

* `longviewclient_update` (value: `"longviewclient_update"`)

* `managed_disabled` (value: `"managed_disabled"`)

* `managed_enabled` (value: `"managed_enabled"`)

* `managed_service_create` (value: `"managed_service_create"`)

* `managed_service_delete` (value: `"managed_service_delete"`)

* `nodebalancer_create` (value: `"nodebalancer_create"`)

* `nodebalancer_delete` (value: `"nodebalancer_delete"`)

* `nodebalancer_update` (value: `"nodebalancer_update"`)

* `nodebalancer_config_create` (value: `"nodebalancer_config_create"`)

* `nodebalancer_config_delete` (value: `"nodebalancer_config_delete"`)

* `nodebalancer_config_update` (value: `"nodebalancer_config_update"`)

* `nodebalancer_node_create` (value: `"nodebalancer_node_create"`)

* `nodebalancer_node_delete` (value: `"nodebalancer_node_delete"`)

* `nodebalancer_node_update` (value: `"nodebalancer_node_update"`)

* `oauth_client_create` (value: `"oauth_client_create"`)

* `oauth_client_delete` (value: `"oauth_client_delete"`)

* `oauth_client_secret_reset` (value: `"oauth_client_secret_reset"`)

* `oauth_client_update` (value: `"oauth_client_update"`)

* `password_reset` (value: `"password_reset"`)

* `payment_method_add` (value: `"payment_method_add"`)

* `payment_submitted` (value: `"payment_submitted"`)

* `profile_update` (value: `"profile_update"`)

* `stackscript_create` (value: `"stackscript_create"`)

* `stackscript_delete` (value: `"stackscript_delete"`)

* `stackscript_update` (value: `"stackscript_update"`)

* `stackscript_publicize` (value: `"stackscript_publicize"`)

* `stackscript_revise` (value: `"stackscript_revise"`)

* `tag_create` (value: `"tag_create"`)

* `tag_delete` (value: `"tag_delete"`)

* `tfa_disabled` (value: `"tfa_disabled"`)

* `tfa_enabled` (value: `"tfa_enabled"`)

* `ticket_attachment_upload` (value: `"ticket_attachment_upload"`)

* `ticket_create` (value: `"ticket_create"`)

* `ticket_update` (value: `"ticket_update"`)

* `token_create` (value: `"token_create"`)

* `token_delete` (value: `"token_delete"`)

* `token_update` (value: `"token_update"`)

* `user_create` (value: `"user_create"`)

* `user_update` (value: `"user_update"`)

* `user_delete` (value: `"user_delete"`)

* `user_ssh_key_add` (value: `"user_ssh_key_add"`)

* `user_ssh_key_delete` (value: `"user_ssh_key_delete"`)

* `user_ssh_key_update` (value: `"user_ssh_key_update"`)

* `vlan_attach` (value: `"vlan_attach"`)

* `vlan_detach` (value: `"vlan_detach"`)

* `volume_attach` (value: `"volume_attach"`)

* `volume_clone` (value: `"volume_clone"`)

* `volume_create` (value: `"volume_create"`)

* `volume_delete` (value: `"volume_delete"`)

* `volume_update` (value: `"volume_update"`)

* `volume_detach` (value: `"volume_detach"`)

* `volume_resize` (value: `"volume_resize"`)





## Enum: StatusEnum


* `failed` (value: `"failed"`)

* `finished` (value: `"finished"`)

* `notification` (value: `"notification"`)

* `scheduled` (value: `"scheduled"`)

* `started` (value: `"started"`)




