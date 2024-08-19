# SquareConnectApi.CreateCustomerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**birthday** | **String** | The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed. For example, &#x60;0000-09-21T00:00:00-00:00&#x60; represents a birthday on September 21 and &#x60;1998-09-21T00:00:00-00:00&#x60; represents a birthday on September 21, 1998. You can also specify this value in &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**companyName** | **String** | A business name associated with the customer profile. | [optional] 
**emailAddress** | **String** | The email address associated with the customer profile. | [optional] 
**familyName** | **String** | The family name (that is, the last name) associated with the customer profile. | [optional] 
**givenName** | **String** | The given name (that is, the first name) associated with the customer profile. | [optional] 
**idempotencyKey** | **String** | The idempotency key for the request. For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency). | [optional] 
**nickname** | **String** | A nickname for the customer profile. | [optional] 
**note** | **String** | A custom note associated with the customer profile. | [optional] 
**phoneNumber** | **String** | The 11-digit phone number associated with the customer profile. | [optional] 
**referenceId** | **String** | An optional second ID used to associate the customer profile with an entity in another system. | [optional] 


