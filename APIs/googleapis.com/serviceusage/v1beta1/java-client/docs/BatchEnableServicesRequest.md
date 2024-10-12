

# BatchEnableServicesRequest

Request message for the `BatchEnableServices` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**serviceIds** | **List&lt;String&gt;** | The identifiers of the services to enable on the project. A valid identifier would be: serviceusage.googleapis.com Enabling services requires that each service is public or is shared with the user enabling the service. Two or more services must be specified. To enable a single service, use the &#x60;EnableService&#x60; method instead. A single request can enable a maximum of 20 services at a time. If more than 20 services are specified, the request will fail, and no state changes will occur. |  [optional] |



