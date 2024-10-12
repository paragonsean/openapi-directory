

# GoogleCloudChannelV1CloudIdentityInfo

Cloud Identity information for the Cloud Channel Customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminConsoleUri** | **String** | Output only. URI of Customer&#39;s Admin console dashboard. |  [optional] [readonly] |
|**alternateEmail** | **String** | The alternate email. |  [optional] |
|**customerType** | [**CustomerTypeEnum**](#CustomerTypeEnum) | CustomerType indicates verification type needed for using services. |  [optional] |
|**eduData** | [**GoogleCloudChannelV1EduData**](GoogleCloudChannelV1EduData.md) |  |  [optional] |
|**isDomainVerified** | **Boolean** | Output only. Whether the domain is verified. This field is not returned for a Customer&#39;s cloud_identity_info resource. Partners can use the domains.get() method of the Workspace SDK&#39;s Directory API, or listen to the PRIMARY_DOMAIN_VERIFIED Pub/Sub event in to track domain verification of their resolve Workspace customers. |  [optional] [readonly] |
|**languageCode** | **String** | Language code. |  [optional] |
|**phoneNumber** | **String** | Phone number associated with the Cloud Identity. |  [optional] |
|**primaryDomain** | **String** | Output only. The primary domain name. |  [optional] [readonly] |



## Enum: CustomerTypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_TYPE_UNSPECIFIED | &quot;CUSTOMER_TYPE_UNSPECIFIED&quot; |
| DOMAIN | &quot;DOMAIN&quot; |
| TEAM | &quot;TEAM&quot; |



