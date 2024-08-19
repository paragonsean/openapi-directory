

# Plan

Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The plan ID. |  [optional] |
|**product** | **String** | Specifies the product of the image from the marketplace. This is the same value as Offer under the imageReference element. |  [optional] |
|**promotionCode** | **String** | The promotion code. |  [optional] |
|**publisher** | **String** | The publisher ID. |  [optional] |



