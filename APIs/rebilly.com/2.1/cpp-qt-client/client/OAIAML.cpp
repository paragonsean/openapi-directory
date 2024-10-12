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

#include "OAIAML.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAML::OAIAML(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAML::OAIAML() {
    this->initializeModel();
}

OAIAML::~OAIAML() {}

void OAIAML::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_address_isSet = false;
    m_address_isValid = false;

    m_aliases_isSet = false;
    m_aliases_isValid = false;

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_confidence_isSet = false;
    m_confidence_isValid = false;

    m_dob_isSet = false;
    m_dob_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_legal_basis_isSet = false;
    m_legal_basis_isValid = false;

    m_nationality_isSet = false;
    m_nationality_isValid = false;

    m_passport_isSet = false;
    m_passport_isValid = false;

    m_regime_isSet = false;
    m_regime_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_source_type_isSet = false;
    m_source_type_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAML::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAML::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_aliases_isValid = ::OpenAPI::fromJsonValue(m_aliases, json[QString("aliases")]);
    m_aliases_isSet = !json[QString("aliases")].isNull() && m_aliases_isValid;

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_confidence_isValid = ::OpenAPI::fromJsonValue(m_confidence, json[QString("confidence")]);
    m_confidence_isSet = !json[QString("confidence")].isNull() && m_confidence_isValid;

    m_dob_isValid = ::OpenAPI::fromJsonValue(m_dob, json[QString("dob")]);
    m_dob_isSet = !json[QString("dob")].isNull() && m_dob_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_legal_basis_isValid = ::OpenAPI::fromJsonValue(m_legal_basis, json[QString("legalBasis")]);
    m_legal_basis_isSet = !json[QString("legalBasis")].isNull() && m_legal_basis_isValid;

    m_nationality_isValid = ::OpenAPI::fromJsonValue(m_nationality, json[QString("nationality")]);
    m_nationality_isSet = !json[QString("nationality")].isNull() && m_nationality_isValid;

    m_passport_isValid = ::OpenAPI::fromJsonValue(m_passport, json[QString("passport")]);
    m_passport_isSet = !json[QString("passport")].isNull() && m_passport_isValid;

    m_regime_isValid = ::OpenAPI::fromJsonValue(m_regime, json[QString("regime")]);
    m_regime_isSet = !json[QString("regime")].isNull() && m_regime_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_source_type_isValid = ::OpenAPI::fromJsonValue(m_source_type, json[QString("sourceType")]);
    m_source_type_isSet = !json[QString("sourceType")].isNull() && m_source_type_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAML::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAML::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_address.size() > 0) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_aliases.size() > 0) {
        obj.insert(QString("aliases"), ::OpenAPI::toJsonValue(m_aliases));
    }
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_confidence_isSet) {
        obj.insert(QString("confidence"), ::OpenAPI::toJsonValue(m_confidence));
    }
    if (m_dob.size() > 0) {
        obj.insert(QString("dob"), ::OpenAPI::toJsonValue(m_dob));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_gender_isSet) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_legal_basis.size() > 0) {
        obj.insert(QString("legalBasis"), ::OpenAPI::toJsonValue(m_legal_basis));
    }
    if (m_nationality_isSet) {
        obj.insert(QString("nationality"), ::OpenAPI::toJsonValue(m_nationality));
    }
    if (m_passport.size() > 0) {
        obj.insert(QString("passport"), ::OpenAPI::toJsonValue(m_passport));
    }
    if (m_regime_isSet) {
        obj.insert(QString("regime"), ::OpenAPI::toJsonValue(m_regime));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_source_type_isSet) {
        obj.insert(QString("sourceType"), ::OpenAPI::toJsonValue(m_source_type));
    }
    if (m_title.size() > 0) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<OAISelfLink> OAIAML::getLinks() const {
    return m__links;
}
void OAIAML::setLinks(const QList<OAISelfLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIAML::is__links_Set() const{
    return m__links_isSet;
}

bool OAIAML::is__links_Valid() const{
    return m__links_isValid;
}

QList<OAIAML_address_inner> OAIAML::getAddress() const {
    return m_address;
}
void OAIAML::setAddress(const QList<OAIAML_address_inner> &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIAML::is_address_Set() const{
    return m_address_isSet;
}

bool OAIAML::is_address_Valid() const{
    return m_address_isValid;
}

QList<OAIAML_aliases_inner> OAIAML::getAliases() const {
    return m_aliases;
}
void OAIAML::setAliases(const QList<OAIAML_aliases_inner> &aliases) {
    m_aliases = aliases;
    m_aliases_isSet = true;
}

bool OAIAML::is_aliases_Set() const{
    return m_aliases_isSet;
}

bool OAIAML::is_aliases_Valid() const{
    return m_aliases_isValid;
}

QString OAIAML::getComments() const {
    return m_comments;
}
void OAIAML::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAIAML::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAIAML::is_comments_Valid() const{
    return m_comments_isValid;
}

QString OAIAML::getConfidence() const {
    return m_confidence;
}
void OAIAML::setConfidence(const QString &confidence) {
    m_confidence = confidence;
    m_confidence_isSet = true;
}

bool OAIAML::is_confidence_Set() const{
    return m_confidence_isSet;
}

bool OAIAML::is_confidence_Valid() const{
    return m_confidence_isValid;
}

QList<QDate> OAIAML::getDob() const {
    return m_dob;
}
void OAIAML::setDob(const QList<QDate> &dob) {
    m_dob = dob;
    m_dob_isSet = true;
}

bool OAIAML::is_dob_Set() const{
    return m_dob_isSet;
}

bool OAIAML::is_dob_Valid() const{
    return m_dob_isValid;
}

QString OAIAML::getFirstName() const {
    return m_first_name;
}
void OAIAML::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIAML::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIAML::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIAML::getGender() const {
    return m_gender;
}
void OAIAML::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIAML::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIAML::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAIAML::getLastName() const {
    return m_last_name;
}
void OAIAML::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIAML::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIAML::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QList<QString> OAIAML::getLegalBasis() const {
    return m_legal_basis;
}
void OAIAML::setLegalBasis(const QList<QString> &legal_basis) {
    m_legal_basis = legal_basis;
    m_legal_basis_isSet = true;
}

bool OAIAML::is_legal_basis_Set() const{
    return m_legal_basis_isSet;
}

bool OAIAML::is_legal_basis_Valid() const{
    return m_legal_basis_isValid;
}

QString OAIAML::getNationality() const {
    return m_nationality;
}
void OAIAML::setNationality(const QString &nationality) {
    m_nationality = nationality;
    m_nationality_isSet = true;
}

bool OAIAML::is_nationality_Set() const{
    return m_nationality_isSet;
}

bool OAIAML::is_nationality_Valid() const{
    return m_nationality_isValid;
}

QList<OAIAML_passport_inner> OAIAML::getPassport() const {
    return m_passport;
}
void OAIAML::setPassport(const QList<OAIAML_passport_inner> &passport) {
    m_passport = passport;
    m_passport_isSet = true;
}

bool OAIAML::is_passport_Set() const{
    return m_passport_isSet;
}

bool OAIAML::is_passport_Valid() const{
    return m_passport_isValid;
}

QString OAIAML::getRegime() const {
    return m_regime;
}
void OAIAML::setRegime(const QString &regime) {
    m_regime = regime;
    m_regime_isSet = true;
}

bool OAIAML::is_regime_Set() const{
    return m_regime_isSet;
}

bool OAIAML::is_regime_Valid() const{
    return m_regime_isValid;
}

QString OAIAML::getSource() const {
    return m_source;
}
void OAIAML::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIAML::is_source_Set() const{
    return m_source_isSet;
}

bool OAIAML::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIAML::getSourceType() const {
    return m_source_type;
}
void OAIAML::setSourceType(const QString &source_type) {
    m_source_type = source_type;
    m_source_type_isSet = true;
}

bool OAIAML::is_source_type_Set() const{
    return m_source_type_isSet;
}

bool OAIAML::is_source_type_Valid() const{
    return m_source_type_isValid;
}

QList<QString> OAIAML::getTitle() const {
    return m_title;
}
void OAIAML::setTitle(const QList<QString> &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIAML::is_title_Set() const{
    return m_title_isSet;
}

bool OAIAML::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIAML::getType() const {
    return m_type;
}
void OAIAML::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAML::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAML::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAML::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_address.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_aliases.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_confidence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dob.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_legal_basis.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_nationality_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_passport.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_regime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAML::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
