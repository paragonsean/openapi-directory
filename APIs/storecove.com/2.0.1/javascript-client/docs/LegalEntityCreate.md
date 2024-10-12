# StorecoveApi.LegalEntityCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertisements** | **[String]** | A list of document types to advertise. Use if this LegalEntity needs the ability to receive more than only invoice documents. | [optional] 
**city** | **String** | The city. | 
**country** | [**Country**](Country.md) |  | 
**county** | **String** | County, if applicable | [optional] 
**line1** | **String** | The first address line. | 
**line2** | **String** | The second address line, if applicable | [optional] 
**partyName** | **String** | The name of the company. | 
**_public** | **Boolean** | Whether or not this LegalEntity is public. Public means it will be entered into the PEPPOL directory at https://directory.peppol.eu/ | [optional] [default to true]
**rea** | [**Rea**](Rea.md) |  | [optional] 
**tenantId** | **String** | The id of the tenant, to be used in case of single-tenant solutions that share webhook URLs. This property will included in webhook events. | [optional] 
**thirdPartyPassword** | **String** | The password to use to authenticate to a system through which to send the document, or to obtain tax authority approval to send it. This field is currently relevant only for India and mandatory when creating an IN LegalEntity. | [optional] 
**thirdPartyUsername** | **String** | The username to use to authenticate to a system through which to send the document, or to obtain tax authority approval to send it. This field is currently relevant only for India and mandatory when creating an IN LegalEntity. | [optional] 
**zip** | **String** | The zipcode. | 



## Enum: [AdvertisementsEnum]


* `invoice` (value: `"invoice"`)

* `invoice_response` (value: `"invoice_response"`)

* `order` (value: `"order"`)

* `ordering` (value: `"ordering"`)

* `order_response` (value: `"order_response"`)




