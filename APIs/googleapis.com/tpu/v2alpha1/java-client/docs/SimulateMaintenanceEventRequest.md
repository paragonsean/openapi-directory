

# SimulateMaintenanceEventRequest

Request for SimulateMaintenanceEvent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workerIds** | **List&lt;String&gt;** | The 0-based worker ID. If it is empty, worker ID 0 will be selected for maintenance event simulation. A maintenance event will only be fired on the first specified worker ID. Future implementations may support firing on multiple workers. |  [optional] |



