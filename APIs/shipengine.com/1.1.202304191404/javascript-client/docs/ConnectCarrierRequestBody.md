# ShipEngineApi.ConnectCarrierRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nickname** | **String** | Nickname | 
**password** | **String** | Password | 
**username** | **String** | Username | 
**email** | **String** | The email address | 
**merchantSellerId** | **String** |  | 
**mwsAuthToken** | **String** |  | 
**authCode** | **String** | Amazon UK Shipping auth code. | 
**accountNumber** | **String** | Account number | 
**ftpPassword** | **String** | FTP password | 
**ftpUsername** | **String** | FTP username | 
**apiKey** | **String** | API key | 
**apiSecret** | **String** | The DHL E-Commerce API secret. This field is optional, but if not set you will not be able to get rates for this account.  | 
**contractId** | **String** | Canada Post Account Contract ID | 
**ancillaryEndorsement** | [**AncillaryServiceEndorsement**](AncillaryServiceEndorsement.md) |  | [optional] 
**clientId** | **String** | The client id | 
**distributionCenter** | **String** | The distribution center | 
**pickupNumber** | **String** | The pickup number | 
**registrationId** | **String** |  | [optional] 
**softwareName** | **String** |  | [optional] 
**soldTo** | **String** | Sold To field | [optional] 
**countryCode** | **String** | Country code | 
**siteId** | **String** | A string that uniquely identifies the site | 
**account** | **String** | Account | 
**passphrase** | **String** | Passphrase | 
**address1** | **String** | Address Line 1 | 
**address2** | **String** | Address Line 2 | [optional] 
**agreeToEula** | **Boolean** | Boolean signaling agreement to the Fedex End User License Agreement | 
**city** | **String** | City | 
**company** | **String** | Company | 
**firstName** | **String** | First name | 
**lastName** | **String** | Last name | 
**meterNumber** | **String** | Meter number | [optional] 
**phone** | **String** | Phone | 
**postalCode** | **String** | Postal code | 
**state** | **String** | State | 
**mailerId** | **Number** | Mailer id | 
**profileName** | **String** | Profile name | [optional] 
**inductionSite** | **String** | Induction site | 
**merchantId** | **Number** | Merchant id | [optional] 
**activationKey** | **String** | Activation key | 
**companyName** | **String** | Company name | [optional] 
**contactName** | **String** | Contact name | 
**obaEmail** | **String** | The oba email address | [optional] 
**streetLine1** | **String** | Street line1 | [optional] 
**streetLine2** | **String** | Street line2 | [optional] 
**streetLine3** | **String** | Street line3 | [optional] 
**accessKey** | **String** | Seko Account Access Key | 
**sendleId** | **String** | A string that uniquely identifies the sendle | 
**accountCountryCode** | **String** | Account country code | 
**accountPostalCode** | **String** | Account postal code | 
**agreeToTechnologyAgreement** | **Boolean** | The Agreement to the [UPS Technology Agreement](https://www.ups.com/assets/resources/media/UTA_with_EUR.pdf) | 
**invoice** | [**UpsInvoice**](UpsInvoice.md) | The UPS invoice | [optional] 
**invoiceAmount** | **Number** | The invoice amount | [optional] 
**invoiceCurrencyCode** | **String** | The invoice currency code | [optional] 
**title** | **String** | Title | [optional] 


