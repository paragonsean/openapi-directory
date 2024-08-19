# ThePlaidApi.Security

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closePrice** | **Number** | Price of the security at the close of the previous trading session. Null for non-public securities.  If the security is a foreign currency this field will be updated daily and will be priced in USD.  If the security is a cryptocurrency, this field will be updated multiple times a day. As crypto prices can fluctuate quickly and data may become stale sooner than other asset classes, refer to &#x60;update_datetime&#x60; with the time when the price was last updated.  | 
**closePriceAsOf** | **Date** | Date for which &#x60;close_price&#x60; is accurate. Always &#x60;null&#x60; if &#x60;close_price&#x60; is &#x60;null&#x60;. | 
**cusip** | **String** | 9-character CUSIP, an identifier assigned to North American securities. Please note that Plaid&#39;s customers must hold a license directly from CUSIP Global Services to receive CUSIP &amp; ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com. | 
**institutionId** | **String** | If &#x60;institution_security_id&#x60; is present, this field indicates the Plaid &#x60;institution_id&#x60; of the institution to whom the identifier belongs. | 
**institutionSecurityId** | **String** | An identifier given to the security by the institution | 
**isCashEquivalent** | **Boolean** | Indicates that a security is a highly liquid asset and can be treated like cash. | 
**isin** | **String** | 12-character ISIN, a globally unique securities identifier. Please note that Plaid&#39;s customers must hold a license directly from CUSIP Global Services to receive CUSIP &amp; ISIN data. This field will be null by default for new customers. For existing customers, this field will be null by default starting on Sept 15, 2023. If you would like access to this field, please contact your Plaid Account Manager or reach out to investments-vendors@plaid.com. | 
**isoCurrencyCode** | **String** | The ISO-4217 currency code of the price given. Always &#x60;null&#x60; if &#x60;unofficial_currency_code&#x60; is non-&#x60;null&#x60;. | 
**name** | **String** | A descriptive name for the security, suitable for display. | 
**proxySecurityId** | **String** | In certain cases, Plaid will provide the ID of another security whose performance resembles this security, typically when the original security has low volume, or when a private security can be modeled with a publicly traded security. | 
**securityId** | **String** | A unique, Plaid-specific identifier for the security, used to associate securities with holdings. Like all Plaid identifiers, the &#x60;security_id&#x60; is case sensitive. The &#x60;security_id&#x60; may change if inherent details of the security change due to a corporate action, for example, in the event of a ticker symbol change or CUSIP change. | 
**sedol** | **String** | 7-character SEDOL, an identifier assigned to securities in the UK. | 
**tickerSymbol** | **String** | The security’s trading symbol for publicly traded securities, and otherwise a short identifier if available. | 
**type** | **String** | The security type of the holding. Valid security types are:  &#x60;cash&#x60;: Cash, currency, and money market funds  &#x60;cryptocurrency&#x60;: Digital or virtual currencies  &#x60;derivative&#x60;: Options, warrants, and other derivative instruments  &#x60;equity&#x60;: Domestic and foreign equities  &#x60;etf&#x60;: Multi-asset exchange-traded investment funds  &#x60;fixed income&#x60;: Bonds and certificates of deposit (CDs)  &#x60;loan&#x60;: Loans and loan receivables  &#x60;mutual fund&#x60;: Open- and closed-end vehicles pooling funds of multiple investors  &#x60;other&#x60;: Unknown or other investment types | 
**unofficialCurrencyCode** | **String** | The unofficial currency code associated with the security. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-&#x60;null&#x60;. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported &#x60;iso_currency_code&#x60;s. | 
**updateDatetime** | **Date** | Date and time at which &#x60;close_price&#x60; is accurate, in ISO 8601 format (YYYY-MM-DDTHH:mm:ssZ). Always &#x60;null&#x60; if &#x60;close_price&#x60; is &#x60;null&#x60;. | [optional] 


