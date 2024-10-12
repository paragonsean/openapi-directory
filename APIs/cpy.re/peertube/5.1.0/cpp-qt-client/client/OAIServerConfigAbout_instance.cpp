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

#include "OAIServerConfigAbout_instance.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServerConfigAbout_instance::OAIServerConfigAbout_instance(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServerConfigAbout_instance::OAIServerConfigAbout_instance() {
    this->initializeModel();
}

OAIServerConfigAbout_instance::~OAIServerConfigAbout_instance() {}

void OAIServerConfigAbout_instance::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_short_description_isSet = false;
    m_short_description_isValid = false;

    m_terms_isSet = false;
    m_terms_isValid = false;
}

void OAIServerConfigAbout_instance::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServerConfigAbout_instance::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_short_description_isValid = ::OpenAPI::fromJsonValue(m_short_description, json[QString("shortDescription")]);
    m_short_description_isSet = !json[QString("shortDescription")].isNull() && m_short_description_isValid;

    m_terms_isValid = ::OpenAPI::fromJsonValue(m_terms, json[QString("terms")]);
    m_terms_isSet = !json[QString("terms")].isNull() && m_terms_isValid;
}

QString OAIServerConfigAbout_instance::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServerConfigAbout_instance::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_short_description_isSet) {
        obj.insert(QString("shortDescription"), ::OpenAPI::toJsonValue(m_short_description));
    }
    if (m_terms_isSet) {
        obj.insert(QString("terms"), ::OpenAPI::toJsonValue(m_terms));
    }
    return obj;
}

QString OAIServerConfigAbout_instance::getDescription() const {
    return m_description;
}
void OAIServerConfigAbout_instance::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIServerConfigAbout_instance::is_description_Set() const{
    return m_description_isSet;
}

bool OAIServerConfigAbout_instance::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIServerConfigAbout_instance::getName() const {
    return m_name;
}
void OAIServerConfigAbout_instance::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIServerConfigAbout_instance::is_name_Set() const{
    return m_name_isSet;
}

bool OAIServerConfigAbout_instance::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIServerConfigAbout_instance::getShortDescription() const {
    return m_short_description;
}
void OAIServerConfigAbout_instance::setShortDescription(const QString &short_description) {
    m_short_description = short_description;
    m_short_description_isSet = true;
}

bool OAIServerConfigAbout_instance::is_short_description_Set() const{
    return m_short_description_isSet;
}

bool OAIServerConfigAbout_instance::is_short_description_Valid() const{
    return m_short_description_isValid;
}

QString OAIServerConfigAbout_instance::getTerms() const {
    return m_terms;
}
void OAIServerConfigAbout_instance::setTerms(const QString &terms) {
    m_terms = terms;
    m_terms_isSet = true;
}

bool OAIServerConfigAbout_instance::is_terms_Set() const{
    return m_terms_isSet;
}

bool OAIServerConfigAbout_instance::is_terms_Valid() const{
    return m_terms_isValid;
}

bool OAIServerConfigAbout_instance::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_short_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_terms_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServerConfigAbout_instance::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
