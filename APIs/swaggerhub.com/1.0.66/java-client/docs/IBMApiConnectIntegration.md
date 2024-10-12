

# IBMApiConnectIntegration

Configuration details for the [IBM API Connect](https://support.smartbear.com/swaggerhub/docs/integrations/ibm-api-connect.html) integration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether the integration is enabled or disabled |  [optional] |
|**id** | **UUID** | ID of the integration |  [optional] [readonly] |
|**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. |  |
|**apiId** | **String** | The name of the API in your IBM Cloud organization to publish to. If left blank, a new API will be created when the integration is triggered. When specified, any existing API definition will be overwritten. |  [optional] |
|**apiKey** | **String** | IBM Cloud API Key, obtain a key via https://cloud.ibm.com/iam/apikeys. Write-only property. Required to create and update the integration. |  [optional] |
|**configType** | [**ConfigTypeEnum**](#ConfigTypeEnum) | Integration type |  |
|**orgDisplayName** | **String** | The organization display name under your IBM Cloud account |  [optional] [readonly] |
|**orgId** | **String** | The organization under your IBM Cloud account to which you want to deploy your API. Can be specified by ID or name.  The organization ID is an alphanumeric string like &#x60;680ee27a0cf28d61b4e9a462&#x60;. The organization name uses the format &#x60;&lt;cloudFoundryOrgName&gt;-&lt;spaceName&gt;&#x60;, where &#x60;&lt;cloudFoundryOrgName&gt;&#x60; is your Cloud Foundry organization name changed to lowercase and with non-alphanumeric characters removed.  The easiest way to find the value for &#x60;orgId&#x60; is to start configuring the IBM integration in SwaggerHub UI. After you authenticate using an IBM API key, you will see a list of organizations in the format \&quot;CFOrgName (SpaceName) (OrgId)\&quot;. The value in the last parentheses is the &#x60;orgId&#x60;.  Alternatively, if you have the [API Connect Developer Toolkit](https://www.npmjs.com/package/apiconnect) installed, you can use the &#x60;apic orgs --server apimanager.us-south.apiconnect.cloud.ibm.com&#x60; command to get the organization names that can be used as &#x60;orgId&#x60;. |  |



## Enum: ConfigTypeEnum

| Name | Value |
|---- | -----|
| IBM_API_CONNECT | &quot;IBM_API_CONNECT&quot; |



