# MarketplaceApi.AcceptSellerLeadRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Marketplace&#39;s account ID | [default to &#39;5fb38ace-d95e-45ad-970d-ee97cce9fbcd&#39;]
**accountable** | [**Accountable**](Accountable.md) |  | 
**address** | [**Address**](Address.md) |  | 
**document** | **String** | Company&#39;s legal document code. | [default to &#39;12345671000&#39;]
**email** | **String** | email of the admin responsible for the seller. | [default to &#39;seller@email.com&#39;]
**hasAcceptedLegalTerms** | **Boolean** | Indicates if the seller has accepted the platform&#39;s legal terms and conditions. | [default to true]
**salesChannel** | **String** | Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) associated to the seller account created. | [default to &#39;1&#39;]
**sellerAccountName** | **String** | Name of the seller&#39;s account, part of the url of their VTEX Admin. | [default to &#39;seller123&#39;]
**sellerEmail** | **String** | Seller&#39;s contact email. | [default to &#39;selleremail@email.com&#39;]
**sellerName** | **String** | Seller&#39;s store&#39;s name. | [default to &#39;Seller Name&#39;]
**sellerType** | **Number** | Type of seller, including:   &#x60;1&#x60;: regular seller   &#x60;2&#x60;: whitelabel seller | [default to 1]


