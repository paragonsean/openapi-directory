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
* Enum class AcquirerName.
* @enum {}
* @readonly
*/
export default class AcquirerName {
    
        /**
         * value: "Adyen"
         * @const
         */
        "Adyen" = "Adyen";

    
        /**
         * value: "Alipay"
         * @const
         */
        "Alipay" = "Alipay";

    
        /**
         * value: "AIB"
         * @const
         */
        "AIB" = "AIB";

    
        /**
         * value: "Airpay"
         * @const
         */
        "Airpay" = "Airpay";

    
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
         * value: "AstroPay Card"
         * @const
         */
        "AstroPay Card" = "AstroPay Card";

    
        /**
         * value: "Ipay Options"
         * @const
         */
        "Ipay Options" = "Ipay Options";

    
        /**
         * value: "B+S"
         * @const
         */
        "B+S" = "B+S";

    
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
         * value: "Bank of America"
         * @const
         */
        "Bank of America" = "Bank of America";

    
        /**
         * value: "Bank of Moscow"
         * @const
         */
        "Bank of Moscow" = "Bank of Moscow";

    
        /**
         * value: "Bank of Rebilly"
         * @const
         */
        "Bank of Rebilly" = "Bank of Rebilly";

    
        /**
         * value: "Bank One"
         * @const
         */
        "Bank One" = "Bank One";

    
        /**
         * value: "BMO Harris Bank"
         * @const
         */
        "BMO Harris Bank" = "BMO Harris Bank";

    
        /**
         * value: "Borgun"
         * @const
         */
        "Borgun" = "Borgun";

    
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
         * value: "Catalunya Caixa"
         * @const
         */
        "Catalunya Caixa" = "Catalunya Caixa";

    
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
         * value: "ChinaUnionPay"
         * @const
         */
        "ChinaUnionPay" = "ChinaUnionPay";

    
        /**
         * value: "CIM"
         * @const
         */
        "CIM" = "CIM";

    
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
         * value: "dLocal"
         * @const
         */
        "dLocal" = "dLocal";

    
        /**
         * value: "Dragonphoenix"
         * @const
         */
        "Dragonphoenix" = "Dragonphoenix";

    
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
         * value: "Euteller"
         * @const
         */
        "Euteller" = "Euteller";

    
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
         * value: "Fifth Third Bank"
         * @const
         */
        "Fifth Third Bank" = "Fifth Third Bank";

    
        /**
         * value: "Finrax"
         * @const
         */
        "Finrax" = "Finrax";

    
        /**
         * value: "First Data Buypass"
         * @const
         */
        "First Data Buypass" = "First Data Buypass";

    
        /**
         * value: "First Data Nashville"
         * @const
         */
        "First Data Nashville" = "First Data Nashville";

    
        /**
         * value: "First Data North"
         * @const
         */
        "First Data North" = "First Data North";

    
        /**
         * value: "First Data Omaha"
         * @const
         */
        "First Data Omaha" = "First Data Omaha";

    
        /**
         * value: "FinTecSystems"
         * @const
         */
        "FinTecSystems" = "FinTecSystems";

    
        /**
         * value: "Flexepin"
         * @const
         */
        "Flexepin" = "Flexepin";

    
        /**
         * value: "Forte"
         * @const
         */
        "Forte" = "Forte";

    
        /**
         * value: "FundSend"
         * @const
         */
        "FundSend" = "FundSend";

    
        /**
         * value: "Gigadat"
         * @const
         */
        "Gigadat" = "Gigadat";

    
        /**
         * value: "Global East"
         * @const
         */
        "Global East" = "Global East";

    
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
         * value: "Heartland"
         * @const
         */
        "Heartland" = "Heartland";

    
        /**
         * value: "HiPay"
         * @const
         */
        "HiPay" = "HiPay";

    
        /**
         * value: "HSBC"
         * @const
         */
        "HSBC" = "HSBC";

    
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
         * value: "Intuit"
         * @const
         */
        "Intuit" = "Intuit";

    
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
         * value: "Masapay"
         * @const
         */
        "Masapay" = "Masapay";

    
        /**
         * value: "Merrick"
         * @const
         */
        "Merrick" = "Merrick";

    
        /**
         * value: "Mission Valley Bank"
         * @const
         */
        "Mission Valley Bank" = "Mission Valley Bank";

    
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
         * value: "NATWEST"
         * @const
         */
        "NATWEST" = "NATWEST";

    
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
         * value: "Other"
         * @const
         */
        "Other" = "Other";

    
        /**
         * value: "Panamerican"
         * @const
         */
        "Panamerican" = "Panamerican";

    
        /**
         * value: "Panda Bank"
         * @const
         */
        "Panda Bank" = "Panda Bank";

    
        /**
         * value: "Paramount"
         * @const
         */
        "Paramount" = "Paramount";

    
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
         * value: "Pay4fun"
         * @const
         */
        "Pay4fun" = "Pay4fun";

    
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
         * value: "Paynetics"
         * @const
         */
        "Paynetics" = "Paynetics";

    
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
         * value: "Peoples Trust Company"
         * @const
         */
        "Peoples Trust Company" = "Peoples Trust Company";

    
        /**
         * value: "PostFinance"
         * @const
         */
        "PostFinance" = "PostFinance";

    
        /**
         * value: "Privatbank"
         * @const
         */
        "Privatbank" = "Privatbank";

    
        /**
         * value: "Prosa"
         * @const
         */
        "Prosa" = "Prosa";

    
        /**
         * value: "QQPay"
         * @const
         */
        "QQPay" = "QQPay";

    
        /**
         * value: "Rapyd"
         * @const
         */
        "Rapyd" = "Rapyd";

    
        /**
         * value: "RBC"
         * @const
         */
        "RBC" = "RBC";

    
        /**
         * value: "RBS WorldPay"
         * @const
         */
        "RBS WorldPay" = "RBS WorldPay";

    
        /**
         * value: "RealTime"
         * @const
         */
        "RealTime" = "RealTime";

    
        /**
         * value: "Rotessa"
         * @const
         */
        "Rotessa" = "Rotessa";

    
        /**
         * value: "SaltarPay"
         * @const
         */
        "SaltarPay" = "SaltarPay";

    
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
         * value: "State Bank of Mauritius"
         * @const
         */
        "State Bank of Mauritius" = "State Bank of Mauritius";

    
        /**
         * value: "Stripe"
         * @const
         */
        "Stripe" = "Stripe";

    
        /**
         * value: "TBI"
         * @const
         */
        "TBI" = "TBI";

    
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
         * value: "Trustly"
         * @const
         */
        "Trustly" = "Trustly";

    
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
         * value: "TSYS"
         * @const
         */
        "TSYS" = "TSYS";

    
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
         * value: "Vantiv"
         * @const
         */
        "Vantiv" = "Vantiv";

    
        /**
         * value: "VCreditos"
         * @const
         */
        "VCreditos" = "VCreditos";

    
        /**
         * value: "VoicePay"
         * @const
         */
        "VoicePay" = "VoicePay";

    
        /**
         * value: "Wallet88"
         * @const
         */
        "Wallet88" = "Wallet88";

    
        /**
         * value: "WeChat Pay"
         * @const
         */
        "WeChat Pay" = "WeChat Pay";

    
        /**
         * value: "Wells Fargo"
         * @const
         */
        "Wells Fargo" = "Wells Fargo";

    
        /**
         * value: "Wing Hang Bank"
         * @const
         */
        "Wing Hang Bank" = "Wing Hang Bank";

    
        /**
         * value: "Wirecard"
         * @const
         */
        "Wirecard" = "Wirecard";

    
        /**
         * value: "WorldPay"
         * @const
         */
        "WorldPay" = "WorldPay";

    
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
    * Returns a <code>AcquirerName</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/AcquirerName} The enum <code>AcquirerName</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

