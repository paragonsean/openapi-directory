

# Company


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**CompanyLinks**](CompanyLinks.md) | References to resources connected with this company. |  [optional] |
|**dataCenters** | [**List&lt;DataCenter&gt;**](DataCenter.md) | List of available data centers.  Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers. |  [optional] |
|**description** | **String** | Your description for the company account, maximum 300 characters |  [optional] |
|**id** | **String** | The unique identifier of the company account. |  [optional] |
|**name** | **String** | The legal or trading name of the company. |  [optional] |
|**reference** | **String** | Your reference to the account |  [optional] |
|**status** | **String** | The status of the company account.  Possible values:  * **Active**: Users can log in. Processing and payout capabilities depend on the status of the merchant account. * **Inactive**: Users can log in. Payment processing and payouts are disabled. * **Closed**: The company account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled. |  [optional] |



