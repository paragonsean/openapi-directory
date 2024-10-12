# GooglePlayAndroidDeveloperApi.IntroductoryPriceInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**introductoryPriceAmountMicros** | **String** | Introductory price of the subscription, not including tax. The currency is the same as price_currency_code. Price is expressed in micro-units, where 1,000,000 micro-units represents one unit of the currency. For example, if the subscription price is €1.99, price_amount_micros is 1990000. | [optional] 
**introductoryPriceCurrencyCode** | **String** | ISO 4217 currency code for the introductory subscription price. For example, if the price is specified in British pounds sterling, price_currency_code is \&quot;GBP\&quot;. | [optional] 
**introductoryPriceCycles** | **Number** | The number of billing period to offer introductory pricing. | [optional] 
**introductoryPricePeriod** | **String** | Introductory price period, specified in ISO 8601 format. Common values are (but not limited to) \&quot;P1W\&quot; (one week), \&quot;P1M\&quot; (one month), \&quot;P3M\&quot; (three months), \&quot;P6M\&quot; (six months), and \&quot;P1Y\&quot; (one year). | [optional] 


