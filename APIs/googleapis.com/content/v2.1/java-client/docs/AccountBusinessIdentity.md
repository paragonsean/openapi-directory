

# AccountBusinessIdentity

The [business identity attributes](https://support.google.com/merchants/answer/10342414) can be used to self-declare attributes that let customers know more about your business.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blackOwned** | [**AccountIdentityType**](AccountIdentityType.md) |  |  [optional] |
|**includeForPromotions** | **Boolean** | Required. By setting this field, your business may be included in promotions for all the selected attributes. If you clear this option, it won&#39;t affect your identification with any of the attributes. For this field to be set, the merchant must self identify with at least one of the &#x60;AccountIdentityType&#x60;. If none are included, the request will be considered invalid. |  [optional] |
|**latinoOwned** | [**AccountIdentityType**](AccountIdentityType.md) |  |  [optional] |
|**smallBusiness** | [**AccountIdentityType**](AccountIdentityType.md) |  |  [optional] |
|**veteranOwned** | [**AccountIdentityType**](AccountIdentityType.md) |  |  [optional] |
|**womenOwned** | [**AccountIdentityType**](AccountIdentityType.md) |  |  [optional] |



