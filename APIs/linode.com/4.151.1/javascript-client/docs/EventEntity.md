# LinodeApi.EventEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** | The unique ID for an Event&#39;s entity.   Some Event entities do not have IDs associated with them, so they will not be returned when filtering by ID. These Events include:   * &#x60;account&#x60;   * &#x60;profile&#x60;  Entities for some Events are assigned the ID of the Linode they correspond to. When filtering by ID for these Events, use the corresponding Linode&#39;s ID. These Events include:   * &#x60;disks&#x60;   * &#x60;backups&#x60;   Tag Events use a tag&#39;s name for the entity ID field. When filtering by ID for tag Events, supply the name of the tag.  | [optional] 
**label** | **String** | The current label of this object. The label may reflect changes that occur with this Event.  | [optional] 
**type** | **String** | The type of entity that is being referenced by the Event.  | [optional] [readonly] 
**url** | **String** | The URL where you can access the object this Event is for. If a relative URL, it is relative to the domain you retrieved the Event from.  | [optional] 



## Enum: TypeEnum


* `account` (value: `"account"`)

* `backups` (value: `"backups"`)

* `community` (value: `"community"`)

* `disks` (value: `"disks"`)

* `domain` (value: `"domain"`)

* `entity_transfer` (value: `"entity_transfer"`)

* `firewall` (value: `"firewall"`)

* `image` (value: `"image"`)

* `ipaddress` (value: `"ipaddress"`)

* `linode` (value: `"linode"`)

* `longview` (value: `"longview"`)

* `managed_service` (value: `"managed_service"`)

* `nodebalancer` (value: `"nodebalancer"`)

* `oauth_client` (value: `"oauth_client"`)

* `profile` (value: `"profile"`)

* `stackscript` (value: `"stackscript"`)

* `tag` (value: `"tag"`)

* `ticket` (value: `"ticket"`)

* `token` (value: `"token"`)

* `user` (value: `"user"`)

* `user_ssh_key` (value: `"user_ssh_key"`)

* `volume` (value: `"volume"`)




