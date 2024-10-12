/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class GatewayName.
* @enum {}
* @readonly
*/
export default class GatewayName {
    
        /**
         * value: "A1Gateway"
         * @const
         */
        "A1Gateway" = "A1Gateway";

    
        /**
         * value: "Adyen"
         * @const
         */
        "Adyen" = "Adyen";

    
        /**
         * value: "Airpay"
         * @const
         */
        "Airpay" = "Airpay";

    
        /**
         * value: "AmexVPC"
         * @const
         */
        "AmexVPC" = "AmexVPC";

    
        /**
         * value: "ApcoPay"
         * @const
         */
        "ApcoPay" = "ApcoPay";

    
        /**
         * value: "AsiaPaymentGateway"
         * @const
         */
        "AsiaPaymentGateway" = "AsiaPaymentGateway";

    
        /**
         * value: "AstroPayCard"
         * @const
         */
        "AstroPayCard" = "AstroPayCard";

    
        /**
         * value: "AuthorizeNet"
         * @const
         */
        "AuthorizeNet" = "AuthorizeNet";

    
        /**
         * value: "Bambora"
         * @const
         */
        "Bambora" = "Bambora";

    
        /**
         * value: "BitPay"
         * @const
         */
        "BitPay" = "BitPay";

    
        /**
         * value: "BlueSnap"
         * @const
         */
        "BlueSnap" = "BlueSnap";

    
        /**
         * value: "BraintreePayments"
         * @const
         */
        "BraintreePayments" = "BraintreePayments";

    
        /**
         * value: "Cardknox"
         * @const
         */
        "Cardknox" = "Cardknox";

    
        /**
         * value: "Cashflows"
         * @const
         */
        "Cashflows" = "Cashflows";

    
        /**
         * value: "CASHlib"
         * @const
         */
        "CASHlib" = "CASHlib";

    
        /**
         * value: "CashToCode"
         * @const
         */
        "CashToCode" = "CashToCode";

    
        /**
         * value: "CauriPayment"
         * @const
         */
        "CauriPayment" = "CauriPayment";

    
        /**
         * value: "Cayan"
         * @const
         */
        "Cayan" = "Cayan";

    
        /**
         * value: "CCAvenue"
         * @const
         */
        "CCAvenue" = "CCAvenue";

    
        /**
         * value: "Chase"
         * @const
         */
        "Chase" = "Chase";

    
        /**
         * value: "Circle"
         * @const
         */
        "Circle" = "Circle";

    
        /**
         * value: "Citadel"
         * @const
         */
        "Citadel" = "Citadel";

    
        /**
         * value: "Clearhaus"
         * @const
         */
        "Clearhaus" = "Clearhaus";

    
        /**
         * value: "CODVoucher"
         * @const
         */
        "CODVoucher" = "CODVoucher";

    
        /**
         * value: "CoinPayments"
         * @const
         */
        "CoinPayments" = "CoinPayments";

    
        /**
         * value: "Conekta"
         * @const
         */
        "Conekta" = "Conekta";

    
        /**
         * value: "Coppr"
         * @const
         */
        "Coppr" = "Coppr";

    
        /**
         * value: "Credorax"
         * @const
         */
        "Credorax" = "Credorax";

    
        /**
         * value: "Cryptonator"
         * @const
         */
        "Cryptonator" = "Cryptonator";

    
        /**
         * value: "CyberSource"
         * @const
         */
        "CyberSource" = "CyberSource";

    
        /**
         * value: "DataCash"
         * @const
         */
        "DataCash" = "DataCash";

    
        /**
         * value: "Dengi"
         * @const
         */
        "Dengi" = "Dengi";

    
        /**
         * value: "Dragonphoenix"
         * @const
         */
        "Dragonphoenix" = "Dragonphoenix";

    
        /**
         * value: "Directa24"
         * @const
         */
        "Directa24" = "Directa24";

    
        /**
         * value: "dLocal"
         * @const
         */
        "dLocal" = "dLocal";

    
        /**
         * value: "EBANX"
         * @const
         */
        "EBANX" = "EBANX";

    
        /**
         * value: "ecoPayz"
         * @const
         */
        "ecoPayz" = "ecoPayz";

    
        /**
         * value: "EcorePay"
         * @const
         */
        "EcorePay" = "EcorePay";

    
        /**
         * value: "Elavon"
         * @const
         */
        "Elavon" = "Elavon";

    
        /**
         * value: "Euteller"
         * @const
         */
        "Euteller" = "Euteller";

    
        /**
         * value: "eMerchantPay"
         * @const
         */
        "eMerchantPay" = "eMerchantPay";

    
        /**
         * value: "EMS"
         * @const
         */
        "EMS" = "EMS";

    
        /**
         * value: "EPG"
         * @const
         */
        "EPG" = "EPG";

    
        /**
         * value: "EPro"
         * @const
         */
        "EPro" = "EPro";

    
        /**
         * value: "eZeeWallet"
         * @const
         */
        "eZeeWallet" = "eZeeWallet";

    
        /**
         * value: "ezyEFT"
         * @const
         */
        "ezyEFT" = "ezyEFT";

    
        /**
         * value: "Finrax"
         * @const
         */
        "Finrax" = "Finrax";

    
        /**
         * value: "Flexepin"
         * @const
         */
        "Flexepin" = "Flexepin";

    
        /**
         * value: "FinTecSystems"
         * @const
         */
        "FinTecSystems" = "FinTecSystems";

    
        /**
         * value: "FundSend"
         * @const
         */
        "FundSend" = "FundSend";

    
        /**
         * value: "Forte"
         * @const
         */
        "Forte" = "Forte";

    
        /**
         * value: "GET"
         * @const
         */
        "GET" = "GET";

    
        /**
         * value: "Gigadat"
         * @const
         */
        "Gigadat" = "Gigadat";

    
        /**
         * value: "GlobalOnePay"
         * @const
         */
        "GlobalOnePay" = "GlobalOnePay";

    
        /**
         * value: "Gooney"
         * @const
         */
        "Gooney" = "Gooney";

    
        /**
         * value: "Gpaysafe"
         * @const
         */
        "Gpaysafe" = "Gpaysafe";

    
        /**
         * value: "Greenbox"
         * @const
         */
        "Greenbox" = "Greenbox";

    
        /**
         * value: "HiPay"
         * @const
         */
        "HiPay" = "HiPay";

    
        /**
         * value: "iCanPay"
         * @const
         */
        "iCanPay" = "iCanPay";

    
        /**
         * value: "ICEPAY"
         * @const
         */
        "ICEPAY" = "ICEPAY";

    
        /**
         * value: "iCheque"
         * @const
         */
        "iCheque" = "iCheque";

    
        /**
         * value: "iDebit"
         * @const
         */
        "iDebit" = "iDebit";

    
        /**
         * value: "Ilixium"
         * @const
         */
        "Ilixium" = "Ilixium";

    
        /**
         * value: "Ingenico"
         * @const
         */
        "Ingenico" = "Ingenico";

    
        /**
         * value: "INOVAPAY"
         * @const
         */
        "INOVAPAY" = "INOVAPAY";

    
        /**
         * value: "Inovio"
         * @const
         */
        "Inovio" = "Inovio";

    
        /**
         * value: "Intuit"
         * @const
         */
        "Intuit" = "Intuit";

    
        /**
         * value: "InstaDebit"
         * @const
         */
        "InstaDebit" = "InstaDebit";

    
        /**
         * value: "IpayOptions"
         * @const
         */
        "IpayOptions" = "IpayOptions";

    
        /**
         * value: "JetPay"
         * @const
         */
        "JetPay" = "JetPay";

    
        /**
         * value: "Jeton"
         * @const
         */
        "Jeton" = "Jeton";

    
        /**
         * value: "Khelocard"
         * @const
         */
        "Khelocard" = "Khelocard";

    
        /**
         * value: "Konnektive"
         * @const
         */
        "Konnektive" = "Konnektive";

    
        /**
         * value: "loonie"
         * @const
         */
        "loonie" = "loonie";

    
        /**
         * value: "LPG"
         * @const
         */
        "LPG" = "LPG";

    
        /**
         * value: "MiFinity"
         * @const
         */
        "MiFinity" = "MiFinity";

    
        /**
         * value: "Moneris"
         * @const
         */
        "Moneris" = "Moneris";

    
        /**
         * value: "MtaPay"
         * @const
         */
        "MtaPay" = "MtaPay";

    
        /**
         * value: "MuchBetter"
         * @const
         */
        "MuchBetter" = "MuchBetter";

    
        /**
         * value: "MyFatoorah"
         * @const
         */
        "MyFatoorah" = "MyFatoorah";

    
        /**
         * value: "Neosurf"
         * @const
         */
        "Neosurf" = "Neosurf";

    
        /**
         * value: "Netbanking"
         * @const
         */
        "Netbanking" = "Netbanking";

    
        /**
         * value: "Neteller"
         * @const
         */
        "Neteller" = "Neteller";

    
        /**
         * value: "NGenius"
         * @const
         */
        "NGenius" = "NGenius";

    
        /**
         * value: "NinjaWallet"
         * @const
         */
        "NinjaWallet" = "NinjaWallet";

    
        /**
         * value: "NMI"
         * @const
         */
        "NMI" = "NMI";

    
        /**
         * value: "NuaPay"
         * @const
         */
        "NuaPay" = "NuaPay";

    
        /**
         * value: "OchaPay"
         * @const
         */
        "OchaPay" = "OchaPay";

    
        /**
         * value: "Onlineueberweisen"
         * @const
         */
        "Onlineueberweisen" = "Onlineueberweisen";

    
        /**
         * value: "OnRamp"
         * @const
         */
        "OnRamp" = "OnRamp";

    
        /**
         * value: "Pagsmile"
         * @const
         */
        "Pagsmile" = "Pagsmile";

    
        /**
         * value: "Panamerican"
         * @const
         */
        "Panamerican" = "Panamerican";

    
        /**
         * value: "ParamountEft"
         * @const
         */
        "ParamountEft" = "ParamountEft";

    
        /**
         * value: "ParamountInterac"
         * @const
         */
        "ParamountInterac" = "ParamountInterac";

    
        /**
         * value: "PandaGateway"
         * @const
         */
        "PandaGateway" = "PandaGateway";

    
        /**
         * value: "Pay4Fun"
         * @const
         */
        "Pay4Fun" = "Pay4Fun";

    
        /**
         * value: "PayCash"
         * @const
         */
        "PayCash" = "PayCash";

    
        /**
         * value: "PayClub"
         * @const
         */
        "PayClub" = "PayClub";

    
        /**
         * value: "Payeezy"
         * @const
         */
        "Payeezy" = "Payeezy";

    
        /**
         * value: "Payflow"
         * @const
         */
        "Payflow" = "Payflow";

    
        /**
         * value: "PaymentAsia"
         * @const
         */
        "PaymentAsia" = "PaymentAsia";

    
        /**
         * value: "PaymenTechnologies"
         * @const
         */
        "PaymenTechnologies" = "PaymenTechnologies";

    
        /**
         * value: "PaymentsOS"
         * @const
         */
        "PaymentsOS" = "PaymentsOS";

    
        /**
         * value: "Paymero"
         * @const
         */
        "Paymero" = "Paymero";

    
        /**
         * value: "PayPal"
         * @const
         */
        "PayPal" = "PayPal";

    
        /**
         * value: "Payr"
         * @const
         */
        "Payr" = "Payr";

    
        /**
         * value: "Paysafe"
         * @const
         */
        "Paysafe" = "Paysafe";

    
        /**
         * value: "Paysafecash"
         * @const
         */
        "Paysafecash" = "Paysafecash";

    
        /**
         * value: "PayTabs"
         * @const
         */
        "PayTabs" = "PayTabs";

    
        /**
         * value: "PayULatam"
         * @const
         */
        "PayULatam" = "PayULatam";

    
        /**
         * value: "Payvision"
         * @const
         */
        "Payvision" = "Payvision";

    
        /**
         * value: "Piastrix"
         * @const
         */
        "Piastrix" = "Piastrix";

    
        /**
         * value: "Plugnpay"
         * @const
         */
        "Plugnpay" = "Plugnpay";

    
        /**
         * value: "PostFinance"
         * @const
         */
        "PostFinance" = "PostFinance";

    
        /**
         * value: "Prosa"
         * @const
         */
        "Prosa" = "Prosa";

    
        /**
         * value: "Rapyd"
         * @const
         */
        "Rapyd" = "Rapyd";

    
        /**
         * value: "Realex"
         * @const
         */
        "Realex" = "Realex";

    
        /**
         * value: "Realtime"
         * @const
         */
        "Realtime" = "Realtime";

    
        /**
         * value: "Redsys"
         * @const
         */
        "Redsys" = "Redsys";

    
        /**
         * value: "Rotessa"
         * @const
         */
        "Rotessa" = "Rotessa";

    
        /**
         * value: "RPN"
         * @const
         */
        "RPN" = "RPN";

    
        /**
         * value: "SaltarPay"
         * @const
         */
        "SaltarPay" = "SaltarPay";

    
        /**
         * value: "Sagepay"
         * @const
         */
        "Sagepay" = "Sagepay";

    
        /**
         * value: "SeamlessChex"
         * @const
         */
        "SeamlessChex" = "SeamlessChex";

    
        /**
         * value: "SecureTrading"
         * @const
         */
        "SecureTrading" = "SecureTrading";

    
        /**
         * value: "SecurionPay"
         * @const
         */
        "SecurionPay" = "SecurionPay";

    
        /**
         * value: "Skrill"
         * @const
         */
        "Skrill" = "Skrill";

    
        /**
         * value: "SmartInvoice"
         * @const
         */
        "SmartInvoice" = "SmartInvoice";

    
        /**
         * value: "SMSVoucher"
         * @const
         */
        "SMSVoucher" = "SMSVoucher";

    
        /**
         * value: "Sofort"
         * @const
         */
        "Sofort" = "Sofort";

    
        /**
         * value: "SparkPay"
         * @const
         */
        "SparkPay" = "SparkPay";

    
        /**
         * value: "StaticGateway"
         * @const
         */
        "StaticGateway" = "StaticGateway";

    
        /**
         * value: "Stripe"
         * @const
         */
        "Stripe" = "Stripe";

    
        /**
         * value: "TestProcessor"
         * @const
         */
        "TestProcessor" = "TestProcessor";

    
        /**
         * value: "ToditoCash"
         * @const
         */
        "ToditoCash" = "ToditoCash";

    
        /**
         * value: "TrustPay"
         * @const
         */
        "TrustPay" = "TrustPay";

    
        /**
         * value: "TrustsPay"
         * @const
         */
        "TrustsPay" = "TrustsPay";

    
        /**
         * value: "Trustly"
         * @const
         */
        "Trustly" = "Trustly";

    
        /**
         * value: "TWINT"
         * @const
         */
        "TWINT" = "TWINT";

    
        /**
         * value: "UPayCard"
         * @const
         */
        "UPayCard" = "UPayCard";

    
        /**
         * value: "USAePay"
         * @const
         */
        "USAePay" = "USAePay";

    
        /**
         * value: "VantivLitle"
         * @const
         */
        "VantivLitle" = "VantivLitle";

    
        /**
         * value: "vegaaH"
         * @const
         */
        "vegaaH" = "vegaaH";

    
        /**
         * value: "VCreditos"
         * @const
         */
        "VCreditos" = "VCreditos";

    
        /**
         * value: "Wallet88"
         * @const
         */
        "Wallet88" = "Wallet88";

    
        /**
         * value: "Walpay"
         * @const
         */
        "Walpay" = "Walpay";

    
        /**
         * value: "Wirecard"
         * @const
         */
        "Wirecard" = "Wirecard";

    
        /**
         * value: "WorldlineAtosFrankfurt"
         * @const
         */
        "WorldlineAtosFrankfurt" = "WorldlineAtosFrankfurt";

    
        /**
         * value: "Worldpay"
         * @const
         */
        "Worldpay" = "Worldpay";

    
        /**
         * value: "XPay"
         * @const
         */
        "XPay" = "XPay";

    
        /**
         * value: "Zimpler"
         * @const
         */
        "Zimpler" = "Zimpler";

    
        /**
         * value: "Zotapay"
         * @const
         */
        "Zotapay" = "Zotapay";

    

    /**
    * Returns a <code>GatewayName</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/GatewayName} The enum <code>GatewayName</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

