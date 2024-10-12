# CloudComposerApi.DatabaseConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machineType** | **String** | Optional. Cloud SQL machine type used by Airflow database. It has to be one of: db-n1-standard-2, db-n1-standard-4, db-n1-standard-8 or db-n1-standard-16. If not specified, db-n1-standard-2 will be used. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. | [optional] 
**zone** | **String** | Optional. The Compute Engine zone where the Airflow database is created. If zone is provided, it must be in the region selected for the environment. If zone is not provided, a zone is automatically selected. The zone can only be set during environment creation. Supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.*. | [optional] 


