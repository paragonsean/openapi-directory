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

#include "OAIDirecta24Banks.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDirecta24Banks::OAIDirecta24Banks(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDirecta24Banks::OAIDirecta24Banks() {
    this->initializeModel();
}

OAIDirecta24Banks::~OAIDirecta24Banks() {}

void OAIDirecta24Banks::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIDirecta24Banks::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIDirecta24Banks::fromJson(QString jsonString) {
    
    if ( jsonString.compare("AA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::AA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AL", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::AL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AZ", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::AZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("B", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::B;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BB", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BE", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BL", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BM", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BN", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BP", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BQ", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BQ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BU", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BV", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BW", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BX", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BZ", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::BZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::CA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CE", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::CE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::CI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CU", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::CU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EF", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::EF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EN", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::EN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EY", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::EY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::FA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FB", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::FB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::FC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::GC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GG", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::GG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::HC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("I", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::I;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("IA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::IA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("IB", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::IB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("JM", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::JM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::LC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LE", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::LE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LL", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::LL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::MC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MD", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::MD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MP", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::MP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MT", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::MT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NB", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::NB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OM", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::OM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OX", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::OX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::PC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PH", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::PH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PL", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::PL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SB", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::SB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::SC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SE", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::SE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SF", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::SF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SM", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::SM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SS", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::SS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ST", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::ST;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SU", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::SU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TC", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::TC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TG", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::TG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TY", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::TY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UB", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::UB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::UI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UL", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::UL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("US", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::US;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VD", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::VD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VI", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::VI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WA", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::WA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WP", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::WP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WU", Qt::CaseInsensitive) == 0) {
        m_value = eOAIDirecta24Banks::WU;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIDirecta24Banks::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIDirecta24Banks::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIDirecta24Banks::AA:
            val = "AA";
            break;
        case eOAIDirecta24Banks::AL:
            val = "AL";
            break;
        case eOAIDirecta24Banks::AZ:
            val = "AZ";
            break;
        case eOAIDirecta24Banks::B:
            val = "B";
            break;
        case eOAIDirecta24Banks::BB:
            val = "BB";
            break;
        case eOAIDirecta24Banks::BC:
            val = "BC";
            break;
        case eOAIDirecta24Banks::BE:
            val = "BE";
            break;
        case eOAIDirecta24Banks::BL:
            val = "BL";
            break;
        case eOAIDirecta24Banks::BM:
            val = "BM";
            break;
        case eOAIDirecta24Banks::BN:
            val = "BN";
            break;
        case eOAIDirecta24Banks::BP:
            val = "BP";
            break;
        case eOAIDirecta24Banks::BQ:
            val = "BQ";
            break;
        case eOAIDirecta24Banks::BU:
            val = "BU";
            break;
        case eOAIDirecta24Banks::BV:
            val = "BV";
            break;
        case eOAIDirecta24Banks::BW:
            val = "BW";
            break;
        case eOAIDirecta24Banks::BX:
            val = "BX";
            break;
        case eOAIDirecta24Banks::BZ:
            val = "BZ";
            break;
        case eOAIDirecta24Banks::CA:
            val = "CA";
            break;
        case eOAIDirecta24Banks::CE:
            val = "CE";
            break;
        case eOAIDirecta24Banks::CI:
            val = "CI";
            break;
        case eOAIDirecta24Banks::CU:
            val = "CU";
            break;
        case eOAIDirecta24Banks::EF:
            val = "EF";
            break;
        case eOAIDirecta24Banks::EN:
            val = "EN";
            break;
        case eOAIDirecta24Banks::EY:
            val = "EY";
            break;
        case eOAIDirecta24Banks::FA:
            val = "FA";
            break;
        case eOAIDirecta24Banks::FB:
            val = "FB";
            break;
        case eOAIDirecta24Banks::FC:
            val = "FC";
            break;
        case eOAIDirecta24Banks::GC:
            val = "GC";
            break;
        case eOAIDirecta24Banks::GG:
            val = "GG";
            break;
        case eOAIDirecta24Banks::HC:
            val = "HC";
            break;
        case eOAIDirecta24Banks::I:
            val = "I";
            break;
        case eOAIDirecta24Banks::IA:
            val = "IA";
            break;
        case eOAIDirecta24Banks::IB:
            val = "IB";
            break;
        case eOAIDirecta24Banks::JM:
            val = "JM";
            break;
        case eOAIDirecta24Banks::LC:
            val = "LC";
            break;
        case eOAIDirecta24Banks::LE:
            val = "LE";
            break;
        case eOAIDirecta24Banks::LL:
            val = "LL";
            break;
        case eOAIDirecta24Banks::MC:
            val = "MC";
            break;
        case eOAIDirecta24Banks::MD:
            val = "MD";
            break;
        case eOAIDirecta24Banks::MP:
            val = "MP";
            break;
        case eOAIDirecta24Banks::MT:
            val = "MT";
            break;
        case eOAIDirecta24Banks::NB:
            val = "NB";
            break;
        case eOAIDirecta24Banks::OM:
            val = "OM";
            break;
        case eOAIDirecta24Banks::OX:
            val = "OX";
            break;
        case eOAIDirecta24Banks::PC:
            val = "PC";
            break;
        case eOAIDirecta24Banks::PH:
            val = "PH";
            break;
        case eOAIDirecta24Banks::PL:
            val = "PL";
            break;
        case eOAIDirecta24Banks::SB:
            val = "SB";
            break;
        case eOAIDirecta24Banks::SC:
            val = "SC";
            break;
        case eOAIDirecta24Banks::SE:
            val = "SE";
            break;
        case eOAIDirecta24Banks::SF:
            val = "SF";
            break;
        case eOAIDirecta24Banks::SM:
            val = "SM";
            break;
        case eOAIDirecta24Banks::SS:
            val = "SS";
            break;
        case eOAIDirecta24Banks::ST:
            val = "ST";
            break;
        case eOAIDirecta24Banks::SU:
            val = "SU";
            break;
        case eOAIDirecta24Banks::TC:
            val = "TC";
            break;
        case eOAIDirecta24Banks::TG:
            val = "TG";
            break;
        case eOAIDirecta24Banks::TY:
            val = "TY";
            break;
        case eOAIDirecta24Banks::UB:
            val = "UB";
            break;
        case eOAIDirecta24Banks::UI:
            val = "UI";
            break;
        case eOAIDirecta24Banks::UL:
            val = "UL";
            break;
        case eOAIDirecta24Banks::US:
            val = "US";
            break;
        case eOAIDirecta24Banks::VD:
            val = "VD";
            break;
        case eOAIDirecta24Banks::VI:
            val = "VI";
            break;
        case eOAIDirecta24Banks::WA:
            val = "WA";
            break;
        case eOAIDirecta24Banks::WP:
            val = "WP";
            break;
        case eOAIDirecta24Banks::WU:
            val = "WU";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIDirecta24Banks::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIDirecta24Banks::eOAIDirecta24Banks OAIDirecta24Banks::getValue() const {
    return m_value;
}

void OAIDirecta24Banks::setValue(const OAIDirecta24Banks::eOAIDirecta24Banks& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIDirecta24Banks::isSet() const {
    
    return m_value_isSet;
}

bool OAIDirecta24Banks::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
