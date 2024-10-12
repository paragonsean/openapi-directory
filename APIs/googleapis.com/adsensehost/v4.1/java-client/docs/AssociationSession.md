

# AssociationSession


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Hosted account id of the associated publisher after association. Present if status is ACCEPTED. |  [optional] |
|**id** | **String** | Unique identifier of this association session. |  [optional] |
|**kind** | **String** | Kind of resource this is, in this case adsensehost#associationSession. |  [optional] |
|**productCodes** | **List&lt;String&gt;** | The products to associate with the user. Options: AFC, AFG, AFV, AFS (deprecated), AFMC (deprecated) |  [optional] |
|**redirectUrl** | **String** | Redirect URL of this association session. Used to redirect users into the AdSense association flow. |  [optional] |
|**status** | **String** | Status of the completed association, available once the association callback token has been verified. One of ACCEPTED, REJECTED, or ERROR. |  [optional] |
|**userLocale** | **String** | The preferred locale of the user themselves when going through the AdSense association flow. |  [optional] |
|**websiteLocale** | **String** | The locale of the user&#39;s hosted website. |  [optional] |
|**websiteUrl** | **String** | The URL of the user&#39;s hosted website. |  [optional] |



