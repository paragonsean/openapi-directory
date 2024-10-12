# ApigeeApi.GoogleCloudApigeeV1Organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addonsConfig** | [**GoogleCloudApigeeV1AddonsConfig**](GoogleCloudApigeeV1AddonsConfig.md) |  | [optional] 
**analyticsRegion** | **String** | Required. DEPRECATED: This field will eventually be deprecated and replaced with a differently-named field. Primary Google Cloud region for analytics data storage. For valid values, see [Create an Apigee organization](https://cloud.google.com/apigee/docs/api-platform/get-started/create-org). | [optional] 
**apiConsumerDataEncryptionKeyName** | **String** | Cloud KMS key name used for encrypting API consumer data. Required for US/EU regions when [BillingType](#BillingType) is &#x60;SUBSCRIPTION&#x60;. When [BillingType](#BillingType) is &#x60;EVALUATION&#x60; or the region is not US/EU, a Google-Managed encryption key will be used. Format: &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*&#x60; | [optional] 
**apiConsumerDataLocation** | **String** | This field is needed only for customers with control plane in US or EU. Apigee stores some control plane data only in single region. This field determines which single region Apigee should use. For example: \&quot;us-west1\&quot; when control plane is in US or \&quot;europe-west2\&quot; when control plane is in EU. | [optional] 
**apigeeProjectId** | **String** | Output only. Apigee Project ID associated with the organization. Use this project to allowlist Apigee in the Service Attachment when using private service connect with Apigee. | [optional] [readonly] 
**attributes** | **[String]** | Not used by Apigee. | [optional] 
**authorizedNetwork** | **String** | Compute Engine network used for Service Networking to be peered with Apigee runtime instances. See [Getting started with the Service Networking API](https://cloud.google.com/service-infrastructure/docs/service-networking/getting-started). Valid only when [RuntimeType](#RuntimeType) is set to &#x60;CLOUD&#x60;. The value must be set before the creation of a runtime instance and can be updated only when there are no runtime instances. For example: &#x60;default&#x60;. Apigee also supports shared VPC (that is, the host network project is not the same as the one that is peering with Apigee). See [Shared VPC overview](https://cloud.google.com/vpc/docs/shared-vpc). To use a shared VPC network, use the following format: &#x60;projects/{host-project-id}/{region}/networks/{network-name}&#x60;. For example: &#x60;projects/my-sharedvpc-host/global/networks/mynetwork&#x60; **Note:** Not supported for Apigee hybrid. | [optional] 
**billingType** | **String** | Billing type of the Apigee organization. See [Apigee pricing](https://cloud.google.com/apigee/pricing). | [optional] 
**caCertificate** | **Blob** | Output only. Base64-encoded public certificate for the root CA of the Apigee organization. Valid only when [RuntimeType](#RuntimeType) is &#x60;CLOUD&#x60;. | [optional] [readonly] 
**controlPlaneEncryptionKeyName** | **String** | Cloud KMS key name used for encrypting control plane data that is stored in a multi region. Required when [BillingType](#BillingType) is &#x60;SUBSCRIPTION&#x60;. When [BillingType](#BillingType) is &#x60;EVALUATION&#x60;, a Google-Managed encryption key will be used. Format: &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*&#x60; | [optional] 
**createdAt** | **String** | Output only. Time that the Apigee organization was created in milliseconds since epoch. | [optional] [readonly] 
**customerName** | **String** | Not used by Apigee. | [optional] 
**description** | **String** | Description of the Apigee organization. | [optional] 
**disableVpcPeering** | **Boolean** | Optional. Flag that specifies whether the VPC Peering through Private Google Access should be disabled between the consumer network and Apigee. Valid only when RuntimeType is set to CLOUD. Required if an authorizedNetwork on the consumer project is not provided, in which case the flag should be set to true. The value must be set before the creation of any Apigee runtime instance and can be updated only when there are no runtime instances. **Note:** Apigee will be deprecating the vpc peering model that requires you to provide &#39;authorizedNetwork&#39;, by making the non-peering model as the default way of provisioning Apigee organization in future. So, this will be a temporary flag to enable the transition. Not supported for Apigee hybrid. | [optional] 
**displayName** | **String** | Display name for the Apigee organization. Unused, but reserved for future use. | [optional] 
**environments** | **[String]** | Output only. List of environments in the Apigee organization. | [optional] [readonly] 
**expiresAt** | **String** | Output only. Time that the Apigee organization is scheduled for deletion. | [optional] [readonly] 
**lastModifiedAt** | **String** | Output only. Time that the Apigee organization was last modified in milliseconds since epoch. | [optional] [readonly] 
**name** | **String** | Output only. Name of the Apigee organization. | [optional] [readonly] 
**portalDisabled** | **Boolean** | Configuration for the Portals settings. | [optional] 
**projectId** | **String** | Output only. Project ID associated with the Apigee organization. | [optional] [readonly] 
**properties** | [**GoogleCloudApigeeV1Properties**](GoogleCloudApigeeV1Properties.md) |  | [optional] 
**runtimeDatabaseEncryptionKeyName** | **String** | Cloud KMS key name used for encrypting the data that is stored and replicated across runtime instances. Update is not allowed after the organization is created. Required when [RuntimeType](#RuntimeType) is &#x60;CLOUD&#x60;. If not specified when [RuntimeType](#RuntimeType) is &#x60;TRIAL&#x60;, a Google-Managed encryption key will be used. For example: \&quot;projects/foo/locations/us/keyRings/bar/cryptoKeys/baz\&quot;. **Note:** Not supported for Apigee hybrid. | [optional] 
**runtimeType** | **String** | Required. Runtime type of the Apigee organization based on the Apigee subscription purchased. | [optional] 
**state** | **String** | Output only. State of the organization. Values other than ACTIVE means the resource is not ready to use. | [optional] [readonly] 
**subscriptionPlan** | **String** | Output only. Subscription plan that the customer has purchased. Output only. | [optional] [readonly] 
**subscriptionType** | **String** | Output only. DEPRECATED: This will eventually be replaced by BillingType. Subscription type of the Apigee organization. Valid values include trial (free, limited, and for evaluation purposes only) or paid (full subscription has been purchased). See [Apigee pricing](https://cloud.google.com/apigee/pricing/). | [optional] [readonly] 
**type** | **String** | Not used by Apigee. | [optional] 



## Enum: BillingTypeEnum


* `BILLING_TYPE_UNSPECIFIED` (value: `"BILLING_TYPE_UNSPECIFIED"`)

* `SUBSCRIPTION` (value: `"SUBSCRIPTION"`)

* `EVALUATION` (value: `"EVALUATION"`)

* `PAYG` (value: `"PAYG"`)





## Enum: RuntimeTypeEnum


* `RUNTIME_TYPE_UNSPECIFIED` (value: `"RUNTIME_TYPE_UNSPECIFIED"`)

* `CLOUD` (value: `"CLOUD"`)

* `HYBRID` (value: `"HYBRID"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)





## Enum: SubscriptionPlanEnum


* `PLAN_UNSPECIFIED` (value: `"SUBSCRIPTION_PLAN_UNSPECIFIED"`)

* `2021` (value: `"SUBSCRIPTION_2021"`)

* `2024` (value: `"SUBSCRIPTION_2024"`)





## Enum: SubscriptionTypeEnum


* `SUBSCRIPTION_TYPE_UNSPECIFIED` (value: `"SUBSCRIPTION_TYPE_UNSPECIFIED"`)

* `PAID` (value: `"PAID"`)

* `TRIAL` (value: `"TRIAL"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `TRIAL` (value: `"TYPE_TRIAL"`)

* `PAID` (value: `"TYPE_PAID"`)

* `INTERNAL` (value: `"TYPE_INTERNAL"`)




