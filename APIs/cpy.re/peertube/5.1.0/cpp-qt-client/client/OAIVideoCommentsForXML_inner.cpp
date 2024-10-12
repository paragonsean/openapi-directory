/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVideoCommentsForXML_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoCommentsForXML_inner::OAIVideoCommentsForXML_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoCommentsForXML_inner::OAIVideoCommentsForXML_inner() {
    this->initializeModel();
}

OAIVideoCommentsForXML_inner::~OAIVideoCommentsForXML_inner() {}

void OAIVideoCommentsForXML_inner::initializeModel() {

    m_contentencoded_isSet = false;
    m_contentencoded_isValid = false;

    m_dccreator_isSet = false;
    m_dccreator_isValid = false;

    m_guid_isSet = false;
    m_guid_isValid = false;

    m_link_isSet = false;
    m_link_isValid = false;

    m_pub_date_isSet = false;
    m_pub_date_isValid = false;
}

void OAIVideoCommentsForXML_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoCommentsForXML_inner::fromJsonObject(QJsonObject json) {

    m_contentencoded_isValid = ::OpenAPI::fromJsonValue(m_contentencoded, json[QString("content:encoded")]);
    m_contentencoded_isSet = !json[QString("content:encoded")].isNull() && m_contentencoded_isValid;

    m_dccreator_isValid = ::OpenAPI::fromJsonValue(m_dccreator, json[QString("dc:creator")]);
    m_dccreator_isSet = !json[QString("dc:creator")].isNull() && m_dccreator_isValid;

    m_guid_isValid = ::OpenAPI::fromJsonValue(m_guid, json[QString("guid")]);
    m_guid_isSet = !json[QString("guid")].isNull() && m_guid_isValid;

    m_link_isValid = ::OpenAPI::fromJsonValue(m_link, json[QString("link")]);
    m_link_isSet = !json[QString("link")].isNull() && m_link_isValid;

    m_pub_date_isValid = ::OpenAPI::fromJsonValue(m_pub_date, json[QString("pubDate")]);
    m_pub_date_isSet = !json[QString("pubDate")].isNull() && m_pub_date_isValid;
}

QString OAIVideoCommentsForXML_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoCommentsForXML_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_contentencoded_isSet) {
        obj.insert(QString("content:encoded"), ::OpenAPI::toJsonValue(m_contentencoded));
    }
    if (m_dccreator_isSet) {
        obj.insert(QString("dc:creator"), ::OpenAPI::toJsonValue(m_dccreator));
    }
    if (m_guid_isSet) {
        obj.insert(QString("guid"), ::OpenAPI::toJsonValue(m_guid));
    }
    if (m_link_isSet) {
        obj.insert(QString("link"), ::OpenAPI::toJsonValue(m_link));
    }
    if (m_pub_date_isSet) {
        obj.insert(QString("pubDate"), ::OpenAPI::toJsonValue(m_pub_date));
    }
    return obj;
}

QString OAIVideoCommentsForXML_inner::getContentencoded() const {
    return m_contentencoded;
}
void OAIVideoCommentsForXML_inner::setContentencoded(const QString &contentencoded) {
    m_contentencoded = contentencoded;
    m_contentencoded_isSet = true;
}

bool OAIVideoCommentsForXML_inner::is_contentencoded_Set() const{
    return m_contentencoded_isSet;
}

bool OAIVideoCommentsForXML_inner::is_contentencoded_Valid() const{
    return m_contentencoded_isValid;
}

QString OAIVideoCommentsForXML_inner::getDccreator() const {
    return m_dccreator;
}
void OAIVideoCommentsForXML_inner::setDccreator(const QString &dccreator) {
    m_dccreator = dccreator;
    m_dccreator_isSet = true;
}

bool OAIVideoCommentsForXML_inner::is_dccreator_Set() const{
    return m_dccreator_isSet;
}

bool OAIVideoCommentsForXML_inner::is_dccreator_Valid() const{
    return m_dccreator_isValid;
}

QString OAIVideoCommentsForXML_inner::getGuid() const {
    return m_guid;
}
void OAIVideoCommentsForXML_inner::setGuid(const QString &guid) {
    m_guid = guid;
    m_guid_isSet = true;
}

bool OAIVideoCommentsForXML_inner::is_guid_Set() const{
    return m_guid_isSet;
}

bool OAIVideoCommentsForXML_inner::is_guid_Valid() const{
    return m_guid_isValid;
}

QString OAIVideoCommentsForXML_inner::getLink() const {
    return m_link;
}
void OAIVideoCommentsForXML_inner::setLink(const QString &link) {
    m_link = link;
    m_link_isSet = true;
}

bool OAIVideoCommentsForXML_inner::is_link_Set() const{
    return m_link_isSet;
}

bool OAIVideoCommentsForXML_inner::is_link_Valid() const{
    return m_link_isValid;
}

QDateTime OAIVideoCommentsForXML_inner::getPubDate() const {
    return m_pub_date;
}
void OAIVideoCommentsForXML_inner::setPubDate(const QDateTime &pub_date) {
    m_pub_date = pub_date;
    m_pub_date_isSet = true;
}

bool OAIVideoCommentsForXML_inner::is_pub_date_Set() const{
    return m_pub_date_isSet;
}

bool OAIVideoCommentsForXML_inner::is_pub_date_Valid() const{
    return m_pub_date_isValid;
}

bool OAIVideoCommentsForXML_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contentencoded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dccreator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_guid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pub_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoCommentsForXML_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
