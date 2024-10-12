

# MigrateLinodeInstanceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**region** | **String** | The region to which the Linode will be migrated. Must be a valid region slug. A list of regions can be viewed by using the [GET /regions](/docs/api/regions/#regions-list) endpoint. A cross data center migration will cancel a pending migration that has not yet been initiated. A cross data center migration will initiate a &#x60;linode_migrate_datacenter_create&#x60; event.  |  [optional] |
|**upgrade** | **Boolean** | When initiating a cross DC migration, setting this value to true will also ensure that the Linode is upgraded to the latest generation of hardware that corresponds to your Linode&#39;s Type, if any free upgrades are available for it. If no free upgrades are available, and this value is set to true, then the endpoint will return a 400 error code and the migration will not be performed. If the data center set in the &#x60;region&#x60; field does not allow upgrades, then the endpoint will return a 400 error code and the migration will not be performed.  |  [optional] |



