

# GoogleCloudChannelV1CloudIdentityCustomerAccount

Entity representing a Cloud Identity account that may be associated with a Channel Services API partner.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerCloudIdentityId** | **String** | If existing &#x3D; true, the Cloud Identity ID of the customer. |  [optional] |
|**customerName** | **String** | If owned &#x3D; true, the name of the customer that owns the Cloud Identity account. Customer_name uses the format: accounts/{account_id}/customers/{customer_id} |  [optional] |
|**existing** | **Boolean** | Returns true if a Cloud Identity account exists for a specific domain. |  [optional] |
|**owned** | **Boolean** | Returns true if the Cloud Identity account is associated with a customer of the Channel Services partner. |  [optional] |



