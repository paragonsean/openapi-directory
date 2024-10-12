

# ApplicationGatewayConnectionDraining

Connection draining allows open connections to a backend server to be active for a specified time after the backend server got removed from the configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**drainTimeoutInSec** | **Integer** | The number of seconds connection draining is active. Acceptable values are from 1 second to 3600 seconds. |  |
|**enabled** | **Boolean** | Whether connection draining is enabled or not. |  |



