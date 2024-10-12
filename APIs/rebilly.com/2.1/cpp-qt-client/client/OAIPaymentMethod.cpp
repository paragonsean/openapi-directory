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

#include "OAIPaymentMethod.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentMethod::OAIPaymentMethod(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentMethod::OAIPaymentMethod() {
    this->initializeModel();
}

OAIPaymentMethod::~OAIPaymentMethod() {}

void OAIPaymentMethod::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIPaymentMethod::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIPaymentMethod::fromJson(QString jsonString) {
    
    if ( jsonString.compare("payment-card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYMENT_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ach", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ACH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("check", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CHECK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("paypal", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYPAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AdvCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ADVCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Airpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::AIRPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Alfa-click", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ALFA_CLICK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Alipay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ALIPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Apple Pay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::APPLE_PAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AstroPay Card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ASTROPAY_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AstroPay-GO", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ASTROPAY_GO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-3", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_3;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-4", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_4;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-5", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_5;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-6", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_6;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-7", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_7;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-8", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_8;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bank-transfer-9", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANK_TRANSFER_9;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Beeline", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BEELINE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Belfius-direct-net", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BELFIUS_DIRECT_NET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bitcoin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BITCOIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Boleto", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BOLETO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Boleto-2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BOLETO_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Boleto-3", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BOLETO_3;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cash-deposit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CASH_DEPOSIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CASHlib", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CASHLIB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CashToCode", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CASHTOCODE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CCAvenue", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CCAVENUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("China UnionPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CHINA_UNIONPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CODVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CODVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Conekta-oxxo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CONEKTA_OXXO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Conekta-spei", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CONEKTA_SPEI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cryptocurrency", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CRYPTOCURRENCY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cupon-de-pagos", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CUPON_DE_PAGOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CyberSource", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::CYBERSOURCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("domestic-cards", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::DOMESTIC_CARDS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("echeck", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ECHECK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ecoPayz", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ECOPAYZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ecoVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ECOVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EPS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::EPS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ePay.bg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::EPAY_BG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Ethereum", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ETHEREUM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("e-wallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::E_WALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ezyEFT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::EZYEFT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("eZeeWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::EZEEWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Flexepin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::FLEXEPIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Giropay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::GIROPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Google Pay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::GOOGLE_PAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gpaysafe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::GPAYSAFE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iDebit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::IDEBIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iDEAL", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::IDEAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ING-homepay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ING_HOMEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INOVAPAY-pin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INOVAPAY_PIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INOVAPAY-wallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INOVAPAY_WALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("InstaDebit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INSTADEBIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("instant-bank-transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INSTANT_BANK_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Interac-online", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INTERAC_ONLINE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Interac-eTransfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INTERAC_ETRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Interac-express-connect", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INTERAC_EXPRESS_CONNECT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Interac", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INTERAC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::INVOICE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::IWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Jeton", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::JETON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("jpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::JPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Khelocard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::KHELOCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Klarna", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::KLARNA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Litecoin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::LITECOIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("loonie", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::LOONIE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LPG-online", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::LPG_ONLINE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LPG-payment-card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::LPG_PAYMENT_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Megafon", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::MEGAFON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MiFinity-eWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::MIFINITY_EWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("miscellaneous", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::MISCELLANEOUS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bancontact", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::BANCONTACT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MTS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::MTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MuchBetter", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::MUCHBETTER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MyFatoorah", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::MYFATOORAH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neosurf", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::NEOSURF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Netbanking", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::NETBANKING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neteller", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::NETELLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Nordea-Solo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::NORDEA_SOLO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OchaPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::OCHAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("online-bank-transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ONLINE_BANK_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Onlineueberweisen", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ONLINEUEBERWEISEN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("oriental-wallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ORIENTAL_WALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OXXO", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::OXXO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pagsmile-lottery", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAGSMILE_LOTTERY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pagsmile-deposit-express", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAGSMILE_DEPOSIT_EXPRESS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payeer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYEER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymentAsia-crypto", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYMENTASIA_CRYPTO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paysafecard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYSAFECARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayTabs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYTABS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pay4Fun", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAY4FUN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paymero", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYMERO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paymero-QR", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYMERO_QR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayULatam", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PAYULATAM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Perfect-money", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PERFECT_MONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Piastrix", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PIASTRIX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PIX", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PIX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PinPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PINPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("phone", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PHONE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PhonePe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PHONEPE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("POLi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::POLI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PostFinance-card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::POSTFINANCE_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PostFinance-e-finance", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::POSTFINANCE_E_FINANCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Przelewy24", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::PRZELEWY24;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("QIWI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::QIWI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("QQPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::QQPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Resurs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::RESURS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SEPA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SEPA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Siirto", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SIIRTO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Skrill", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SKRILL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Skrill Rapid Transfer", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SKRILL_RAPID_TRANSFER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SMSVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SMSVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Sofort", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SOFORT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SparkPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SPARKPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("swift-dbt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::SWIFT_DBT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Tele2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::TELE2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Terminaly-RF", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::TERMINALY_RF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Tether", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::TETHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ToditoCash-card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::TODITOCASH_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Trustly", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::TRUSTLY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TWINT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::TWINT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UniCrypt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::UNICRYPT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPayCard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::UPAYCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::UPI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VCreditos", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::VCREDITOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VenusPoint", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::VENUSPOINT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::VOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher-2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::VOUCHER_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher-3", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::VOUCHER_3;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("voucher-4", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::VOUCHER_4;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webmoney", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::WEBMONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::WEBPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webpay-2", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::WEBPAY_2;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Webpay Card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::WEBPAY_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WeChat Pay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::WECHAT_PAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPay-P2P", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::XPAY_P2P;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPay-QR", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::XPAY_QR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Yandex-money", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::YANDEX_MONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zotapay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ZOTAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zimpler", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPaymentMethod::ZIMPLER;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIPaymentMethod::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIPaymentMethod::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIPaymentMethod::PAYMENT_CARD:
            val = "payment-card";
            break;
        case eOAIPaymentMethod::ACH:
            val = "ach";
            break;
        case eOAIPaymentMethod::CASH:
            val = "cash";
            break;
        case eOAIPaymentMethod::CHECK:
            val = "check";
            break;
        case eOAIPaymentMethod::PAYPAL:
            val = "paypal";
            break;
        case eOAIPaymentMethod::ADVCASH:
            val = "AdvCash";
            break;
        case eOAIPaymentMethod::AIRPAY:
            val = "Airpay";
            break;
        case eOAIPaymentMethod::ALFA_CLICK:
            val = "Alfa-click";
            break;
        case eOAIPaymentMethod::ALIPAY:
            val = "Alipay";
            break;
        case eOAIPaymentMethod::APPLE_PAY:
            val = "Apple Pay";
            break;
        case eOAIPaymentMethod::ASTROPAY_CARD:
            val = "AstroPay Card";
            break;
        case eOAIPaymentMethod::ASTROPAY_GO:
            val = "AstroPay-GO";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER:
            val = "bank-transfer";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_2:
            val = "bank-transfer-2";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_3:
            val = "bank-transfer-3";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_4:
            val = "bank-transfer-4";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_5:
            val = "bank-transfer-5";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_6:
            val = "bank-transfer-6";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_7:
            val = "bank-transfer-7";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_8:
            val = "bank-transfer-8";
            break;
        case eOAIPaymentMethod::BANK_TRANSFER_9:
            val = "bank-transfer-9";
            break;
        case eOAIPaymentMethod::BEELINE:
            val = "Beeline";
            break;
        case eOAIPaymentMethod::BELFIUS_DIRECT_NET:
            val = "Belfius-direct-net";
            break;
        case eOAIPaymentMethod::BITCOIN:
            val = "bitcoin";
            break;
        case eOAIPaymentMethod::BOLETO:
            val = "Boleto";
            break;
        case eOAIPaymentMethod::BOLETO_2:
            val = "Boleto-2";
            break;
        case eOAIPaymentMethod::BOLETO_3:
            val = "Boleto-3";
            break;
        case eOAIPaymentMethod::CASH_DEPOSIT:
            val = "cash-deposit";
            break;
        case eOAIPaymentMethod::CASHLIB:
            val = "CASHlib";
            break;
        case eOAIPaymentMethod::CASHTOCODE:
            val = "CashToCode";
            break;
        case eOAIPaymentMethod::CCAVENUE:
            val = "CCAvenue";
            break;
        case eOAIPaymentMethod::CHINA_UNIONPAY:
            val = "China UnionPay";
            break;
        case eOAIPaymentMethod::CODVOUCHER:
            val = "CODVoucher";
            break;
        case eOAIPaymentMethod::CONEKTA_OXXO:
            val = "Conekta-oxxo";
            break;
        case eOAIPaymentMethod::CONEKTA_SPEI:
            val = "Conekta-spei";
            break;
        case eOAIPaymentMethod::CRYPTOCURRENCY:
            val = "cryptocurrency";
            break;
        case eOAIPaymentMethod::CUPON_DE_PAGOS:
            val = "Cupon-de-pagos";
            break;
        case eOAIPaymentMethod::CYBERSOURCE:
            val = "CyberSource";
            break;
        case eOAIPaymentMethod::DOMESTIC_CARDS:
            val = "domestic-cards";
            break;
        case eOAIPaymentMethod::ECHECK:
            val = "echeck";
            break;
        case eOAIPaymentMethod::ECOPAYZ:
            val = "ecoPayz";
            break;
        case eOAIPaymentMethod::ECOVOUCHER:
            val = "ecoVoucher";
            break;
        case eOAIPaymentMethod::EPS:
            val = "EPS";
            break;
        case eOAIPaymentMethod::EPAY_BG:
            val = "ePay.bg";
            break;
        case eOAIPaymentMethod::ETHEREUM:
            val = "Ethereum";
            break;
        case eOAIPaymentMethod::E_WALLET:
            val = "e-wallet";
            break;
        case eOAIPaymentMethod::EZYEFT:
            val = "ezyEFT";
            break;
        case eOAIPaymentMethod::EZEEWALLET:
            val = "eZeeWallet";
            break;
        case eOAIPaymentMethod::FLEXEPIN:
            val = "Flexepin";
            break;
        case eOAIPaymentMethod::GIROPAY:
            val = "Giropay";
            break;
        case eOAIPaymentMethod::GOOGLE_PAY:
            val = "Google Pay";
            break;
        case eOAIPaymentMethod::GPAYSAFE:
            val = "Gpaysafe";
            break;
        case eOAIPaymentMethod::IDEBIT:
            val = "iDebit";
            break;
        case eOAIPaymentMethod::IDEAL:
            val = "iDEAL";
            break;
        case eOAIPaymentMethod::ING_HOMEPAY:
            val = "ING-homepay";
            break;
        case eOAIPaymentMethod::INOVAPAY_PIN:
            val = "INOVAPAY-pin";
            break;
        case eOAIPaymentMethod::INOVAPAY_WALLET:
            val = "INOVAPAY-wallet";
            break;
        case eOAIPaymentMethod::INSTADEBIT:
            val = "InstaDebit";
            break;
        case eOAIPaymentMethod::INSTANT_BANK_TRANSFER:
            val = "instant-bank-transfer";
            break;
        case eOAIPaymentMethod::INTERAC_ONLINE:
            val = "Interac-online";
            break;
        case eOAIPaymentMethod::INTERAC_ETRANSFER:
            val = "Interac-eTransfer";
            break;
        case eOAIPaymentMethod::INTERAC_EXPRESS_CONNECT:
            val = "Interac-express-connect";
            break;
        case eOAIPaymentMethod::INTERAC:
            val = "Interac";
            break;
        case eOAIPaymentMethod::INVOICE:
            val = "invoice";
            break;
        case eOAIPaymentMethod::IWALLET:
            val = "iWallet";
            break;
        case eOAIPaymentMethod::JETON:
            val = "Jeton";
            break;
        case eOAIPaymentMethod::JPAY:
            val = "jpay";
            break;
        case eOAIPaymentMethod::KHELOCARD:
            val = "Khelocard";
            break;
        case eOAIPaymentMethod::KLARNA:
            val = "Klarna";
            break;
        case eOAIPaymentMethod::LITECOIN:
            val = "Litecoin";
            break;
        case eOAIPaymentMethod::LOONIE:
            val = "loonie";
            break;
        case eOAIPaymentMethod::LPG_ONLINE:
            val = "LPG-online";
            break;
        case eOAIPaymentMethod::LPG_PAYMENT_CARD:
            val = "LPG-payment-card";
            break;
        case eOAIPaymentMethod::MEGAFON:
            val = "Megafon";
            break;
        case eOAIPaymentMethod::MIFINITY_EWALLET:
            val = "MiFinity-eWallet";
            break;
        case eOAIPaymentMethod::MISCELLANEOUS:
            val = "miscellaneous";
            break;
        case eOAIPaymentMethod::BANCONTACT:
            val = "Bancontact";
            break;
        case eOAIPaymentMethod::MTS:
            val = "MTS";
            break;
        case eOAIPaymentMethod::MUCHBETTER:
            val = "MuchBetter";
            break;
        case eOAIPaymentMethod::MYFATOORAH:
            val = "MyFatoorah";
            break;
        case eOAIPaymentMethod::NEOSURF:
            val = "Neosurf";
            break;
        case eOAIPaymentMethod::NETBANKING:
            val = "Netbanking";
            break;
        case eOAIPaymentMethod::NETELLER:
            val = "Neteller";
            break;
        case eOAIPaymentMethod::NORDEA_SOLO:
            val = "Nordea-Solo";
            break;
        case eOAIPaymentMethod::OCHAPAY:
            val = "OchaPay";
            break;
        case eOAIPaymentMethod::ONLINE_BANK_TRANSFER:
            val = "online-bank-transfer";
            break;
        case eOAIPaymentMethod::ONLINEUEBERWEISEN:
            val = "Onlineueberweisen";
            break;
        case eOAIPaymentMethod::ORIENTAL_WALLET:
            val = "oriental-wallet";
            break;
        case eOAIPaymentMethod::OXXO:
            val = "OXXO";
            break;
        case eOAIPaymentMethod::PAGSMILE_LOTTERY:
            val = "Pagsmile-lottery";
            break;
        case eOAIPaymentMethod::PAGSMILE_DEPOSIT_EXPRESS:
            val = "Pagsmile-deposit-express";
            break;
        case eOAIPaymentMethod::PAYCASH:
            val = "PayCash";
            break;
        case eOAIPaymentMethod::PAYEER:
            val = "Payeer";
            break;
        case eOAIPaymentMethod::PAYMENTASIA_CRYPTO:
            val = "PaymentAsia-crypto";
            break;
        case eOAIPaymentMethod::PAYSAFECARD:
            val = "Paysafecard";
            break;
        case eOAIPaymentMethod::PAYTABS:
            val = "PayTabs";
            break;
        case eOAIPaymentMethod::PAY4FUN:
            val = "Pay4Fun";
            break;
        case eOAIPaymentMethod::PAYMERO:
            val = "Paymero";
            break;
        case eOAIPaymentMethod::PAYMERO_QR:
            val = "Paymero-QR";
            break;
        case eOAIPaymentMethod::PAYULATAM:
            val = "PayULatam";
            break;
        case eOAIPaymentMethod::PERFECT_MONEY:
            val = "Perfect-money";
            break;
        case eOAIPaymentMethod::PIASTRIX:
            val = "Piastrix";
            break;
        case eOAIPaymentMethod::PIX:
            val = "PIX";
            break;
        case eOAIPaymentMethod::PINPAY:
            val = "PinPay";
            break;
        case eOAIPaymentMethod::PHONE:
            val = "phone";
            break;
        case eOAIPaymentMethod::PHONEPE:
            val = "PhonePe";
            break;
        case eOAIPaymentMethod::POLI:
            val = "POLi";
            break;
        case eOAIPaymentMethod::POSTFINANCE_CARD:
            val = "PostFinance-card";
            break;
        case eOAIPaymentMethod::POSTFINANCE_E_FINANCE:
            val = "PostFinance-e-finance";
            break;
        case eOAIPaymentMethod::PRZELEWY24:
            val = "Przelewy24";
            break;
        case eOAIPaymentMethod::QIWI:
            val = "QIWI";
            break;
        case eOAIPaymentMethod::QQPAY:
            val = "QQPay";
            break;
        case eOAIPaymentMethod::RESURS:
            val = "Resurs";
            break;
        case eOAIPaymentMethod::SEPA:
            val = "SEPA";
            break;
        case eOAIPaymentMethod::SIIRTO:
            val = "Siirto";
            break;
        case eOAIPaymentMethod::SKRILL:
            val = "Skrill";
            break;
        case eOAIPaymentMethod::SKRILL_RAPID_TRANSFER:
            val = "Skrill Rapid Transfer";
            break;
        case eOAIPaymentMethod::SMSVOUCHER:
            val = "SMSVoucher";
            break;
        case eOAIPaymentMethod::SOFORT:
            val = "Sofort";
            break;
        case eOAIPaymentMethod::SPARKPAY:
            val = "SparkPay";
            break;
        case eOAIPaymentMethod::SWIFT_DBT:
            val = "swift-dbt";
            break;
        case eOAIPaymentMethod::TELE2:
            val = "Tele2";
            break;
        case eOAIPaymentMethod::TERMINALY_RF:
            val = "Terminaly-RF";
            break;
        case eOAIPaymentMethod::TETHER:
            val = "Tether";
            break;
        case eOAIPaymentMethod::TODITOCASH_CARD:
            val = "ToditoCash-card";
            break;
        case eOAIPaymentMethod::TRUSTLY:
            val = "Trustly";
            break;
        case eOAIPaymentMethod::TWINT:
            val = "TWINT";
            break;
        case eOAIPaymentMethod::UNICRYPT:
            val = "UniCrypt";
            break;
        case eOAIPaymentMethod::UPAYCARD:
            val = "UPayCard";
            break;
        case eOAIPaymentMethod::UPI:
            val = "UPI";
            break;
        case eOAIPaymentMethod::VCREDITOS:
            val = "VCreditos";
            break;
        case eOAIPaymentMethod::VENUSPOINT:
            val = "VenusPoint";
            break;
        case eOAIPaymentMethod::VOUCHER:
            val = "voucher";
            break;
        case eOAIPaymentMethod::VOUCHER_2:
            val = "voucher-2";
            break;
        case eOAIPaymentMethod::VOUCHER_3:
            val = "voucher-3";
            break;
        case eOAIPaymentMethod::VOUCHER_4:
            val = "voucher-4";
            break;
        case eOAIPaymentMethod::WEBMONEY:
            val = "Webmoney";
            break;
        case eOAIPaymentMethod::WEBPAY:
            val = "Webpay";
            break;
        case eOAIPaymentMethod::WEBPAY_2:
            val = "Webpay-2";
            break;
        case eOAIPaymentMethod::WEBPAY_CARD:
            val = "Webpay Card";
            break;
        case eOAIPaymentMethod::WECHAT_PAY:
            val = "WeChat Pay";
            break;
        case eOAIPaymentMethod::XPAY_P2P:
            val = "XPay-P2P";
            break;
        case eOAIPaymentMethod::XPAY_QR:
            val = "XPay-QR";
            break;
        case eOAIPaymentMethod::YANDEX_MONEY:
            val = "Yandex-money";
            break;
        case eOAIPaymentMethod::ZOTAPAY:
            val = "Zotapay";
            break;
        case eOAIPaymentMethod::ZIMPLER:
            val = "Zimpler";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIPaymentMethod::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIPaymentMethod::eOAIPaymentMethod OAIPaymentMethod::getValue() const {
    return m_value;
}

void OAIPaymentMethod::setValue(const OAIPaymentMethod::eOAIPaymentMethod& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIPaymentMethod::isSet() const {
    
    return m_value_isSet;
}

bool OAIPaymentMethod::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
