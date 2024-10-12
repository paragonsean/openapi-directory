

# DnsBindPermission

DnsBindPermission resource that contains the accounts having the consumer DNS bind permission on the corresponding intranet VPC of the consumer project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. Output only. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource and location can only be global. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/global/dnsBindPermission&#x60; |  [optional] [readonly] |
|**principals** | [**List&lt;Principal&gt;**](Principal.md) | Output only. Users/Service accounts which have access for binding on the intranet VPC project corresponding to the consumer project. |  [optional] [readonly] |



