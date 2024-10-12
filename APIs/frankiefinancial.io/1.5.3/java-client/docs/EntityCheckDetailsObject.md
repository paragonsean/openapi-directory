

# EntityCheckDetailsObject

Contains all the details we'll check regarding an Entity. It is assumed that this will grow over time.  Current supported check parameters:    - entity: The Entity we're checking. This must be supplied.   - deviceCheckDetails: |     An optional array of parameters for us to check the device and biometric characteristics against. This may map to a session key or device identifier, along with additional information that we can use to check against services like ThreatMetrix, BioCatch (or whatever has been configured for the Customer) 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceCheckDetails** | [**List&lt;DeviceCheckDetailsObject&gt;**](DeviceCheckDetailsObject.md) |  |  [optional] |
|**entity** | [**EntityObject**](EntityObject.md) |  |  |



