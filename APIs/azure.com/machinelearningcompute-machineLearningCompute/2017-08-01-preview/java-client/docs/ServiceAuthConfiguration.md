

# ServiceAuthConfiguration

Global service auth configuration properties. These are the data-plane authorization keys and are used if a service doesn't define it's own.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**primaryAuthKeyHash** | **String** | The primary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API. |  |
|**secondaryAuthKeyHash** | **String** | The secondary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API. |  |



