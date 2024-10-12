

# ApplicationGatewaySslCertificatePropertiesFormat

Properties of SSL certificates of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **String** | Base-64 encoded pfx certificate. Only applicable in PUT Request. |  [optional] |
|**password** | **String** | Password for the pfx file specified in data. Only applicable in PUT request. |  [optional] |
|**provisioningState** | **String** | Provisioning state of the SSL certificate resource Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicCertData** | **String** | Base-64 encoded Public cert data corresponding to pfx specified in data. Only applicable in GET request. |  [optional] |



