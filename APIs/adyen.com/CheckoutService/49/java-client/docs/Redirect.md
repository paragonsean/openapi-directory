

# Redirect


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Map&lt;String, String&gt;** | When the redirect URL must be accessed via POST, use this data to post to the redirect URL. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | The web method that you must use to access the redirect URL.  Possible values: GET, POST. |  [optional] |
|**url** | **String** | The URL, to which you must redirect a shopper to complete a payment. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |



