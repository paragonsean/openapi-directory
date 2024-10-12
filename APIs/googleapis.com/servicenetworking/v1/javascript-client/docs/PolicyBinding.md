# ServiceNetworkingApi.PolicyBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **String** | Required. Member to bind the role with. See /iam/docs/reference/rest/v1/Policy#Binding for how to format each member. Eg. - user:myuser@mydomain.com - serviceAccount:my-service-account@app.gserviceaccount.com | [optional] 
**role** | **String** | Required. Role to apply. Only allowlisted roles can be used at the specified granularity. The role must be one of the following: - &#39;roles/container.hostServiceAgentUser&#39; applied on the shared VPC host project - &#39;roles/compute.securityAdmin&#39; applied on the shared VPC host project - &#39;roles/compute.networkAdmin&#39; applied on the shared VPC host project - &#39;roles/compute.xpnAdmin&#39; applied on the shared VPC host project - &#39;roles/dns.admin&#39; applied on the shared VPC host project | [optional] 


