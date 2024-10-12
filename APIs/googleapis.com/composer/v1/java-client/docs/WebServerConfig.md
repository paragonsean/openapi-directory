

# WebServerConfig

The configuration settings for the Airflow web server App Engine instance. Supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**machineType** | **String** | Optional. Machine type on which Airflow web server is running. It has to be one of: composer-n1-webserver-2, composer-n1-webserver-4 or composer-n1-webserver-8. If not specified, composer-n1-webserver-2 will be used. Value custom is returned only in response, if Airflow web server parameters were manually changed to a non-standard values. |  [optional] |



