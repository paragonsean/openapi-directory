# CloudDataprocApi.StartupConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requiredRegistrationFraction** | **Number** | Optional. The config setting to enable cluster creation/ updation to be successful only after required_registration_fraction of instances are up and running. This configuration is applicable to only secondary workers for now. The cluster will fail if required_registration_fraction of instances are not available. This will include instance creation, agent registration, and service registration (if enabled). | [optional] 


