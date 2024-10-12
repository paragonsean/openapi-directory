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

#include "OAIFile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFile::OAIFile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFile::OAIFile() {
    this->initializeModel();
}

OAIFile::~OAIFile() {}

void OAIFile::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_extension_isSet = false;
    m_extension_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_public_isSet = false;
    m_is_public_isValid = false;

    m_mime_isSet = false;
    m_mime_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_sha1_isSet = false;
    m_sha1_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAIFile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFile::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_extension_isValid = ::OpenAPI::fromJsonValue(m_extension, json[QString("extension")]);
    m_extension_isSet = !json[QString("extension")].isNull() && m_extension_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_public_isValid = ::OpenAPI::fromJsonValue(m_is_public, json[QString("isPublic")]);
    m_is_public_isSet = !json[QString("isPublic")].isNull() && m_is_public_isValid;

    m_mime_isValid = ::OpenAPI::fromJsonValue(m_mime, json[QString("mime")]);
    m_mime_isSet = !json[QString("mime")].isNull() && m_mime_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_sha1_isValid = ::OpenAPI::fromJsonValue(m_sha1, json[QString("sha1")]);
    m_sha1_isSet = !json[QString("sha1")].isNull() && m_sha1_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAIFile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFile::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_extension_isSet) {
        obj.insert(QString("extension"), ::OpenAPI::toJsonValue(m_extension));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_public_isSet) {
        obj.insert(QString("isPublic"), ::OpenAPI::toJsonValue(m_is_public));
    }
    if (m_mime_isSet) {
        obj.insert(QString("mime"), ::OpenAPI::toJsonValue(m_mime));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_sha1_isSet) {
        obj.insert(QString("sha1"), ::OpenAPI::toJsonValue(m_sha1));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

QList<OAIFile__links_inner> OAIFile::getLinks() const {
    return m__links;
}
void OAIFile::setLinks(const QList<OAIFile__links_inner> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIFile::is__links_Set() const{
    return m__links_isSet;
}

bool OAIFile::is__links_Valid() const{
    return m__links_isValid;
}

QDateTime OAIFile::getCreatedTime() const {
    return m_created_time;
}
void OAIFile::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIFile::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIFile::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAIFile::getDescription() const {
    return m_description;
}
void OAIFile::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIFile::is_description_Set() const{
    return m_description_isSet;
}

bool OAIFile::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIFile::getExtension() const {
    return m_extension;
}
void OAIFile::setExtension(const QString &extension) {
    m_extension = extension;
    m_extension_isSet = true;
}

bool OAIFile::is_extension_Set() const{
    return m_extension_isSet;
}

bool OAIFile::is_extension_Valid() const{
    return m_extension_isValid;
}

qint32 OAIFile::getHeight() const {
    return m_height;
}
void OAIFile::setHeight(const qint32 &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIFile::is_height_Set() const{
    return m_height_isSet;
}

bool OAIFile::is_height_Valid() const{
    return m_height_isValid;
}

QString OAIFile::getId() const {
    return m_id;
}
void OAIFile::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFile::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFile::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIFile::isIsPublic() const {
    return m_is_public;
}
void OAIFile::setIsPublic(const bool &is_public) {
    m_is_public = is_public;
    m_is_public_isSet = true;
}

bool OAIFile::is_is_public_Set() const{
    return m_is_public_isSet;
}

bool OAIFile::is_is_public_Valid() const{
    return m_is_public_isValid;
}

QString OAIFile::getMime() const {
    return m_mime;
}
void OAIFile::setMime(const QString &mime) {
    m_mime = mime;
    m_mime_isSet = true;
}

bool OAIFile::is_mime_Set() const{
    return m_mime_isSet;
}

bool OAIFile::is_mime_Valid() const{
    return m_mime_isValid;
}

QString OAIFile::getName() const {
    return m_name;
}
void OAIFile::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIFile::is_name_Set() const{
    return m_name_isSet;
}

bool OAIFile::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIFile::getSha1() const {
    return m_sha1;
}
void OAIFile::setSha1(const QString &sha1) {
    m_sha1 = sha1;
    m_sha1_isSet = true;
}

bool OAIFile::is_sha1_Set() const{
    return m_sha1_isSet;
}

bool OAIFile::is_sha1_Valid() const{
    return m_sha1_isValid;
}

qint32 OAIFile::getSize() const {
    return m_size;
}
void OAIFile::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIFile::is_size_Set() const{
    return m_size_isSet;
}

bool OAIFile::is_size_Valid() const{
    return m_size_isValid;
}

QList<QString> OAIFile::getTags() const {
    return m_tags;
}
void OAIFile::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIFile::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIFile::is_tags_Valid() const{
    return m_tags_isValid;
}

QDateTime OAIFile::getUpdatedTime() const {
    return m_updated_time;
}
void OAIFile::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIFile::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIFile::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

qint32 OAIFile::getWidth() const {
    return m_width;
}
void OAIFile::setWidth(const qint32 &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAIFile::is_width_Set() const{
    return m_width_isSet;
}

bool OAIFile::is_width_Valid() const{
    return m_width_isValid;
}

bool OAIFile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_public_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sha1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
