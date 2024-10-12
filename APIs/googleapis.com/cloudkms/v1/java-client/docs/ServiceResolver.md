

# ServiceResolver

A ServiceResolver represents an EKM replica that can be reached within an EkmConnection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpointFilter** | **String** | Optional. The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. An endpoint will be chosen arbitrarily from the filtered list for each request. For endpoint filter syntax and examples, see https://cloud.google.com/service-directory/docs/reference/rpc/google.cloud.servicedirectory.v1#resolveservicerequest. |  [optional] |
|**hostname** | **String** | Required. The hostname of the EKM replica used at TLS and HTTP layers. |  [optional] |
|**serverCertificates** | [**List&lt;Certificate&gt;**](Certificate.md) | Required. A list of leaf server certificates used to authenticate HTTPS connections to the EKM replica. Currently, a maximum of 10 Certificate is supported. |  [optional] |
|**serviceDirectoryService** | **String** | Required. The resource name of the Service Directory service pointing to an EKM replica, in the format &#x60;projects/_*_/locations/_*_/namespaces/_*_/services/_*&#x60;. |  [optional] |



