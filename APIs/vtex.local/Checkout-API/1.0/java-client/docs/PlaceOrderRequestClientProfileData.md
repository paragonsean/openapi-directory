

# PlaceOrderRequestClientProfileData

Customer's profile information. The `email` functions as a customer's ID.    For customers already in your database, sending only the email address is enough to register the order to the shopper’s existing account.    > If the shopper exists in you database but is not logged in, sending other profile information along with the email will cause the platform to fail placing the order. This happens because this action is interpreted as an attempt to edit profile data, which is not possible unless the customer is logged in to the store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**corporateDocument** | **String** | Corporate document, if the customer is a legal entity. |  [optional] |
|**corporateName** | **String** | Company name, if the customer is a legal entity. |  [optional] |
|**corporatePhone** | **String** | Corporate phone number, if the customer is a legal entity. |  [optional] |
|**document** | **String** | Document number informed by the customer. |  [optional] |
|**documentType** | **String** | Type of the document informed by the customer. |  [optional] |
|**email** | **String** | Customer&#39;s email address. |  |
|**firstName** | **String** | Customer&#39;s first name. |  [optional] |
|**isCorporate** | **Boolean** | &#x60;true&#x60; if the customer is a legal entity. |  [optional] |
|**lastName** | **String** | Customer&#39;s last name. |  [optional] |
|**phone** | **String** | Customer&#39;s phone number. |  [optional] |
|**stateInscription** | **String** | State inscription, if the customer is a legal entity. |  [optional] |
|**tradeName** | **String** | Trade name, if the customer is a legal entity. |  [optional] |



