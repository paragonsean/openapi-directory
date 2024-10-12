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

#include "OAIGatewayName.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGatewayName::OAIGatewayName(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGatewayName::OAIGatewayName() {
    this->initializeModel();
}

OAIGatewayName::~OAIGatewayName() {}

void OAIGatewayName::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIGatewayName::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIGatewayName::fromJson(QString jsonString) {
    
    if ( jsonString.compare("A1Gateway", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::A1GATEWAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Adyen", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ADYEN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Airpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::AIRPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AmexVPC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::AMEXVPC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ApcoPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::APCOPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AsiaPaymentGateway", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ASIAPAYMENTGATEWAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AstroPayCard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ASTROPAYCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AuthorizeNet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::AUTHORIZENET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Bambora", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::BAMBORA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BitPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::BITPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BlueSnap", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::BLUESNAP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BraintreePayments", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::BRAINTREEPAYMENTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cardknox", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CARDKNOX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cashflows", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CASHFLOWS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CASHlib", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CASHLIB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CashToCode", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CASHTOCODE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CauriPayment", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CAURIPAYMENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cayan", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CAYAN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CCAvenue", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CCAVENUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Chase", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CHASE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Circle", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CIRCLE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Citadel", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CITADEL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Clearhaus", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CLEARHAUS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CODVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CODVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CoinPayments", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::COINPAYMENTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Conekta", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CONEKTA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Coppr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::COPPR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Credorax", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CREDORAX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Cryptonator", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CRYPTONATOR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CyberSource", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::CYBERSOURCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DataCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::DATACASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Dengi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::DENGI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Dragonphoenix", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::DRAGONPHOENIX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Directa24", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::DIRECTA24;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("dLocal", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::DLOCAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EBANX", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EBANX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ecoPayz", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ECOPAYZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EcorePay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ECOREPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Elavon", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ELAVON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Euteller", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EUTELLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("eMerchantPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EMERCHANTPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EMS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EMS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EPG", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EPG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EPro", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EPRO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("eZeeWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EZEEWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ezyEFT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::EZYEFT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Finrax", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::FINRAX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Flexepin", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::FLEXEPIN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FinTecSystems", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::FINTECSYSTEMS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FundSend", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::FUNDSEND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Forte", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::FORTE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GET", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::GET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gigadat", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::GIGADAT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GlobalOnePay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::GLOBALONEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gooney", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::GOONEY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Gpaysafe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::GPAYSAFE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Greenbox", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::GREENBOX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HiPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::HIPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iCanPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ICANPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ICEPAY", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ICEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iCheque", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ICHEQUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iDebit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::IDEBIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Ilixium", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ILIXIUM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Ingenico", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::INGENICO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INOVAPAY", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::INOVAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Inovio", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::INOVIO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Intuit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::INTUIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("InstaDebit", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::INSTADEBIT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("IpayOptions", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::IPAYOPTIONS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("JetPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::JETPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Jeton", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::JETON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Khelocard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::KHELOCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Konnektive", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::KONNEKTIVE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("loonie", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::LOONIE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LPG", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::LPG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MiFinity", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::MIFINITY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Moneris", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::MONERIS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MtaPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::MTAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MuchBetter", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::MUCHBETTER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MyFatoorah", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::MYFATOORAH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neosurf", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::NEOSURF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Netbanking", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::NETBANKING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Neteller", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::NETELLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NGenius", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::NGENIUS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NinjaWallet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::NINJAWALLET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NMI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::NMI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NuaPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::NUAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OchaPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::OCHAPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Onlineueberweisen", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ONLINEUEBERWEISEN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OnRamp", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ONRAMP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pagsmile", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAGSMILE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Panamerican", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PANAMERICAN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ParamountEft", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PARAMOUNTEFT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ParamountInterac", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PARAMOUNTINTERAC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PandaGateway", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PANDAGATEWAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Pay4Fun", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAY4FUN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayClub", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYCLUB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payeezy", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYEEZY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payflow", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYFLOW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymentAsia", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYMENTASIA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymenTechnologies", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYMENTECHNOLOGIES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PaymentsOS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYMENTSOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paymero", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYMERO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayPal", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYPAL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paysafe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYSAFE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Paysafecash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYSAFECASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayTabs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYTABS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PayULatam", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYULATAM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Payvision", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PAYVISION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Piastrix", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PIASTRIX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Plugnpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PLUGNPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PostFinance", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::POSTFINANCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Prosa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::PROSA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Rapyd", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::RAPYD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Realex", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::REALEX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Realtime", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::REALTIME;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Redsys", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::REDSYS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Rotessa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ROTESSA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RPN", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::RPN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SaltarPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SALTARPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Sagepay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SAGEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SeamlessChex", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SEAMLESSCHEX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SecureTrading", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SECURETRADING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SecurionPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SECURIONPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Skrill", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SKRILL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SmartInvoice", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SMARTINVOICE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SMSVoucher", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SMSVOUCHER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Sofort", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SOFORT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SparkPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::SPARKPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("StaticGateway", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::STATICGATEWAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Stripe", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::STRIPE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TestProcessor", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::TESTPROCESSOR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ToditoCash", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::TODITOCASH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TrustPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::TRUSTPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TrustsPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::TRUSTSPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Trustly", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::TRUSTLY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TWINT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::TWINT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UPayCard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::UPAYCARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("USAePay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::USAEPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VantivLitle", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::VANTIVLITLE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("vegaaH", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::VEGAAH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VCreditos", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::VCREDITOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Wallet88", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::WALLET88;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Walpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::WALPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Wirecard", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::WIRECARD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WorldlineAtosFrankfurt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::WORLDLINEATOSFRANKFURT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Worldpay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::WORLDPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::XPAY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zimpler", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ZIMPLER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("Zotapay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGatewayName::ZOTAPAY;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIGatewayName::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIGatewayName::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIGatewayName::A1GATEWAY:
            val = "A1Gateway";
            break;
        case eOAIGatewayName::ADYEN:
            val = "Adyen";
            break;
        case eOAIGatewayName::AIRPAY:
            val = "Airpay";
            break;
        case eOAIGatewayName::AMEXVPC:
            val = "AmexVPC";
            break;
        case eOAIGatewayName::APCOPAY:
            val = "ApcoPay";
            break;
        case eOAIGatewayName::ASIAPAYMENTGATEWAY:
            val = "AsiaPaymentGateway";
            break;
        case eOAIGatewayName::ASTROPAYCARD:
            val = "AstroPayCard";
            break;
        case eOAIGatewayName::AUTHORIZENET:
            val = "AuthorizeNet";
            break;
        case eOAIGatewayName::BAMBORA:
            val = "Bambora";
            break;
        case eOAIGatewayName::BITPAY:
            val = "BitPay";
            break;
        case eOAIGatewayName::BLUESNAP:
            val = "BlueSnap";
            break;
        case eOAIGatewayName::BRAINTREEPAYMENTS:
            val = "BraintreePayments";
            break;
        case eOAIGatewayName::CARDKNOX:
            val = "Cardknox";
            break;
        case eOAIGatewayName::CASHFLOWS:
            val = "Cashflows";
            break;
        case eOAIGatewayName::CASHLIB:
            val = "CASHlib";
            break;
        case eOAIGatewayName::CASHTOCODE:
            val = "CashToCode";
            break;
        case eOAIGatewayName::CAURIPAYMENT:
            val = "CauriPayment";
            break;
        case eOAIGatewayName::CAYAN:
            val = "Cayan";
            break;
        case eOAIGatewayName::CCAVENUE:
            val = "CCAvenue";
            break;
        case eOAIGatewayName::CHASE:
            val = "Chase";
            break;
        case eOAIGatewayName::CIRCLE:
            val = "Circle";
            break;
        case eOAIGatewayName::CITADEL:
            val = "Citadel";
            break;
        case eOAIGatewayName::CLEARHAUS:
            val = "Clearhaus";
            break;
        case eOAIGatewayName::CODVOUCHER:
            val = "CODVoucher";
            break;
        case eOAIGatewayName::COINPAYMENTS:
            val = "CoinPayments";
            break;
        case eOAIGatewayName::CONEKTA:
            val = "Conekta";
            break;
        case eOAIGatewayName::COPPR:
            val = "Coppr";
            break;
        case eOAIGatewayName::CREDORAX:
            val = "Credorax";
            break;
        case eOAIGatewayName::CRYPTONATOR:
            val = "Cryptonator";
            break;
        case eOAIGatewayName::CYBERSOURCE:
            val = "CyberSource";
            break;
        case eOAIGatewayName::DATACASH:
            val = "DataCash";
            break;
        case eOAIGatewayName::DENGI:
            val = "Dengi";
            break;
        case eOAIGatewayName::DRAGONPHOENIX:
            val = "Dragonphoenix";
            break;
        case eOAIGatewayName::DIRECTA24:
            val = "Directa24";
            break;
        case eOAIGatewayName::DLOCAL:
            val = "dLocal";
            break;
        case eOAIGatewayName::EBANX:
            val = "EBANX";
            break;
        case eOAIGatewayName::ECOPAYZ:
            val = "ecoPayz";
            break;
        case eOAIGatewayName::ECOREPAY:
            val = "EcorePay";
            break;
        case eOAIGatewayName::ELAVON:
            val = "Elavon";
            break;
        case eOAIGatewayName::EUTELLER:
            val = "Euteller";
            break;
        case eOAIGatewayName::EMERCHANTPAY:
            val = "eMerchantPay";
            break;
        case eOAIGatewayName::EMS:
            val = "EMS";
            break;
        case eOAIGatewayName::EPG:
            val = "EPG";
            break;
        case eOAIGatewayName::EPRO:
            val = "EPro";
            break;
        case eOAIGatewayName::EZEEWALLET:
            val = "eZeeWallet";
            break;
        case eOAIGatewayName::EZYEFT:
            val = "ezyEFT";
            break;
        case eOAIGatewayName::FINRAX:
            val = "Finrax";
            break;
        case eOAIGatewayName::FLEXEPIN:
            val = "Flexepin";
            break;
        case eOAIGatewayName::FINTECSYSTEMS:
            val = "FinTecSystems";
            break;
        case eOAIGatewayName::FUNDSEND:
            val = "FundSend";
            break;
        case eOAIGatewayName::FORTE:
            val = "Forte";
            break;
        case eOAIGatewayName::GET:
            val = "GET";
            break;
        case eOAIGatewayName::GIGADAT:
            val = "Gigadat";
            break;
        case eOAIGatewayName::GLOBALONEPAY:
            val = "GlobalOnePay";
            break;
        case eOAIGatewayName::GOONEY:
            val = "Gooney";
            break;
        case eOAIGatewayName::GPAYSAFE:
            val = "Gpaysafe";
            break;
        case eOAIGatewayName::GREENBOX:
            val = "Greenbox";
            break;
        case eOAIGatewayName::HIPAY:
            val = "HiPay";
            break;
        case eOAIGatewayName::ICANPAY:
            val = "iCanPay";
            break;
        case eOAIGatewayName::ICEPAY:
            val = "ICEPAY";
            break;
        case eOAIGatewayName::ICHEQUE:
            val = "iCheque";
            break;
        case eOAIGatewayName::IDEBIT:
            val = "iDebit";
            break;
        case eOAIGatewayName::ILIXIUM:
            val = "Ilixium";
            break;
        case eOAIGatewayName::INGENICO:
            val = "Ingenico";
            break;
        case eOAIGatewayName::INOVAPAY:
            val = "INOVAPAY";
            break;
        case eOAIGatewayName::INOVIO:
            val = "Inovio";
            break;
        case eOAIGatewayName::INTUIT:
            val = "Intuit";
            break;
        case eOAIGatewayName::INSTADEBIT:
            val = "InstaDebit";
            break;
        case eOAIGatewayName::IPAYOPTIONS:
            val = "IpayOptions";
            break;
        case eOAIGatewayName::JETPAY:
            val = "JetPay";
            break;
        case eOAIGatewayName::JETON:
            val = "Jeton";
            break;
        case eOAIGatewayName::KHELOCARD:
            val = "Khelocard";
            break;
        case eOAIGatewayName::KONNEKTIVE:
            val = "Konnektive";
            break;
        case eOAIGatewayName::LOONIE:
            val = "loonie";
            break;
        case eOAIGatewayName::LPG:
            val = "LPG";
            break;
        case eOAIGatewayName::MIFINITY:
            val = "MiFinity";
            break;
        case eOAIGatewayName::MONERIS:
            val = "Moneris";
            break;
        case eOAIGatewayName::MTAPAY:
            val = "MtaPay";
            break;
        case eOAIGatewayName::MUCHBETTER:
            val = "MuchBetter";
            break;
        case eOAIGatewayName::MYFATOORAH:
            val = "MyFatoorah";
            break;
        case eOAIGatewayName::NEOSURF:
            val = "Neosurf";
            break;
        case eOAIGatewayName::NETBANKING:
            val = "Netbanking";
            break;
        case eOAIGatewayName::NETELLER:
            val = "Neteller";
            break;
        case eOAIGatewayName::NGENIUS:
            val = "NGenius";
            break;
        case eOAIGatewayName::NINJAWALLET:
            val = "NinjaWallet";
            break;
        case eOAIGatewayName::NMI:
            val = "NMI";
            break;
        case eOAIGatewayName::NUAPAY:
            val = "NuaPay";
            break;
        case eOAIGatewayName::OCHAPAY:
            val = "OchaPay";
            break;
        case eOAIGatewayName::ONLINEUEBERWEISEN:
            val = "Onlineueberweisen";
            break;
        case eOAIGatewayName::ONRAMP:
            val = "OnRamp";
            break;
        case eOAIGatewayName::PAGSMILE:
            val = "Pagsmile";
            break;
        case eOAIGatewayName::PANAMERICAN:
            val = "Panamerican";
            break;
        case eOAIGatewayName::PARAMOUNTEFT:
            val = "ParamountEft";
            break;
        case eOAIGatewayName::PARAMOUNTINTERAC:
            val = "ParamountInterac";
            break;
        case eOAIGatewayName::PANDAGATEWAY:
            val = "PandaGateway";
            break;
        case eOAIGatewayName::PAY4FUN:
            val = "Pay4Fun";
            break;
        case eOAIGatewayName::PAYCASH:
            val = "PayCash";
            break;
        case eOAIGatewayName::PAYCLUB:
            val = "PayClub";
            break;
        case eOAIGatewayName::PAYEEZY:
            val = "Payeezy";
            break;
        case eOAIGatewayName::PAYFLOW:
            val = "Payflow";
            break;
        case eOAIGatewayName::PAYMENTASIA:
            val = "PaymentAsia";
            break;
        case eOAIGatewayName::PAYMENTECHNOLOGIES:
            val = "PaymenTechnologies";
            break;
        case eOAIGatewayName::PAYMENTSOS:
            val = "PaymentsOS";
            break;
        case eOAIGatewayName::PAYMERO:
            val = "Paymero";
            break;
        case eOAIGatewayName::PAYPAL:
            val = "PayPal";
            break;
        case eOAIGatewayName::PAYR:
            val = "Payr";
            break;
        case eOAIGatewayName::PAYSAFE:
            val = "Paysafe";
            break;
        case eOAIGatewayName::PAYSAFECASH:
            val = "Paysafecash";
            break;
        case eOAIGatewayName::PAYTABS:
            val = "PayTabs";
            break;
        case eOAIGatewayName::PAYULATAM:
            val = "PayULatam";
            break;
        case eOAIGatewayName::PAYVISION:
            val = "Payvision";
            break;
        case eOAIGatewayName::PIASTRIX:
            val = "Piastrix";
            break;
        case eOAIGatewayName::PLUGNPAY:
            val = "Plugnpay";
            break;
        case eOAIGatewayName::POSTFINANCE:
            val = "PostFinance";
            break;
        case eOAIGatewayName::PROSA:
            val = "Prosa";
            break;
        case eOAIGatewayName::RAPYD:
            val = "Rapyd";
            break;
        case eOAIGatewayName::REALEX:
            val = "Realex";
            break;
        case eOAIGatewayName::REALTIME:
            val = "Realtime";
            break;
        case eOAIGatewayName::REDSYS:
            val = "Redsys";
            break;
        case eOAIGatewayName::ROTESSA:
            val = "Rotessa";
            break;
        case eOAIGatewayName::RPN:
            val = "RPN";
            break;
        case eOAIGatewayName::SALTARPAY:
            val = "SaltarPay";
            break;
        case eOAIGatewayName::SAGEPAY:
            val = "Sagepay";
            break;
        case eOAIGatewayName::SEAMLESSCHEX:
            val = "SeamlessChex";
            break;
        case eOAIGatewayName::SECURETRADING:
            val = "SecureTrading";
            break;
        case eOAIGatewayName::SECURIONPAY:
            val = "SecurionPay";
            break;
        case eOAIGatewayName::SKRILL:
            val = "Skrill";
            break;
        case eOAIGatewayName::SMARTINVOICE:
            val = "SmartInvoice";
            break;
        case eOAIGatewayName::SMSVOUCHER:
            val = "SMSVoucher";
            break;
        case eOAIGatewayName::SOFORT:
            val = "Sofort";
            break;
        case eOAIGatewayName::SPARKPAY:
            val = "SparkPay";
            break;
        case eOAIGatewayName::STATICGATEWAY:
            val = "StaticGateway";
            break;
        case eOAIGatewayName::STRIPE:
            val = "Stripe";
            break;
        case eOAIGatewayName::TESTPROCESSOR:
            val = "TestProcessor";
            break;
        case eOAIGatewayName::TODITOCASH:
            val = "ToditoCash";
            break;
        case eOAIGatewayName::TRUSTPAY:
            val = "TrustPay";
            break;
        case eOAIGatewayName::TRUSTSPAY:
            val = "TrustsPay";
            break;
        case eOAIGatewayName::TRUSTLY:
            val = "Trustly";
            break;
        case eOAIGatewayName::TWINT:
            val = "TWINT";
            break;
        case eOAIGatewayName::UPAYCARD:
            val = "UPayCard";
            break;
        case eOAIGatewayName::USAEPAY:
            val = "USAePay";
            break;
        case eOAIGatewayName::VANTIVLITLE:
            val = "VantivLitle";
            break;
        case eOAIGatewayName::VEGAAH:
            val = "vegaaH";
            break;
        case eOAIGatewayName::VCREDITOS:
            val = "VCreditos";
            break;
        case eOAIGatewayName::WALLET88:
            val = "Wallet88";
            break;
        case eOAIGatewayName::WALPAY:
            val = "Walpay";
            break;
        case eOAIGatewayName::WIRECARD:
            val = "Wirecard";
            break;
        case eOAIGatewayName::WORLDLINEATOSFRANKFURT:
            val = "WorldlineAtosFrankfurt";
            break;
        case eOAIGatewayName::WORLDPAY:
            val = "Worldpay";
            break;
        case eOAIGatewayName::XPAY:
            val = "XPay";
            break;
        case eOAIGatewayName::ZIMPLER:
            val = "Zimpler";
            break;
        case eOAIGatewayName::ZOTAPAY:
            val = "Zotapay";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIGatewayName::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIGatewayName::eOAIGatewayName OAIGatewayName::getValue() const {
    return m_value;
}

void OAIGatewayName::setValue(const OAIGatewayName::eOAIGatewayName& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIGatewayName::isSet() const {
    
    return m_value_isSet;
}

bool OAIGatewayName::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
