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

#include "OAI_api_v1_abuses_post_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_api_v1_abuses_post_request::OAI_api_v1_abuses_post_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_api_v1_abuses_post_request::OAI_api_v1_abuses_post_request() {
    this->initializeModel();
}

OAI_api_v1_abuses_post_request::~OAI_api_v1_abuses_post_request() {}

void OAI_api_v1_abuses_post_request::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_predefined_reasons_isSet = false;
    m_predefined_reasons_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_video_isSet = false;
    m_video_isValid = false;
}

void OAI_api_v1_abuses_post_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_api_v1_abuses_post_request::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("comment")]);
    m_comment_isSet = !json[QString("comment")].isNull() && m_comment_isValid;

    m_predefined_reasons_isValid = ::OpenAPI::fromJsonValue(m_predefined_reasons, json[QString("predefinedReasons")]);
    m_predefined_reasons_isSet = !json[QString("predefinedReasons")].isNull() && m_predefined_reasons_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_video_isValid = ::OpenAPI::fromJsonValue(m_video, json[QString("video")]);
    m_video_isSet = !json[QString("video")].isNull() && m_video_isValid;
}

QString OAI_api_v1_abuses_post_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_api_v1_abuses_post_request::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_comment.isSet()) {
        obj.insert(QString("comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_predefined_reasons.size() > 0) {
        obj.insert(QString("predefinedReasons"), ::OpenAPI::toJsonValue(m_predefined_reasons));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_video.isSet()) {
        obj.insert(QString("video"), ::OpenAPI::toJsonValue(m_video));
    }
    return obj;
}

OAI_api_v1_abuses_post_request_account OAI_api_v1_abuses_post_request::getAccount() const {
    return m_account;
}
void OAI_api_v1_abuses_post_request::setAccount(const OAI_api_v1_abuses_post_request_account &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAI_api_v1_abuses_post_request::is_account_Set() const{
    return m_account_isSet;
}

bool OAI_api_v1_abuses_post_request::is_account_Valid() const{
    return m_account_isValid;
}

OAI_api_v1_abuses_post_request_comment OAI_api_v1_abuses_post_request::getComment() const {
    return m_comment;
}
void OAI_api_v1_abuses_post_request::setComment(const OAI_api_v1_abuses_post_request_comment &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAI_api_v1_abuses_post_request::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAI_api_v1_abuses_post_request::is_comment_Valid() const{
    return m_comment_isValid;
}

QList<QString> OAI_api_v1_abuses_post_request::getPredefinedReasons() const {
    return m_predefined_reasons;
}
void OAI_api_v1_abuses_post_request::setPredefinedReasons(const QList<QString> &predefined_reasons) {
    m_predefined_reasons = predefined_reasons;
    m_predefined_reasons_isSet = true;
}

bool OAI_api_v1_abuses_post_request::is_predefined_reasons_Set() const{
    return m_predefined_reasons_isSet;
}

bool OAI_api_v1_abuses_post_request::is_predefined_reasons_Valid() const{
    return m_predefined_reasons_isValid;
}

QString OAI_api_v1_abuses_post_request::getReason() const {
    return m_reason;
}
void OAI_api_v1_abuses_post_request::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAI_api_v1_abuses_post_request::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAI_api_v1_abuses_post_request::is_reason_Valid() const{
    return m_reason_isValid;
}

OAI_api_v1_abuses_post_request_video OAI_api_v1_abuses_post_request::getVideo() const {
    return m_video;
}
void OAI_api_v1_abuses_post_request::setVideo(const OAI_api_v1_abuses_post_request_video &video) {
    m_video = video;
    m_video_isSet = true;
}

bool OAI_api_v1_abuses_post_request::is_video_Set() const{
    return m_video_isSet;
}

bool OAI_api_v1_abuses_post_request::is_video_Valid() const{
    return m_video_isValid;
}

bool OAI_api_v1_abuses_post_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_predefined_reasons.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_api_v1_abuses_post_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_reason_isValid && true;
}

} // namespace OpenAPI
