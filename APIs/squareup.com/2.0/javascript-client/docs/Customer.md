# SquareConnectApi.Customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**birthday** | **String** | The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed. For example, &#x60;0000-09-21T00:00:00-00:00&#x60; represents a birthday on September 21 and &#x60;1998-09-21T00:00:00-00:00&#x60; represents a birthday on September 21, 1998. | [optional] 
**cards** | [**[Card]**](Card.md) | Payment details of the credit, debit, and gift cards stored on file for the customer profile.   DEPRECATED at version 2021-06-16. Replaced by calling [ListCards](https://developer.squareup.com/reference/square_2021-08-18/cards-api/list-cards) (for credit and debit cards on file)  or [ListGiftCards](https://developer.squareup.com/reference/square_2021-08-18/gift-cards-api/list-gift-cards) (for gift cards on file) and including the &#x60;customer_id&#x60; query parameter.  For more information, see [Migrate to the Cards API and Gift Cards API](https://developer.squareup.com/docs/customers-api/use-the-api/integrate-with-other-services#migrate-customer-cards). | [optional] 
**companyName** | **String** | A business name associated with the customer profile. | [optional] 
**createdAt** | **String** | The timestamp when the customer profile was created, in RFC 3339 format. | [optional] 
**creationSource** | **String** | A creation source represents the method used to create the customer profile. | [optional] 
**emailAddress** | **String** | The email address associated with the customer profile. | [optional] 
**familyName** | **String** | The family (i.e., last) name associated with the customer profile. | [optional] 
**givenName** | **String** | The given (i.e., first) name associated with the customer profile. | [optional] 
**groupIds** | **[String]** | The IDs of customer groups the customer belongs to. | [optional] 
**id** | **String** | A unique Square-assigned ID for the customer profile. | [optional] 
**nickname** | **String** | A nickname for the customer profile. | [optional] 
**note** | **String** | A custom note associated with the customer profile. | [optional] 
**phoneNumber** | **String** | The 11-digit phone number associated with the customer profile. | [optional] 
**preferences** | [**CustomerPreferences**](CustomerPreferences.md) |  | [optional] 
**referenceId** | **String** | An optional second ID used to associate the customer profile with an entity in another system. | [optional] 
**segmentIds** | **[String]** | The IDs of segments the customer belongs to. | [optional] 
**updatedAt** | **String** | The timestamp when the customer profile was last updated, in RFC 3339 format. | [optional] 
**version** | **Number** | The Square-assigned version number of the customer profile. The version number is incremented each time an update is committed to the customer profile, except for changes to customer segment membership and cards on file. | [optional] 


