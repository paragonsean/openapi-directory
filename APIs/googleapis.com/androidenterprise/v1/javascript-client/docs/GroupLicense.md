# GooglePlayEmmApi.GroupLicense

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisitionKind** | **String** | How this group license was acquired. \&quot;bulkPurchase\&quot; means that this Grouplicenses resource was created because the enterprise purchased licenses for this product; otherwise, the value is \&quot;free\&quot; (for free products). | [optional] 
**approval** | **String** | Whether the product to which this group license relates is currently approved by the enterprise. Products are approved when a group license is first created, but this approval may be revoked by an enterprise admin via Google Play. Unapproved products will not be visible to end users in collections, and new entitlements to them should not normally be created. | [optional] 
**numProvisioned** | **Number** | The total number of provisioned licenses for this product. Returned by read operations, but ignored in write operations. | [optional] 
**numPurchased** | **Number** | The number of purchased licenses (possibly in multiple purchases). If this field is omitted, then there is no limit on the number of licenses that can be provisioned (for example, if the acquisition kind is \&quot;free\&quot;). | [optional] 
**permissions** | **String** | The permission approval status of the product. This field is only set if the product is approved. Possible states are: - \&quot;currentApproved\&quot;, the current set of permissions is approved, but additional permissions will require the administrator to reapprove the product (If the product was approved without specifying the approved permissions setting, then this is the default behavior.), - \&quot;needsReapproval\&quot;, the product has unapproved permissions. No additional product licenses can be assigned until the product is reapproved, - \&quot;allCurrentAndFutureApproved\&quot;, the current permissions are approved and any future permission updates will be automatically approved without administrator review.  | [optional] 
**productId** | **String** | The ID of the product that the license is for. For example, \&quot;app:com.google.android.gm\&quot;. | [optional] 



## Enum: AcquisitionKindEnum


* `free` (value: `"free"`)

* `bulkPurchase` (value: `"bulkPurchase"`)





## Enum: ApprovalEnum


* `approved` (value: `"approved"`)

* `unapproved` (value: `"unapproved"`)





## Enum: PermissionsEnum


* `currentApproved` (value: `"currentApproved"`)

* `needsReapproval` (value: `"needsReapproval"`)

* `allCurrentAndFutureApproved` (value: `"allCurrentAndFutureApproved"`)




