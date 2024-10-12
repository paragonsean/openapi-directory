

# RevokeTokenRequest



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | The access token of the merchant whose token you want to revoke. Do not provide a value for merchant_id if you provide this parameter. |  [optional] |
|**clientId** | **String** | The Square issued ID for your application, available from the [developer dashboard](https://developer.squareup.com/apps). |  [optional] |
|**merchantId** | **String** | The ID of the merchant whose token you want to revoke. Do not provide a value for access_token if you provide this parameter. |  [optional] |
|**revokeOnlyAccessToken** | **Boolean** | If &#x60;true&#x60;, terminate the given single access token, but do not terminate the entire authorization. Default: &#x60;false&#x60; |  [optional] |



