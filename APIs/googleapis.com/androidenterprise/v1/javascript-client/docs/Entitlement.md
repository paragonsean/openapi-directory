# GooglePlayEmmApi.Entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**productId** | **String** | The ID of the product that the entitlement is for. For example, \&quot;app:com.google.android.gm\&quot;. | [optional] 
**reason** | **String** | The reason for the entitlement. For example, \&quot;free\&quot; for free apps. This property is temporary: it will be replaced by the acquisition kind field of group licenses. | [optional] 



## Enum: ReasonEnum


* `free` (value: `"free"`)

* `groupLicense` (value: `"groupLicense"`)

* `userPurchase` (value: `"userPurchase"`)




