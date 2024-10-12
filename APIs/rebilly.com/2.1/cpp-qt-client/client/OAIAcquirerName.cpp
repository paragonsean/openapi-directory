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

#include "OAIAcquirerName.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAcquirerName::OAIAcquirerName(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAcquirerName::OAIAcquirerName() {
    this->initializeModel();
}

OAIAcquirerName::~OAIAcquirerName() {}

void OAIAcquirerName::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIAcquirerName::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIAcquirerName::fromJson(QString jsonString) {
    
    if ( jsonString.compare("Adyen", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ADYEN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Alipay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ALIPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AIB", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::AIB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Airpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::AIRPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ApcoPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::APCOPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AsiaPaymentGateway", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ASIAPAYMENTGATEWAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AstroPay Card", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ASTROPAY_CARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Ipay Options", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::IPAY_OPTIONS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("B+S", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::B_S;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bambora", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BAMBORA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BitPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BITPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bank of America", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BANK_OF_AMERICA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bank of Moscow", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BANK_OF_MOSCOW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bank of Rebilly", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BANK_OF_REBILLY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bank One", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BANK_ONE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BMO Harris Bank", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BMO_HARRIS_BANK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Borgun", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BORGUN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BraintreePayments", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::BRAINTREEPAYMENTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cardknox", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CARDKNOX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CASHlib", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CASHLIB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CashToCode", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CASHTOCODE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Catalunya Caixa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CATALUNYA_CAIXA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CCAvenue", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CCAVENUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Chase", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CHASE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ChinaUnionPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CHINAUNIONPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CIM", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CIM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Circle", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CIRCLE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Citadel", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CITADEL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Clearhaus", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CLEARHAUS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CODVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CODVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CoinPayments", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::COINPAYMENTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Conekta", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CONEKTA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Coppr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::COPPR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Credorax", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CREDORAX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cryptonator", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CRYPTONATOR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CyberSource", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::CYBERSOURCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("dLocal", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::DLOCAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Dragonphoenix", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::DRAGONPHOENIX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EBANX", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::EBANX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ecoPayz", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ECOPAYZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EcorePay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ECOREPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Elavon", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ELAVON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EMS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::EMS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EPG", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::EPG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Euteller", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::EUTELLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("eZeeWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::EZEEWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ezyEFT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::EZYEFT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Fifth Third Bank", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FIFTH_THIRD_BANK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Finrax", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FINRAX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("First Data Buypass", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FIRST_DATA_BUYPASS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("First Data Nashville", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FIRST_DATA_NASHVILLE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("First Data North", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FIRST_DATA_NORTH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("First Data Omaha", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FIRST_DATA_OMAHA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FinTecSystems", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FINTECSYSTEMS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Flexepin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FLEXEPIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Forte", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FORTE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FundSend", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::FUNDSEND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gigadat", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::GIGADAT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Global East", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::GLOBAL_EAST;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gooney", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::GOONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gpaysafe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::GPAYSAFE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Heartland", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::HEARTLAND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HiPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::HIPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HSBC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::HSBC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iCanPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ICANPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ICEPAY", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ICEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iCheque", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ICHEQUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Ilixium", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ILIXIUM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Ingenico", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::INGENICO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INOVAPAY", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::INOVAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Intuit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::INTUIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Jeton", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::JETON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Khelocard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::KHELOCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Konnektive", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::KONNEKTIVE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("loonie", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::LOONIE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LPG", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::LPG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Masapay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::MASAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Merrick", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::MERRICK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Mission Valley Bank", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::MISSION_VALLEY_BANK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MiFinity", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::MIFINITY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Moneris", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::MONERIS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MuchBetter", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::MUCHBETTER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MyFatoorah", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::MYFATOORAH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NATWEST", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::NATWEST;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neosurf", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::NEOSURF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Netbanking", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::NETBANKING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neteller", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::NETELLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NinjaWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::NINJAWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NMI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::NMI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NuaPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::NUAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OchaPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::OCHAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Onlineueberweisen", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ONLINEUEBERWEISEN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OnRamp", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ONRAMP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Other", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::OTHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Panamerican", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PANAMERICAN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Panda Bank", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PANDA_BANK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paramount", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PARAMOUNT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ParamountEft", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PARAMOUNTEFT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ParamountInterac", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PARAMOUNTINTERAC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pay4fun", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAY4FUN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayClub", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYCLUB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymentAsia", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYMENTASIA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymenTechnologies", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYMENTECHNOLOGIES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymentsOS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYMENTSOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paymero", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYMERO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paynetics", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYNETICS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayPal", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYPAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayTabs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYTABS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayULatam", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYULATAM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payvision", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PAYVISION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Piastrix", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PIASTRIX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Peoples Trust Company", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PEOPLES_TRUST_COMPANY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PostFinance", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::POSTFINANCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Privatbank", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PRIVATBANK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Prosa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::PROSA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("QQPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::QQPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Rapyd", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::RAPYD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RBC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::RBC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RBS WorldPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::RBS_WORLDPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RealTime", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::REALTIME;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Rotessa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ROTESSA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SaltarPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SALTARPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SecureTrading", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SECURETRADING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SecurionPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SECURIONPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Skrill", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SKRILL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SmartInvoice", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SMARTINVOICE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SMSVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SMSVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Sofort", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SOFORT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SparkPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::SPARKPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("State Bank of Mauritius", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::STATE_BANK_OF_MAURITIUS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Stripe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::STRIPE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TBI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TBI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TestProcessor", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TESTPROCESSOR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ToditoCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TODITOCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Trustly", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TRUSTLY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TrustPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TRUSTPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TrustsPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TRUSTSPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TSYS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TSYS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TWINT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::TWINT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPayCard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::UPAYCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Vantiv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::VANTIV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VCreditos", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::VCREDITOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VoicePay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::VOICEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Wallet88", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::WALLET88;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WeChat Pay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::WECHAT_PAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Wells Fargo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::WELLS_FARGO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Wing Hang Bank", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::WING_HANG_BANK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Wirecard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::WIRECARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WorldPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::WORLDPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::XPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zimpler", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ZIMPLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zotapay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIAcquirerName::ZOTAPAY;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIAcquirerName::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIAcquirerName::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIAcquirerName::ADYEN:
            val = "Adyen";
            break;
        case eOAIAcquirerName::ALIPAY:
            val = "Alipay";
            break;
        case eOAIAcquirerName::AIB:
            val = "AIB";
            break;
        case eOAIAcquirerName::AIRPAY:
            val = "Airpay";
            break;
        case eOAIAcquirerName::APCOPAY:
            val = "ApcoPay";
            break;
        case eOAIAcquirerName::ASIAPAYMENTGATEWAY:
            val = "AsiaPaymentGateway";
            break;
        case eOAIAcquirerName::ASTROPAY_CARD:
            val = "AstroPay Card";
            break;
        case eOAIAcquirerName::IPAY_OPTIONS:
            val = "Ipay Options";
            break;
        case eOAIAcquirerName::B_S:
            val = "B+S";
            break;
        case eOAIAcquirerName::BAMBORA:
            val = "Bambora";
            break;
        case eOAIAcquirerName::BITPAY:
            val = "BitPay";
            break;
        case eOAIAcquirerName::BANK_OF_AMERICA:
            val = "Bank of America";
            break;
        case eOAIAcquirerName::BANK_OF_MOSCOW:
            val = "Bank of Moscow";
            break;
        case eOAIAcquirerName::BANK_OF_REBILLY:
            val = "Bank of Rebilly";
            break;
        case eOAIAcquirerName::BANK_ONE:
            val = "Bank One";
            break;
        case eOAIAcquirerName::BMO_HARRIS_BANK:
            val = "BMO Harris Bank";
            break;
        case eOAIAcquirerName::BORGUN:
            val = "Borgun";
            break;
        case eOAIAcquirerName::BRAINTREEPAYMENTS:
            val = "BraintreePayments";
            break;
        case eOAIAcquirerName::CARDKNOX:
            val = "Cardknox";
            break;
        case eOAIAcquirerName::CASHLIB:
            val = "CASHlib";
            break;
        case eOAIAcquirerName::CASHTOCODE:
            val = "CashToCode";
            break;
        case eOAIAcquirerName::CATALUNYA_CAIXA:
            val = "Catalunya Caixa";
            break;
        case eOAIAcquirerName::CCAVENUE:
            val = "CCAvenue";
            break;
        case eOAIAcquirerName::CHASE:
            val = "Chase";
            break;
        case eOAIAcquirerName::CHINAUNIONPAY:
            val = "ChinaUnionPay";
            break;
        case eOAIAcquirerName::CIM:
            val = "CIM";
            break;
        case eOAIAcquirerName::CIRCLE:
            val = "Circle";
            break;
        case eOAIAcquirerName::CITADEL:
            val = "Citadel";
            break;
        case eOAIAcquirerName::CLEARHAUS:
            val = "Clearhaus";
            break;
        case eOAIAcquirerName::CODVOUCHER:
            val = "CODVoucher";
            break;
        case eOAIAcquirerName::COINPAYMENTS:
            val = "CoinPayments";
            break;
        case eOAIAcquirerName::CONEKTA:
            val = "Conekta";
            break;
        case eOAIAcquirerName::COPPR:
            val = "Coppr";
            break;
        case eOAIAcquirerName::CREDORAX:
            val = "Credorax";
            break;
        case eOAIAcquirerName::CRYPTONATOR:
            val = "Cryptonator";
            break;
        case eOAIAcquirerName::CYBERSOURCE:
            val = "CyberSource";
            break;
        case eOAIAcquirerName::DLOCAL:
            val = "dLocal";
            break;
        case eOAIAcquirerName::DRAGONPHOENIX:
            val = "Dragonphoenix";
            break;
        case eOAIAcquirerName::EBANX:
            val = "EBANX";
            break;
        case eOAIAcquirerName::ECOPAYZ:
            val = "ecoPayz";
            break;
        case eOAIAcquirerName::ECOREPAY:
            val = "EcorePay";
            break;
        case eOAIAcquirerName::ELAVON:
            val = "Elavon";
            break;
        case eOAIAcquirerName::EMS:
            val = "EMS";
            break;
        case eOAIAcquirerName::EPG:
            val = "EPG";
            break;
        case eOAIAcquirerName::EUTELLER:
            val = "Euteller";
            break;
        case eOAIAcquirerName::EZEEWALLET:
            val = "eZeeWallet";
            break;
        case eOAIAcquirerName::EZYEFT:
            val = "ezyEFT";
            break;
        case eOAIAcquirerName::FIFTH_THIRD_BANK:
            val = "Fifth Third Bank";
            break;
        case eOAIAcquirerName::FINRAX:
            val = "Finrax";
            break;
        case eOAIAcquirerName::FIRST_DATA_BUYPASS:
            val = "First Data Buypass";
            break;
        case eOAIAcquirerName::FIRST_DATA_NASHVILLE:
            val = "First Data Nashville";
            break;
        case eOAIAcquirerName::FIRST_DATA_NORTH:
            val = "First Data North";
            break;
        case eOAIAcquirerName::FIRST_DATA_OMAHA:
            val = "First Data Omaha";
            break;
        case eOAIAcquirerName::FINTECSYSTEMS:
            val = "FinTecSystems";
            break;
        case eOAIAcquirerName::FLEXEPIN:
            val = "Flexepin";
            break;
        case eOAIAcquirerName::FORTE:
            val = "Forte";
            break;
        case eOAIAcquirerName::FUNDSEND:
            val = "FundSend";
            break;
        case eOAIAcquirerName::GIGADAT:
            val = "Gigadat";
            break;
        case eOAIAcquirerName::GLOBAL_EAST:
            val = "Global East";
            break;
        case eOAIAcquirerName::GOONEY:
            val = "Gooney";
            break;
        case eOAIAcquirerName::GPAYSAFE:
            val = "Gpaysafe";
            break;
        case eOAIAcquirerName::HEARTLAND:
            val = "Heartland";
            break;
        case eOAIAcquirerName::HIPAY:
            val = "HiPay";
            break;
        case eOAIAcquirerName::HSBC:
            val = "HSBC";
            break;
        case eOAIAcquirerName::ICANPAY:
            val = "iCanPay";
            break;
        case eOAIAcquirerName::ICEPAY:
            val = "ICEPAY";
            break;
        case eOAIAcquirerName::ICHEQUE:
            val = "iCheque";
            break;
        case eOAIAcquirerName::ILIXIUM:
            val = "Ilixium";
            break;
        case eOAIAcquirerName::INGENICO:
            val = "Ingenico";
            break;
        case eOAIAcquirerName::INOVAPAY:
            val = "INOVAPAY";
            break;
        case eOAIAcquirerName::INTUIT:
            val = "Intuit";
            break;
        case eOAIAcquirerName::JETON:
            val = "Jeton";
            break;
        case eOAIAcquirerName::KHELOCARD:
            val = "Khelocard";
            break;
        case eOAIAcquirerName::KONNEKTIVE:
            val = "Konnektive";
            break;
        case eOAIAcquirerName::LOONIE:
            val = "loonie";
            break;
        case eOAIAcquirerName::LPG:
            val = "LPG";
            break;
        case eOAIAcquirerName::MASAPAY:
            val = "Masapay";
            break;
        case eOAIAcquirerName::MERRICK:
            val = "Merrick";
            break;
        case eOAIAcquirerName::MISSION_VALLEY_BANK:
            val = "Mission Valley Bank";
            break;
        case eOAIAcquirerName::MIFINITY:
            val = "MiFinity";
            break;
        case eOAIAcquirerName::MONERIS:
            val = "Moneris";
            break;
        case eOAIAcquirerName::MUCHBETTER:
            val = "MuchBetter";
            break;
        case eOAIAcquirerName::MYFATOORAH:
            val = "MyFatoorah";
            break;
        case eOAIAcquirerName::NATWEST:
            val = "NATWEST";
            break;
        case eOAIAcquirerName::NEOSURF:
            val = "Neosurf";
            break;
        case eOAIAcquirerName::NETBANKING:
            val = "Netbanking";
            break;
        case eOAIAcquirerName::NETELLER:
            val = "Neteller";
            break;
        case eOAIAcquirerName::NINJAWALLET:
            val = "NinjaWallet";
            break;
        case eOAIAcquirerName::NMI:
            val = "NMI";
            break;
        case eOAIAcquirerName::NUAPAY:
            val = "NuaPay";
            break;
        case eOAIAcquirerName::OCHAPAY:
            val = "OchaPay";
            break;
        case eOAIAcquirerName::ONLINEUEBERWEISEN:
            val = "Onlineueberweisen";
            break;
        case eOAIAcquirerName::ONRAMP:
            val = "OnRamp";
            break;
        case eOAIAcquirerName::OTHER:
            val = "Other";
            break;
        case eOAIAcquirerName::PANAMERICAN:
            val = "Panamerican";
            break;
        case eOAIAcquirerName::PANDA_BANK:
            val = "Panda Bank";
            break;
        case eOAIAcquirerName::PARAMOUNT:
            val = "Paramount";
            break;
        case eOAIAcquirerName::PARAMOUNTEFT:
            val = "ParamountEft";
            break;
        case eOAIAcquirerName::PARAMOUNTINTERAC:
            val = "ParamountInterac";
            break;
        case eOAIAcquirerName::PAY4FUN:
            val = "Pay4fun";
            break;
        case eOAIAcquirerName::PAYCASH:
            val = "PayCash";
            break;
        case eOAIAcquirerName::PAYCLUB:
            val = "PayClub";
            break;
        case eOAIAcquirerName::PAYMENTASIA:
            val = "PaymentAsia";
            break;
        case eOAIAcquirerName::PAYMENTECHNOLOGIES:
            val = "PaymenTechnologies";
            break;
        case eOAIAcquirerName::PAYMENTSOS:
            val = "PaymentsOS";
            break;
        case eOAIAcquirerName::PAYMERO:
            val = "Paymero";
            break;
        case eOAIAcquirerName::PAYNETICS:
            val = "Paynetics";
            break;
        case eOAIAcquirerName::PAYPAL:
            val = "PayPal";
            break;
        case eOAIAcquirerName::PAYR:
            val = "Payr";
            break;
        case eOAIAcquirerName::PAYTABS:
            val = "PayTabs";
            break;
        case eOAIAcquirerName::PAYULATAM:
            val = "PayULatam";
            break;
        case eOAIAcquirerName::PAYVISION:
            val = "Payvision";
            break;
        case eOAIAcquirerName::PIASTRIX:
            val = "Piastrix";
            break;
        case eOAIAcquirerName::PEOPLES_TRUST_COMPANY:
            val = "Peoples Trust Company";
            break;
        case eOAIAcquirerName::POSTFINANCE:
            val = "PostFinance";
            break;
        case eOAIAcquirerName::PRIVATBANK:
            val = "Privatbank";
            break;
        case eOAIAcquirerName::PROSA:
            val = "Prosa";
            break;
        case eOAIAcquirerName::QQPAY:
            val = "QQPay";
            break;
        case eOAIAcquirerName::RAPYD:
            val = "Rapyd";
            break;
        case eOAIAcquirerName::RBC:
            val = "RBC";
            break;
        case eOAIAcquirerName::RBS_WORLDPAY:
            val = "RBS WorldPay";
            break;
        case eOAIAcquirerName::REALTIME:
            val = "RealTime";
            break;
        case eOAIAcquirerName::ROTESSA:
            val = "Rotessa";
            break;
        case eOAIAcquirerName::SALTARPAY:
            val = "SaltarPay";
            break;
        case eOAIAcquirerName::SECURETRADING:
            val = "SecureTrading";
            break;
        case eOAIAcquirerName::SECURIONPAY:
            val = "SecurionPay";
            break;
        case eOAIAcquirerName::SKRILL:
            val = "Skrill";
            break;
        case eOAIAcquirerName::SMARTINVOICE:
            val = "SmartInvoice";
            break;
        case eOAIAcquirerName::SMSVOUCHER:
            val = "SMSVoucher";
            break;
        case eOAIAcquirerName::SOFORT:
            val = "Sofort";
            break;
        case eOAIAcquirerName::SPARKPAY:
            val = "SparkPay";
            break;
        case eOAIAcquirerName::STATE_BANK_OF_MAURITIUS:
            val = "State Bank of Mauritius";
            break;
        case eOAIAcquirerName::STRIPE:
            val = "Stripe";
            break;
        case eOAIAcquirerName::TBI:
            val = "TBI";
            break;
        case eOAIAcquirerName::TESTPROCESSOR:
            val = "TestProcessor";
            break;
        case eOAIAcquirerName::TODITOCASH:
            val = "ToditoCash";
            break;
        case eOAIAcquirerName::TRUSTLY:
            val = "Trustly";
            break;
        case eOAIAcquirerName::TRUSTPAY:
            val = "TrustPay";
            break;
        case eOAIAcquirerName::TRUSTSPAY:
            val = "TrustsPay";
            break;
        case eOAIAcquirerName::TSYS:
            val = "TSYS";
            break;
        case eOAIAcquirerName::TWINT:
            val = "TWINT";
            break;
        case eOAIAcquirerName::UPAYCARD:
            val = "UPayCard";
            break;
        case eOAIAcquirerName::VANTIV:
            val = "Vantiv";
            break;
        case eOAIAcquirerName::VCREDITOS:
            val = "VCreditos";
            break;
        case eOAIAcquirerName::VOICEPAY:
            val = "VoicePay";
            break;
        case eOAIAcquirerName::WALLET88:
            val = "Wallet88";
            break;
        case eOAIAcquirerName::WECHAT_PAY:
            val = "WeChat Pay";
            break;
        case eOAIAcquirerName::WELLS_FARGO:
            val = "Wells Fargo";
            break;
        case eOAIAcquirerName::WING_HANG_BANK:
            val = "Wing Hang Bank";
            break;
        case eOAIAcquirerName::WIRECARD:
            val = "Wirecard";
            break;
        case eOAIAcquirerName::WORLDPAY:
            val = "WorldPay";
            break;
        case eOAIAcquirerName::XPAY:
            val = "XPay";
            break;
        case eOAIAcquirerName::ZIMPLER:
            val = "Zimpler";
            break;
        case eOAIAcquirerName::ZOTAPAY:
            val = "Zotapay";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIAcquirerName::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIAcquirerName::eOAIAcquirerName OAIAcquirerName::getValue() const {
    return m_value;
}

void OAIAcquirerName::setValue(const OAIAcquirerName::eOAIAcquirerName& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIAcquirerName::isSet() const {
    
    return m_value_isSet;
}

bool OAIAcquirerName::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
