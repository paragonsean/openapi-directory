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
* Enum class AlternativePaymentMethods.
* @enum {}
* @readonly
*/
export default class AlternativePaymentMethods {
    
        /**
         * value: "cash"
         * @const
         */
        "cash" = "cash";

    
        /**
         * value: "check"
         * @const
         */
        "check" = "check";

    
        /**
         * value: "paypal"
         * @const
         */
        "paypal" = "paypal";

    
        /**
         * value: "AdvCash"
         * @const
         */
        "AdvCash" = "AdvCash";

    
        /**
         * value: "Alfa-click"
         * @const
         */
        "Alfa-click" = "Alfa-click";

    
        /**
         * value: "Alipay"
         * @const
         */
        "Alipay" = "Alipay";

    
        /**
         * value: "AstroPay Card"
         * @const
         */
        "AstroPay Card" = "AstroPay Card";

    
        /**
         * value: "AstroPay-GO"
         * @const
         */
        "AstroPay-GO" = "AstroPay-GO";

    
        /**
         * value: "bank-transfer"
         * @const
         */
        "bank-transfer" = "bank-transfer";

    
        /**
         * value: "bank-transfer-2"
         * @const
         */
        "bank-transfer-2" = "bank-transfer-2";

    
        /**
         * value: "bank-transfer-3"
         * @const
         */
        "bank-transfer-3" = "bank-transfer-3";

    
        /**
         * value: "bank-transfer-4"
         * @const
         */
        "bank-transfer-4" = "bank-transfer-4";

    
        /**
         * value: "bank-transfer-5"
         * @const
         */
        "bank-transfer-5" = "bank-transfer-5";

    
        /**
         * value: "bank-transfer-6"
         * @const
         */
        "bank-transfer-6" = "bank-transfer-6";

    
        /**
         * value: "bank-transfer-7"
         * @const
         */
        "bank-transfer-7" = "bank-transfer-7";

    
        /**
         * value: "bank-transfer-8"
         * @const
         */
        "bank-transfer-8" = "bank-transfer-8";

    
        /**
         * value: "bank-transfer-9"
         * @const
         */
        "bank-transfer-9" = "bank-transfer-9";

    
        /**
         * value: "Beeline"
         * @const
         */
        "Beeline" = "Beeline";

    
        /**
         * value: "Belfius-direct-net"
         * @const
         */
        "Belfius-direct-net" = "Belfius-direct-net";

    
        /**
         * value: "bitcoin"
         * @const
         */
        "bitcoin" = "bitcoin";

    
        /**
         * value: "Boleto"
         * @const
         */
        "Boleto" = "Boleto";

    
        /**
         * value: "cash-deposit"
         * @const
         */
        "cash-deposit" = "cash-deposit";

    
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
         * value: "China UnionPay"
         * @const
         */
        "China UnionPay" = "China UnionPay";

    
        /**
         * value: "CODVoucher"
         * @const
         */
        "CODVoucher" = "CODVoucher";

    
        /**
         * value: "Conekta-oxxo"
         * @const
         */
        "Conekta-oxxo" = "Conekta-oxxo";

    
        /**
         * value: "Cupon-de-pagos"
         * @const
         */
        "Cupon-de-pagos" = "Cupon-de-pagos";

    
        /**
         * value: "cryptocurrency"
         * @const
         */
        "cryptocurrency" = "cryptocurrency";

    
        /**
         * value: "domestic-cards"
         * @const
         */
        "domestic-cards" = "domestic-cards";

    
        /**
         * value: "echeck"
         * @const
         */
        "echeck" = "echeck";

    
        /**
         * value: "ecoPayz"
         * @const
         */
        "ecoPayz" = "ecoPayz";

    
        /**
         * value: "ecoVoucher"
         * @const
         */
        "ecoVoucher" = "ecoVoucher";

    
        /**
         * value: "EPS"
         * @const
         */
        "EPS" = "EPS";

    
        /**
         * value: "ePay.bg"
         * @const
         */
        "ePay.bg" = "ePay.bg";

    
        /**
         * value: "eZeeWallet"
         * @const
         */
        "eZeeWallet" = "eZeeWallet";

    
        /**
         * value: "Flexepin"
         * @const
         */
        "Flexepin" = "Flexepin";

    
        /**
         * value: "Giropay"
         * @const
         */
        "Giropay" = "Giropay";

    
        /**
         * value: "Gpaysafe"
         * @const
         */
        "Gpaysafe" = "Gpaysafe";

    
        /**
         * value: "Google Pay"
         * @const
         */
        "Google Pay" = "Google Pay";

    
        /**
         * value: "iDebit"
         * @const
         */
        "iDebit" = "iDebit";

    
        /**
         * value: "iDEAL"
         * @const
         */
        "iDEAL" = "iDEAL";

    
        /**
         * value: "ING-homepay"
         * @const
         */
        "ING-homepay" = "ING-homepay";

    
        /**
         * value: "INOVAPAY-pin"
         * @const
         */
        "INOVAPAY-pin" = "INOVAPAY-pin";

    
        /**
         * value: "INOVAPAY-wallet"
         * @const
         */
        "INOVAPAY-wallet" = "INOVAPAY-wallet";

    
        /**
         * value: "InstaDebit"
         * @const
         */
        "InstaDebit" = "InstaDebit";

    
        /**
         * value: "instant-bank-transfer"
         * @const
         */
        "instant-bank-transfer" = "instant-bank-transfer";

    
        /**
         * value: "Interac"
         * @const
         */
        "Interac" = "Interac";

    
        /**
         * value: "Interac-online"
         * @const
         */
        "Interac-online" = "Interac-online";

    
        /**
         * value: "Interac-eTransfer"
         * @const
         */
        "Interac-eTransfer" = "Interac-eTransfer";

    
        /**
         * value: "invoice"
         * @const
         */
        "invoice" = "invoice";

    
        /**
         * value: "iWallet"
         * @const
         */
        "iWallet" = "iWallet";

    
        /**
         * value: "Jeton"
         * @const
         */
        "Jeton" = "Jeton";

    
        /**
         * value: "jpay"
         * @const
         */
        "jpay" = "jpay";

    
        /**
         * value: "Khelocard"
         * @const
         */
        "Khelocard" = "Khelocard";

    
        /**
         * value: "Klarna"
         * @const
         */
        "Klarna" = "Klarna";

    
        /**
         * value: "loonie"
         * @const
         */
        "loonie" = "loonie";

    
        /**
         * value: "Megafon"
         * @const
         */
        "Megafon" = "Megafon";

    
        /**
         * value: "MiFinity-eWallet"
         * @const
         */
        "MiFinity-eWallet" = "MiFinity-eWallet";

    
        /**
         * value: "miscellaneous"
         * @const
         */
        "miscellaneous" = "miscellaneous";

    
        /**
         * value: "Bancontact"
         * @const
         */
        "Bancontact" = "Bancontact";

    
        /**
         * value: "MTS"
         * @const
         */
        "MTS" = "MTS";

    
        /**
         * value: "MuchBetter"
         * @const
         */
        "MuchBetter" = "MuchBetter";

    
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
         * value: "Nordea-Solo"
         * @const
         */
        "Nordea-Solo" = "Nordea-Solo";

    
        /**
         * value: "OchaPay"
         * @const
         */
        "OchaPay" = "OchaPay";

    
        /**
         * value: "online-bank-transfer"
         * @const
         */
        "online-bank-transfer" = "online-bank-transfer";

    
        /**
         * value: "Onlineueberweisen"
         * @const
         */
        "Onlineueberweisen" = "Onlineueberweisen";

    
        /**
         * value: "oriental-wallet"
         * @const
         */
        "oriental-wallet" = "oriental-wallet";

    
        /**
         * value: "OXXO"
         * @const
         */
        "OXXO" = "OXXO";

    
        /**
         * value: "Pagsmile-deposit-express"
         * @const
         */
        "Pagsmile-deposit-express" = "Pagsmile-deposit-express";

    
        /**
         * value: "Pagsmile-lottery"
         * @const
         */
        "Pagsmile-lottery" = "Pagsmile-lottery";

    
        /**
         * value: "PayCash"
         * @const
         */
        "PayCash" = "PayCash";

    
        /**
         * value: "Payeer"
         * @const
         */
        "Payeer" = "Payeer";

    
        /**
         * value: "PaymentAsia-crypto"
         * @const
         */
        "PaymentAsia-crypto" = "PaymentAsia-crypto";

    
        /**
         * value: "Paymero"
         * @const
         */
        "Paymero" = "Paymero";

    
        /**
         * value: "Perfect-money"
         * @const
         */
        "Perfect-money" = "Perfect-money";

    
        /**
         * value: "Piastrix"
         * @const
         */
        "Piastrix" = "Piastrix";

    
        /**
         * value: "plaid-account"
         * @const
         */
        "plaid-account" = "plaid-account";

    
        /**
         * value: "PayTabs"
         * @const
         */
        "PayTabs" = "PayTabs";

    
        /**
         * value: "Paysafecard"
         * @const
         */
        "Paysafecard" = "Paysafecard";

    
        /**
         * value: "Paysafecash"
         * @const
         */
        "Paysafecash" = "Paysafecash";

    
        /**
         * value: "Pay4Fun"
         * @const
         */
        "Pay4Fun" = "Pay4Fun";

    
        /**
         * value: "PinPay"
         * @const
         */
        "PinPay" = "PinPay";

    
        /**
         * value: "phone"
         * @const
         */
        "phone" = "phone";

    
        /**
         * value: "PhonePe"
         * @const
         */
        "PhonePe" = "PhonePe";

    
        /**
         * value: "POLi"
         * @const
         */
        "POLi" = "POLi";

    
        /**
         * value: "PostFinance-card"
         * @const
         */
        "PostFinance-card" = "PostFinance-card";

    
        /**
         * value: "PostFinance-e-finance"
         * @const
         */
        "PostFinance-e-finance" = "PostFinance-e-finance";

    
        /**
         * value: "Przelewy24"
         * @const
         */
        "Przelewy24" = "Przelewy24";

    
        /**
         * value: "QIWI"
         * @const
         */
        "QIWI" = "QIWI";

    
        /**
         * value: "QQPay"
         * @const
         */
        "QQPay" = "QQPay";

    
        /**
         * value: "Resurs"
         * @const
         */
        "Resurs" = "Resurs";

    
        /**
         * value: "SEPA"
         * @const
         */
        "SEPA" = "SEPA";

    
        /**
         * value: "Skrill"
         * @const
         */
        "Skrill" = "Skrill";

    
        /**
         * value: "Skrill Rapid Transfer"
         * @const
         */
        "Skrill Rapid Transfer" = "Skrill Rapid Transfer";

    
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
         * value: "swift-dbt"
         * @const
         */
        "swift-dbt" = "swift-dbt";

    
        /**
         * value: "Tele2"
         * @const
         */
        "Tele2" = "Tele2";

    
        /**
         * value: "Terminaly-RF"
         * @const
         */
        "Terminaly-RF" = "Terminaly-RF";

    
        /**
         * value: "ToditoCash-card"
         * @const
         */
        "ToditoCash-card" = "ToditoCash-card";

    
        /**
         * value: "Trustly"
         * @const
         */
        "Trustly" = "Trustly";

    
        /**
         * value: "UPayCard"
         * @const
         */
        "UPayCard" = "UPayCard";

    
        /**
         * value: "UPI"
         * @const
         */
        "UPI" = "UPI";

    
        /**
         * value: "VCreditos"
         * @const
         */
        "VCreditos" = "VCreditos";

    
        /**
         * value: "VenusPoint"
         * @const
         */
        "VenusPoint" = "VenusPoint";

    
        /**
         * value: "voucher"
         * @const
         */
        "voucher" = "voucher";

    
        /**
         * value: "voucher-2"
         * @const
         */
        "voucher-2" = "voucher-2";

    
        /**
         * value: "voucher-3"
         * @const
         */
        "voucher-3" = "voucher-3";

    
        /**
         * value: "voucher-4"
         * @const
         */
        "voucher-4" = "voucher-4";

    
        /**
         * value: "Webmoney"
         * @const
         */
        "Webmoney" = "Webmoney";

    
        /**
         * value: "Webpay"
         * @const
         */
        "Webpay" = "Webpay";

    
        /**
         * value: "Webpay-2"
         * @const
         */
        "Webpay-2" = "Webpay-2";

    
        /**
         * value: "Webpay Card"
         * @const
         */
        "Webpay Card" = "Webpay Card";

    
        /**
         * value: "WeChat Pay"
         * @const
         */
        "WeChat Pay" = "WeChat Pay";

    
        /**
         * value: "XPay-P2P"
         * @const
         */
        "XPay-P2P" = "XPay-P2P";

    
        /**
         * value: "XPay-QR"
         * @const
         */
        "XPay-QR" = "XPay-QR";

    
        /**
         * value: "Yandex-money"
         * @const
         */
        "Yandex-money" = "Yandex-money";

    
        /**
         * value: "Zotapay"
         * @const
         */
        "Zotapay" = "Zotapay";

    
        /**
         * value: "Zimpler"
         * @const
         */
        "Zimpler" = "Zimpler";

    

    /**
    * Returns a <code>AlternativePaymentMethods</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/AlternativePaymentMethods} The enum <code>AlternativePaymentMethods</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

