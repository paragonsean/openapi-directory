# SquareConnectApi.LoyaltyAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **Number** | The available point balance in the loyalty account. If points are scheduled to expire, they are listed in the &#x60;expiring_point_deadlines&#x60; field.  Your application should be able to handle loyalty accounts that have a negative point balance (&#x60;balance&#x60; is less than 0). This might occur if a seller makes a manual adjustment or as a result of a refund or exchange. | [optional] 
**createdAt** | **String** | The timestamp when the loyalty account was created, in RFC 3339 format. | [optional] 
**customerId** | **String** | The Square-assigned ID of the [customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) that is associated with the account. | [optional] 
**enrolledAt** | **String** | The timestamp when enrollment occurred, in RFC 3339 format. | [optional] 
**expiringPointDeadlines** | [**[LoyaltyAccountExpiringPointDeadline]**](LoyaltyAccountExpiringPointDeadline.md) | The schedule for when points expire in the loyalty account balance. This field is present only if the account has points that are scheduled to expire.   The total number of points in this field equals the number of points in the &#x60;balance&#x60; field. | [optional] 
**id** | **String** | The Square-assigned ID of the loyalty account. | [optional] 
**lifetimePoints** | **Number** | The total points accrued during the lifetime of the account. | [optional] 
**mapping** | [**LoyaltyAccountMapping**](LoyaltyAccountMapping.md) |  | [optional] 
**programId** | **String** | The Square-assigned ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram) to which the account belongs. | 
**updatedAt** | **String** | The timestamp when the loyalty account was last updated, in RFC 3339 format. | [optional] 


