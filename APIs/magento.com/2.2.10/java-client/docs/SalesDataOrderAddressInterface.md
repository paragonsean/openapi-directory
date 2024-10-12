

# SalesDataOrderAddressInterface

Order address interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressType** | **String** | Address type. |  |
|**city** | **String** | City. |  |
|**company** | **String** | Company. |  [optional] |
|**countryId** | **String** | Country ID. |  |
|**customerAddressId** | **Integer** | Country address ID. |  [optional] |
|**customerId** | **Integer** | Customer ID. |  [optional] |
|**email** | **String** | Email address. |  [optional] |
|**entityId** | **Integer** | Order address ID. |  [optional] |
|**extensionAttributes** | [**SalesDataOrderAddressExtensionInterface**](SalesDataOrderAddressExtensionInterface.md) |  |  [optional] |
|**fax** | **String** | Fax number. |  [optional] |
|**firstname** | **String** | First name. |  |
|**lastname** | **String** | Last name. |  |
|**middlename** | **String** | Middle name. |  [optional] |
|**parentId** | **Integer** | Parent ID. |  [optional] |
|**postcode** | **String** | Postal code. |  |
|**prefix** | **String** | Prefix. |  [optional] |
|**region** | **String** | Region. |  [optional] |
|**regionCode** | **String** | Region code. |  [optional] |
|**regionId** | **Integer** | Region ID. |  [optional] |
|**street** | **List&lt;String&gt;** | Array of any street values. Otherwise, null. |  [optional] |
|**suffix** | **String** | Suffix. |  [optional] |
|**telephone** | **String** | Telephone number. |  |
|**vatId** | **String** | VAT ID. |  [optional] |
|**vatIsValid** | **Integer** | VAT-is-valid flag value. |  [optional] |
|**vatRequestDate** | **String** | VAT request date. |  [optional] |
|**vatRequestId** | **String** | VAT request ID. |  [optional] |
|**vatRequestSuccess** | **Integer** | VAT-request-success flag value. |  [optional] |



