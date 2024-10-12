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
 */

#include "OAIAlternativePaymentMethods.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlternativePaymentMethods::OAIAlternativePaymentMethods(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlternativePaymentMethods::OAIAlternativePaymentMethods() {
    this->initializeModel();
}

OAIAlternativePaymentMethods::~OAIAlternativePaymentMethods() {}

void OAIAlternativePaymentMethods::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIAlternativePaymentMethods::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIAlternativePaymentMethods::fromJson(QString jsonString) {
    
    if ( jsonString.compare("cash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("check", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CHECK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("paypal", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYPAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AdvCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ADVCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Alfa-click", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ALFA_CLICK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Alipay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ALIPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AstroPay Card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ASTROPAY_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AstroPay-GO", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ASTROPAY_GO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-3", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_3;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-4", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_4;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-5", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_5;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-6", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_6;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-7", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_7;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-8", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_8;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-9", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANK_TRANSFER_9;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Beeline", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BEELINE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Belfius-direct-net", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BELFIUS_DIRECT_NET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bitcoin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BITCOIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Boleto", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BOLETO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cash-deposit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CASH_DEPOSIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CASHlib", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CASHLIB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CashToCode", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CASHTOCODE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("China UnionPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CHINA_UNIONPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CODVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CODVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Conekta-oxxo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CONEKTA_OXXO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cupon-de-pagos", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CUPON_DE_PAGOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cryptocurrency", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::CRYPTOCURRENCY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("domestic-cards", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::DOMESTIC_CARDS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("echeck", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ECHECK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ecoPayz", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ECOPAYZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ecoVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ECOVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EPS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::EPS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ePay.bg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::EPAY_BG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("eZeeWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::EZEEWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Flexepin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::FLEXEPIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Giropay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::GIROPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gpaysafe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::GPAYSAFE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Google Pay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::GOOGLE_PAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iDebit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::IDEBIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iDEAL", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::IDEAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ING-homepay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ING_HOMEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INOVAPAY-pin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INOVAPAY_PIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INOVAPAY-wallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INOVAPAY_WALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("InstaDebit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INSTADEBIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("instant-bank-transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INSTANT_BANK_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Interac", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INTERAC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Interac-online", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INTERAC_ONLINE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Interac-eTransfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INTERAC_ETRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::INVOICE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::IWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Jeton", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::JETON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("jpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::JPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Khelocard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::KHELOCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Klarna", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::KLARNA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("loonie", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::LOONIE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Megafon", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::MEGAFON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MiFinity-eWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::MIFINITY_EWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("miscellaneous", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::MISCELLANEOUS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bancontact", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::BANCONTACT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MTS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::MTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MuchBetter", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::MUCHBETTER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neosurf", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::NEOSURF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Netbanking", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::NETBANKING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neteller", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::NETELLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Nordea-Solo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::NORDEA_SOLO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OchaPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::OCHAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("online-bank-transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ONLINE_BANK_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Onlineueberweisen", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ONLINEUEBERWEISEN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("oriental-wallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ORIENTAL_WALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OXXO", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::OXXO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pagsmile-deposit-express", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAGSMILE_DEPOSIT_EXPRESS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pagsmile-lottery", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAGSMILE_LOTTERY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payeer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYEER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymentAsia-crypto", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYMENTASIA_CRYPTO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paymero", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYMERO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Perfect-money", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PERFECT_MONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Piastrix", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PIASTRIX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("plaid-account", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PLAID_ACCOUNT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayTabs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYTABS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paysafecard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYSAFECARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paysafecash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAYSAFECASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pay4Fun", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PAY4FUN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PinPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PINPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("phone", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PHONE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PhonePe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PHONEPE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("POLi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::POLI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PostFinance-card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::POSTFINANCE_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PostFinance-e-finance", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::POSTFINANCE_E_FINANCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Przelewy24", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::PRZELEWY24;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("QIWI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::QIWI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("QQPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::QQPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Resurs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::RESURS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SEPA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::SEPA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Skrill", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::SKRILL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Skrill Rapid Transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::SKRILL_RAPID_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SMSVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::SMSVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Sofort", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::SOFORT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SparkPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::SPARKPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("swift-dbt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::SWIFT_DBT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Tele2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::TELE2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Terminaly-RF", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::TERMINALY_RF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ToditoCash-card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::TODITOCASH_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Trustly", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::TRUSTLY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPayCard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::UPAYCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::UPI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VCreditos", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::VCREDITOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VenusPoint", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::VENUSPOINT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::VOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher-2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::VOUCHER_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher-3", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::VOUCHER_3;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher-4", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::VOUCHER_4;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webmoney", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::WEBMONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::WEBPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webpay-2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::WEBPAY_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webpay Card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::WEBPAY_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WeChat Pay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::WECHAT_PAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPay-P2P", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::XPAY_P2P;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPay-QR", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::XPAY_QR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Yandex-money", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::YANDEX_MONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zotapay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ZOTAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zimpler", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAlternativePaymentMethods::ZIMPLER;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIAlternativePaymentMethods::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIAlternativePaymentMethods::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIAlternativePaymentMethods::CASH:
            val = "cash";
            break;
        case eOAIAlternativePaymentMethods::CHECK:
            val = "check";
            break;
        case eOAIAlternativePaymentMethods::PAYPAL:
            val = "paypal";
            break;
        case eOAIAlternativePaymentMethods::ADVCASH:
            val = "AdvCash";
            break;
        case eOAIAlternativePaymentMethods::ALFA_CLICK:
            val = "Alfa-click";
            break;
        case eOAIAlternativePaymentMethods::ALIPAY:
            val = "Alipay";
            break;
        case eOAIAlternativePaymentMethods::ASTROPAY_CARD:
            val = "AstroPay Card";
            break;
        case eOAIAlternativePaymentMethods::ASTROPAY_GO:
            val = "AstroPay-GO";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER:
            val = "bank-transfer";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_2:
            val = "bank-transfer-2";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_3:
            val = "bank-transfer-3";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_4:
            val = "bank-transfer-4";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_5:
            val = "bank-transfer-5";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_6:
            val = "bank-transfer-6";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_7:
            val = "bank-transfer-7";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_8:
            val = "bank-transfer-8";
            break;
        case eOAIAlternativePaymentMethods::BANK_TRANSFER_9:
            val = "bank-transfer-9";
            break;
        case eOAIAlternativePaymentMethods::BEELINE:
            val = "Beeline";
            break;
        case eOAIAlternativePaymentMethods::BELFIUS_DIRECT_NET:
            val = "Belfius-direct-net";
            break;
        case eOAIAlternativePaymentMethods::BITCOIN:
            val = "bitcoin";
            break;
        case eOAIAlternativePaymentMethods::BOLETO:
            val = "Boleto";
            break;
        case eOAIAlternativePaymentMethods::CASH_DEPOSIT:
            val = "cash-deposit";
            break;
        case eOAIAlternativePaymentMethods::CASHLIB:
            val = "CASHlib";
            break;
        case eOAIAlternativePaymentMethods::CASHTOCODE:
            val = "CashToCode";
            break;
        case eOAIAlternativePaymentMethods::CHINA_UNIONPAY:
            val = "China UnionPay";
            break;
        case eOAIAlternativePaymentMethods::CODVOUCHER:
            val = "CODVoucher";
            break;
        case eOAIAlternativePaymentMethods::CONEKTA_OXXO:
            val = "Conekta-oxxo";
            break;
        case eOAIAlternativePaymentMethods::CUPON_DE_PAGOS:
            val = "Cupon-de-pagos";
            break;
        case eOAIAlternativePaymentMethods::CRYPTOCURRENCY:
            val = "cryptocurrency";
            break;
        case eOAIAlternativePaymentMethods::DOMESTIC_CARDS:
            val = "domestic-cards";
            break;
        case eOAIAlternativePaymentMethods::ECHECK:
            val = "echeck";
            break;
        case eOAIAlternativePaymentMethods::ECOPAYZ:
            val = "ecoPayz";
            break;
        case eOAIAlternativePaymentMethods::ECOVOUCHER:
            val = "ecoVoucher";
            break;
        case eOAIAlternativePaymentMethods::EPS:
            val = "EPS";
            break;
        case eOAIAlternativePaymentMethods::EPAY_BG:
            val = "ePay.bg";
            break;
        case eOAIAlternativePaymentMethods::EZEEWALLET:
            val = "eZeeWallet";
            break;
        case eOAIAlternativePaymentMethods::FLEXEPIN:
            val = "Flexepin";
            break;
        case eOAIAlternativePaymentMethods::GIROPAY:
            val = "Giropay";
            break;
        case eOAIAlternativePaymentMethods::GPAYSAFE:
            val = "Gpaysafe";
            break;
        case eOAIAlternativePaymentMethods::GOOGLE_PAY:
            val = "Google Pay";
            break;
        case eOAIAlternativePaymentMethods::IDEBIT:
            val = "iDebit";
            break;
        case eOAIAlternativePaymentMethods::IDEAL:
            val = "iDEAL";
            break;
        case eOAIAlternativePaymentMethods::ING_HOMEPAY:
            val = "ING-homepay";
            break;
        case eOAIAlternativePaymentMethods::INOVAPAY_PIN:
            val = "INOVAPAY-pin";
            break;
        case eOAIAlternativePaymentMethods::INOVAPAY_WALLET:
            val = "INOVAPAY-wallet";
            break;
        case eOAIAlternativePaymentMethods::INSTADEBIT:
            val = "InstaDebit";
            break;
        case eOAIAlternativePaymentMethods::INSTANT_BANK_TRANSFER:
            val = "instant-bank-transfer";
            break;
        case eOAIAlternativePaymentMethods::INTERAC:
            val = "Interac";
            break;
        case eOAIAlternativePaymentMethods::INTERAC_ONLINE:
            val = "Interac-online";
            break;
        case eOAIAlternativePaymentMethods::INTERAC_ETRANSFER:
            val = "Interac-eTransfer";
            break;
        case eOAIAlternativePaymentMethods::INVOICE:
            val = "invoice";
            break;
        case eOAIAlternativePaymentMethods::IWALLET:
            val = "iWallet";
            break;
        case eOAIAlternativePaymentMethods::JETON:
            val = "Jeton";
            break;
        case eOAIAlternativePaymentMethods::JPAY:
            val = "jpay";
            break;
        case eOAIAlternativePaymentMethods::KHELOCARD:
            val = "Khelocard";
            break;
        case eOAIAlternativePaymentMethods::KLARNA:
            val = "Klarna";
            break;
        case eOAIAlternativePaymentMethods::LOONIE:
            val = "loonie";
            break;
        case eOAIAlternativePaymentMethods::MEGAFON:
            val = "Megafon";
            break;
        case eOAIAlternativePaymentMethods::MIFINITY_EWALLET:
            val = "MiFinity-eWallet";
            break;
        case eOAIAlternativePaymentMethods::MISCELLANEOUS:
            val = "miscellaneous";
            break;
        case eOAIAlternativePaymentMethods::BANCONTACT:
            val = "Bancontact";
            break;
        case eOAIAlternativePaymentMethods::MTS:
            val = "MTS";
            break;
        case eOAIAlternativePaymentMethods::MUCHBETTER:
            val = "MuchBetter";
            break;
        case eOAIAlternativePaymentMethods::NEOSURF:
            val = "Neosurf";
            break;
        case eOAIAlternativePaymentMethods::NETBANKING:
            val = "Netbanking";
            break;
        case eOAIAlternativePaymentMethods::NETELLER:
            val = "Neteller";
            break;
        case eOAIAlternativePaymentMethods::NORDEA_SOLO:
            val = "Nordea-Solo";
            break;
        case eOAIAlternativePaymentMethods::OCHAPAY:
            val = "OchaPay";
            break;
        case eOAIAlternativePaymentMethods::ONLINE_BANK_TRANSFER:
            val = "online-bank-transfer";
            break;
        case eOAIAlternativePaymentMethods::ONLINEUEBERWEISEN:
            val = "Onlineueberweisen";
            break;
        case eOAIAlternativePaymentMethods::ORIENTAL_WALLET:
            val = "oriental-wallet";
            break;
        case eOAIAlternativePaymentMethods::OXXO:
            val = "OXXO";
            break;
        case eOAIAlternativePaymentMethods::PAGSMILE_DEPOSIT_EXPRESS:
            val = "Pagsmile-deposit-express";
            break;
        case eOAIAlternativePaymentMethods::PAGSMILE_LOTTERY:
            val = "Pagsmile-lottery";
            break;
        case eOAIAlternativePaymentMethods::PAYCASH:
            val = "PayCash";
            break;
        case eOAIAlternativePaymentMethods::PAYEER:
            val = "Payeer";
            break;
        case eOAIAlternativePaymentMethods::PAYMENTASIA_CRYPTO:
            val = "PaymentAsia-crypto";
            break;
        case eOAIAlternativePaymentMethods::PAYMERO:
            val = "Paymero";
            break;
        case eOAIAlternativePaymentMethods::PERFECT_MONEY:
            val = "Perfect-money";
            break;
        case eOAIAlternativePaymentMethods::PIASTRIX:
            val = "Piastrix";
            break;
        case eOAIAlternativePaymentMethods::PLAID_ACCOUNT:
            val = "plaid-account";
            break;
        case eOAIAlternativePaymentMethods::PAYTABS:
            val = "PayTabs";
            break;
        case eOAIAlternativePaymentMethods::PAYSAFECARD:
            val = "Paysafecard";
            break;
        case eOAIAlternativePaymentMethods::PAYSAFECASH:
            val = "Paysafecash";
            break;
        case eOAIAlternativePaymentMethods::PAY4FUN:
            val = "Pay4Fun";
            break;
        case eOAIAlternativePaymentMethods::PINPAY:
            val = "PinPay";
            break;
        case eOAIAlternativePaymentMethods::PHONE:
            val = "phone";
            break;
        case eOAIAlternativePaymentMethods::PHONEPE:
            val = "PhonePe";
            break;
        case eOAIAlternativePaymentMethods::POLI:
            val = "POLi";
            break;
        case eOAIAlternativePaymentMethods::POSTFINANCE_CARD:
            val = "PostFinance-card";
            break;
        case eOAIAlternativePaymentMethods::POSTFINANCE_E_FINANCE:
            val = "PostFinance-e-finance";
            break;
        case eOAIAlternativePaymentMethods::PRZELEWY24:
            val = "Przelewy24";
            break;
        case eOAIAlternativePaymentMethods::QIWI:
            val = "QIWI";
            break;
        case eOAIAlternativePaymentMethods::QQPAY:
            val = "QQPay";
            break;
        case eOAIAlternativePaymentMethods::RESURS:
            val = "Resurs";
            break;
        case eOAIAlternativePaymentMethods::SEPA:
            val = "SEPA";
            break;
        case eOAIAlternativePaymentMethods::SKRILL:
            val = "Skrill";
            break;
        case eOAIAlternativePaymentMethods::SKRILL_RAPID_TRANSFER:
            val = "Skrill Rapid Transfer";
            break;
        case eOAIAlternativePaymentMethods::SMSVOUCHER:
            val = "SMSVoucher";
            break;
        case eOAIAlternativePaymentMethods::SOFORT:
            val = "Sofort";
            break;
        case eOAIAlternativePaymentMethods::SPARKPAY:
            val = "SparkPay";
            break;
        case eOAIAlternativePaymentMethods::SWIFT_DBT:
            val = "swift-dbt";
            break;
        case eOAIAlternativePaymentMethods::TELE2:
            val = "Tele2";
            break;
        case eOAIAlternativePaymentMethods::TERMINALY_RF:
            val = "Terminaly-RF";
            break;
        case eOAIAlternativePaymentMethods::TODITOCASH_CARD:
            val = "ToditoCash-card";
            break;
        case eOAIAlternativePaymentMethods::TRUSTLY:
            val = "Trustly";
            break;
        case eOAIAlternativePaymentMethods::UPAYCARD:
            val = "UPayCard";
            break;
        case eOAIAlternativePaymentMethods::UPI:
            val = "UPI";
            break;
        case eOAIAlternativePaymentMethods::VCREDITOS:
            val = "VCreditos";
            break;
        case eOAIAlternativePaymentMethods::VENUSPOINT:
            val = "VenusPoint";
            break;
        case eOAIAlternativePaymentMethods::VOUCHER:
            val = "voucher";
            break;
        case eOAIAlternativePaymentMethods::VOUCHER_2:
            val = "voucher-2";
            break;
        case eOAIAlternativePaymentMethods::VOUCHER_3:
            val = "voucher-3";
            break;
        case eOAIAlternativePaymentMethods::VOUCHER_4:
            val = "voucher-4";
            break;
        case eOAIAlternativePaymentMethods::WEBMONEY:
            val = "Webmoney";
            break;
        case eOAIAlternativePaymentMethods::WEBPAY:
            val = "Webpay";
            break;
        case eOAIAlternativePaymentMethods::WEBPAY_2:
            val = "Webpay-2";
            break;
        case eOAIAlternativePaymentMethods::WEBPAY_CARD:
            val = "Webpay Card";
            break;
        case eOAIAlternativePaymentMethods::WECHAT_PAY:
            val = "WeChat Pay";
            break;
        case eOAIAlternativePaymentMethods::XPAY_P2P:
            val = "XPay-P2P";
            break;
        case eOAIAlternativePaymentMethods::XPAY_QR:
            val = "XPay-QR";
            break;
        case eOAIAlternativePaymentMethods::YANDEX_MONEY:
            val = "Yandex-money";
            break;
        case eOAIAlternativePaymentMethods::ZOTAPAY:
            val = "Zotapay";
            break;
        case eOAIAlternativePaymentMethods::ZIMPLER:
            val = "Zimpler";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIAlternativePaymentMethods::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIAlternativePaymentMethods::eOAIAlternativePaymentMethods OAIAlternativePaymentMethods::getValue() const {
    return m_value;
}

void OAIAlternativePaymentMethods::setValue(const OAIAlternativePaymentMethods::eOAIAlternativePaymentMethods& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIAlternativePaymentMethods::isSet() const {
    
    return m_value_isSet;
}

bool OAIAlternativePaymentMethods::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
