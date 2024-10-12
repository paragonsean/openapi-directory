

# Administration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | The email address to send the received document to |  [optional] |
|**id** | **Long** | The Storecove assigned id for the Administration. |  [optional] |
|**legalEntityId** | **Long** | The LegalEntity the Administration belongs to. |  [optional] |
|**packageVersion** | [**PackageVersionEnum**](#PackageVersionEnum) | The version of the package. |  [optional] |
|**packaging** | [**PackagingEnum**](#PackagingEnum) | How to package the purchase invoice. |  [optional] |
|**senderEmailIdentityId** | **Long** | The id of the SenderEmailIdentity. If not provided, the Storecove default sender will be used |  [optional] |



## Enum: PackageVersionEnum

| Name | Value |
|---- | -----|
| PEPPOL_BIS_V3 | &quot;peppol_bis_v3&quot; |
| AUNZ | &quot;aunz&quot; |
| SG | &quot;sg&quot; |



## Enum: PackagingEnum

| Name | Value |
|---- | -----|
| UBL | &quot;ubl&quot; |



