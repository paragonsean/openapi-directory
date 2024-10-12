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

#include "OAIIdentityMatches.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIdentityMatches::OAIIdentityMatches(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIdentityMatches::OAIIdentityMatches() {
    this->initializeModel();
}

OAIIdentityMatches::~OAIIdentityMatches() {}

void OAIIdentityMatches::initializeModel() {

    m_contains_image_isSet = false;
    m_contains_image_isValid = false;

    m_date_of_birth_isSet = false;
    m_date_of_birth_isValid = false;

    m_expiry_date_isSet = false;
    m_expiry_date_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_has_minimal_age_isSet = false;
    m_has_minimal_age_isValid = false;

    m_is_identity_document_isSet = false;
    m_is_identity_document_isValid = false;

    m_is_published_online_isSet = false;
    m_is_published_online_isValid = false;

    m_issue_date_isSet = false;
    m_issue_date_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_nationality_isSet = false;
    m_nationality_isValid = false;
}

void OAIIdentityMatches::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIdentityMatches::fromJsonObject(QJsonObject json) {

    m_contains_image_isValid = ::OpenAPI::fromJsonValue(m_contains_image, json[QString("containsImage")]);
    m_contains_image_isSet = !json[QString("containsImage")].isNull() && m_contains_image_isValid;

    m_date_of_birth_isValid = ::OpenAPI::fromJsonValue(m_date_of_birth, json[QString("dateOfBirth")]);
    m_date_of_birth_isSet = !json[QString("dateOfBirth")].isNull() && m_date_of_birth_isValid;

    m_expiry_date_isValid = ::OpenAPI::fromJsonValue(m_expiry_date, json[QString("expiryDate")]);
    m_expiry_date_isSet = !json[QString("expiryDate")].isNull() && m_expiry_date_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_has_minimal_age_isValid = ::OpenAPI::fromJsonValue(m_has_minimal_age, json[QString("hasMinimalAge")]);
    m_has_minimal_age_isSet = !json[QString("hasMinimalAge")].isNull() && m_has_minimal_age_isValid;

    m_is_identity_document_isValid = ::OpenAPI::fromJsonValue(m_is_identity_document, json[QString("isIdentityDocument")]);
    m_is_identity_document_isSet = !json[QString("isIdentityDocument")].isNull() && m_is_identity_document_isValid;

    m_is_published_online_isValid = ::OpenAPI::fromJsonValue(m_is_published_online, json[QString("isPublishedOnline")]);
    m_is_published_online_isSet = !json[QString("isPublishedOnline")].isNull() && m_is_published_online_isValid;

    m_issue_date_isValid = ::OpenAPI::fromJsonValue(m_issue_date, json[QString("issueDate")]);
    m_issue_date_isSet = !json[QString("issueDate")].isNull() && m_issue_date_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_nationality_isValid = ::OpenAPI::fromJsonValue(m_nationality, json[QString("nationality")]);
    m_nationality_isSet = !json[QString("nationality")].isNull() && m_nationality_isValid;
}

QString OAIIdentityMatches::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIdentityMatches::asJsonObject() const {
    QJsonObject obj;
    if (m_contains_image_isSet) {
        obj.insert(QString("containsImage"), ::OpenAPI::toJsonValue(m_contains_image));
    }
    if (m_date_of_birth_isSet) {
        obj.insert(QString("dateOfBirth"), ::OpenAPI::toJsonValue(m_date_of_birth));
    }
    if (m_expiry_date_isSet) {
        obj.insert(QString("expiryDate"), ::OpenAPI::toJsonValue(m_expiry_date));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_has_minimal_age_isSet) {
        obj.insert(QString("hasMinimalAge"), ::OpenAPI::toJsonValue(m_has_minimal_age));
    }
    if (m_is_identity_document_isSet) {
        obj.insert(QString("isIdentityDocument"), ::OpenAPI::toJsonValue(m_is_identity_document));
    }
    if (m_is_published_online_isSet) {
        obj.insert(QString("isPublishedOnline"), ::OpenAPI::toJsonValue(m_is_published_online));
    }
    if (m_issue_date_isSet) {
        obj.insert(QString("issueDate"), ::OpenAPI::toJsonValue(m_issue_date));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_nationality_isSet) {
        obj.insert(QString("nationality"), ::OpenAPI::toJsonValue(m_nationality));
    }
    return obj;
}

bool OAIIdentityMatches::isContainsImage() const {
    return m_contains_image;
}
void OAIIdentityMatches::setContainsImage(const bool &contains_image) {
    m_contains_image = contains_image;
    m_contains_image_isSet = true;
}

bool OAIIdentityMatches::is_contains_image_Set() const{
    return m_contains_image_isSet;
}

bool OAIIdentityMatches::is_contains_image_Valid() const{
    return m_contains_image_isValid;
}

QDateTime OAIIdentityMatches::getDateOfBirth() const {
    return m_date_of_birth;
}
void OAIIdentityMatches::setDateOfBirth(const QDateTime &date_of_birth) {
    m_date_of_birth = date_of_birth;
    m_date_of_birth_isSet = true;
}

bool OAIIdentityMatches::is_date_of_birth_Set() const{
    return m_date_of_birth_isSet;
}

bool OAIIdentityMatches::is_date_of_birth_Valid() const{
    return m_date_of_birth_isValid;
}

QDateTime OAIIdentityMatches::getExpiryDate() const {
    return m_expiry_date;
}
void OAIIdentityMatches::setExpiryDate(const QDateTime &expiry_date) {
    m_expiry_date = expiry_date;
    m_expiry_date_isSet = true;
}

bool OAIIdentityMatches::is_expiry_date_Set() const{
    return m_expiry_date_isSet;
}

bool OAIIdentityMatches::is_expiry_date_Valid() const{
    return m_expiry_date_isValid;
}

QString OAIIdentityMatches::getFirstName() const {
    return m_first_name;
}
void OAIIdentityMatches::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIIdentityMatches::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIIdentityMatches::is_first_name_Valid() const{
    return m_first_name_isValid;
}

bool OAIIdentityMatches::isHasMinimalAge() const {
    return m_has_minimal_age;
}
void OAIIdentityMatches::setHasMinimalAge(const bool &has_minimal_age) {
    m_has_minimal_age = has_minimal_age;
    m_has_minimal_age_isSet = true;
}

bool OAIIdentityMatches::is_has_minimal_age_Set() const{
    return m_has_minimal_age_isSet;
}

bool OAIIdentityMatches::is_has_minimal_age_Valid() const{
    return m_has_minimal_age_isValid;
}

bool OAIIdentityMatches::isIsIdentityDocument() const {
    return m_is_identity_document;
}
void OAIIdentityMatches::setIsIdentityDocument(const bool &is_identity_document) {
    m_is_identity_document = is_identity_document;
    m_is_identity_document_isSet = true;
}

bool OAIIdentityMatches::is_is_identity_document_Set() const{
    return m_is_identity_document_isSet;
}

bool OAIIdentityMatches::is_is_identity_document_Valid() const{
    return m_is_identity_document_isValid;
}

bool OAIIdentityMatches::isIsPublishedOnline() const {
    return m_is_published_online;
}
void OAIIdentityMatches::setIsPublishedOnline(const bool &is_published_online) {
    m_is_published_online = is_published_online;
    m_is_published_online_isSet = true;
}

bool OAIIdentityMatches::is_is_published_online_Set() const{
    return m_is_published_online_isSet;
}

bool OAIIdentityMatches::is_is_published_online_Valid() const{
    return m_is_published_online_isValid;
}

QDateTime OAIIdentityMatches::getIssueDate() const {
    return m_issue_date;
}
void OAIIdentityMatches::setIssueDate(const QDateTime &issue_date) {
    m_issue_date = issue_date;
    m_issue_date_isSet = true;
}

bool OAIIdentityMatches::is_issue_date_Set() const{
    return m_issue_date_isSet;
}

bool OAIIdentityMatches::is_issue_date_Valid() const{
    return m_issue_date_isValid;
}

QString OAIIdentityMatches::getLastName() const {
    return m_last_name;
}
void OAIIdentityMatches::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIIdentityMatches::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIIdentityMatches::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIIdentityMatches::getNationality() const {
    return m_nationality;
}
void OAIIdentityMatches::setNationality(const QString &nationality) {
    m_nationality = nationality;
    m_nationality_isSet = true;
}

bool OAIIdentityMatches::is_nationality_Set() const{
    return m_nationality_isSet;
}

bool OAIIdentityMatches::is_nationality_Valid() const{
    return m_nationality_isValid;
}

bool OAIIdentityMatches::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contains_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiry_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_minimal_age_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_identity_document_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_published_online_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issue_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nationality_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIdentityMatches::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
