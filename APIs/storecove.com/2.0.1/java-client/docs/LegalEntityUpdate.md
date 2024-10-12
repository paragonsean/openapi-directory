

# LegalEntityUpdate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertisements** | [**List&lt;AdvertisementsEnum&gt;**](#List&lt;AdvertisementsEnum&gt;) | A list of document types to advertise. Use if this LegalEntity needs the ability to receive more than only invoice documents. |  [optional] |
|**city** | **String** | The city. |  [optional] |
|**country** | **Country** |  |  [optional] |
|**county** | **String** | County, if applicable |  [optional] |
|**id** | **Long** | The Storecove assigned id for the LegalEntity. |  [optional] |
|**line1** | **String** | The first address line. |  [optional] |
|**line2** | **String** | The second address line, if applicable |  [optional] |
|**partyName** | **String** | The name of the company. |  [optional] |
|**_public** | **Boolean** | Whether or not this LegalEntity is public. Public means it will be listed in the PEPPOL directory at https://directory.peppol.eu/ which is normally what you want. If you have a good reason to not want the LegalEntity listed, provide false. This property is ignored when for country SG, where it is always true. |  [optional] |
|**rea** | [**Rea**](Rea.md) |  |  [optional] |
|**smartInbox** | **String** | DEPRECATED. Use the &lt;&lt;_openapi_receiveddocuments_resource&gt;&gt; endpoint. The email address of the Smart Inbox for this LegalEntity. |  [optional] |
|**tenantId** | **String** | The id of the tenant, to be used in case of multi-tenant solutions. This property will included in webhook events. |  [optional] |
|**thirdPartyPassword** | **String** | The password to use to authenticate to a system through which to send the document, or to obtain tax authority approval to send it. This field is currently relevant only for India and mandatory when creating an IN LegalEntity. |  [optional] |
|**thirdPartyUsername** | **String** | The username to use to authenticate to a system through which to send the document, or to obtain tax authority approval to send it. This field is currently relevant only for India and mandatory when creating an IN LegalEntity. |  [optional] |
|**zip** | **String** | The zipcode. |  [optional] |



## Enum: List&lt;AdvertisementsEnum&gt;

| Name | Value |
|---- | -----|
| INVOICE | &quot;invoice&quot; |
| INVOICE_RESPONSE | &quot;invoice_response&quot; |
| ORDER | &quot;order&quot; |
| ORDERING | &quot;ordering&quot; |
| ORDER_RESPONSE | &quot;order_response&quot; |



