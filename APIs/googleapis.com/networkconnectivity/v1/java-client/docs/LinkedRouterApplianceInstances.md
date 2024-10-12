

# LinkedRouterApplianceInstances

A collection of router appliance instances. If you configure multiple router appliance instances to receive data from the same set of sites outside of Google Cloud, we recommend that you associate those instances with the same spoke.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instances** | [**List&lt;RouterApplianceInstance&gt;**](RouterApplianceInstance.md) | The list of router appliance instances. |  [optional] |
|**siteToSiteDataTransfer** | **Boolean** | A value that controls whether site-to-site data transfer is enabled for these resources. Data transfer is available only in [supported locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). |  [optional] |
|**vpcNetwork** | **String** | Output only. The VPC network where these router appliance instances are located. |  [optional] [readonly] |



