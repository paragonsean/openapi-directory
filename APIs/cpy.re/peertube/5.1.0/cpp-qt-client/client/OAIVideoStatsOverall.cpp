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

#include "OAIVideoStatsOverall.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVideoStatsOverall::OAIVideoStatsOverall(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVideoStatsOverall::OAIVideoStatsOverall() {
    this->initializeModel();
}

OAIVideoStatsOverall::~OAIVideoStatsOverall() {}

void OAIVideoStatsOverall::initializeModel() {

    m_average_watch_time_isSet = false;
    m_average_watch_time_isValid = false;

    m_countries_isSet = false;
    m_countries_isValid = false;

    m_total_watch_time_isSet = false;
    m_total_watch_time_isValid = false;

    m_viewers_peak_isSet = false;
    m_viewers_peak_isValid = false;

    m_viewers_peak_date_isSet = false;
    m_viewers_peak_date_isValid = false;
}

void OAIVideoStatsOverall::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVideoStatsOverall::fromJsonObject(QJsonObject json) {

    m_average_watch_time_isValid = ::OpenAPI::fromJsonValue(m_average_watch_time, json[QString("averageWatchTime")]);
    m_average_watch_time_isSet = !json[QString("averageWatchTime")].isNull() && m_average_watch_time_isValid;

    m_countries_isValid = ::OpenAPI::fromJsonValue(m_countries, json[QString("countries")]);
    m_countries_isSet = !json[QString("countries")].isNull() && m_countries_isValid;

    m_total_watch_time_isValid = ::OpenAPI::fromJsonValue(m_total_watch_time, json[QString("totalWatchTime")]);
    m_total_watch_time_isSet = !json[QString("totalWatchTime")].isNull() && m_total_watch_time_isValid;

    m_viewers_peak_isValid = ::OpenAPI::fromJsonValue(m_viewers_peak, json[QString("viewersPeak")]);
    m_viewers_peak_isSet = !json[QString("viewersPeak")].isNull() && m_viewers_peak_isValid;

    m_viewers_peak_date_isValid = ::OpenAPI::fromJsonValue(m_viewers_peak_date, json[QString("viewersPeakDate")]);
    m_viewers_peak_date_isSet = !json[QString("viewersPeakDate")].isNull() && m_viewers_peak_date_isValid;
}

QString OAIVideoStatsOverall::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVideoStatsOverall::asJsonObject() const {
    QJsonObject obj;
    if (m_average_watch_time_isSet) {
        obj.insert(QString("averageWatchTime"), ::OpenAPI::toJsonValue(m_average_watch_time));
    }
    if (m_countries.size() > 0) {
        obj.insert(QString("countries"), ::OpenAPI::toJsonValue(m_countries));
    }
    if (m_total_watch_time_isSet) {
        obj.insert(QString("totalWatchTime"), ::OpenAPI::toJsonValue(m_total_watch_time));
    }
    if (m_viewers_peak_isSet) {
        obj.insert(QString("viewersPeak"), ::OpenAPI::toJsonValue(m_viewers_peak));
    }
    if (m_viewers_peak_date_isSet) {
        obj.insert(QString("viewersPeakDate"), ::OpenAPI::toJsonValue(m_viewers_peak_date));
    }
    return obj;
}

double OAIVideoStatsOverall::getAverageWatchTime() const {
    return m_average_watch_time;
}
void OAIVideoStatsOverall::setAverageWatchTime(const double &average_watch_time) {
    m_average_watch_time = average_watch_time;
    m_average_watch_time_isSet = true;
}

bool OAIVideoStatsOverall::is_average_watch_time_Set() const{
    return m_average_watch_time_isSet;
}

bool OAIVideoStatsOverall::is_average_watch_time_Valid() const{
    return m_average_watch_time_isValid;
}

QList<OAIVideoStatsOverall_countries_inner> OAIVideoStatsOverall::getCountries() const {
    return m_countries;
}
void OAIVideoStatsOverall::setCountries(const QList<OAIVideoStatsOverall_countries_inner> &countries) {
    m_countries = countries;
    m_countries_isSet = true;
}

bool OAIVideoStatsOverall::is_countries_Set() const{
    return m_countries_isSet;
}

bool OAIVideoStatsOverall::is_countries_Valid() const{
    return m_countries_isValid;
}

double OAIVideoStatsOverall::getTotalWatchTime() const {
    return m_total_watch_time;
}
void OAIVideoStatsOverall::setTotalWatchTime(const double &total_watch_time) {
    m_total_watch_time = total_watch_time;
    m_total_watch_time_isSet = true;
}

bool OAIVideoStatsOverall::is_total_watch_time_Set() const{
    return m_total_watch_time_isSet;
}

bool OAIVideoStatsOverall::is_total_watch_time_Valid() const{
    return m_total_watch_time_isValid;
}

double OAIVideoStatsOverall::getViewersPeak() const {
    return m_viewers_peak;
}
void OAIVideoStatsOverall::setViewersPeak(const double &viewers_peak) {
    m_viewers_peak = viewers_peak;
    m_viewers_peak_isSet = true;
}

bool OAIVideoStatsOverall::is_viewers_peak_Set() const{
    return m_viewers_peak_isSet;
}

bool OAIVideoStatsOverall::is_viewers_peak_Valid() const{
    return m_viewers_peak_isValid;
}

QDateTime OAIVideoStatsOverall::getViewersPeakDate() const {
    return m_viewers_peak_date;
}
void OAIVideoStatsOverall::setViewersPeakDate(const QDateTime &viewers_peak_date) {
    m_viewers_peak_date = viewers_peak_date;
    m_viewers_peak_date_isSet = true;
}

bool OAIVideoStatsOverall::is_viewers_peak_date_Set() const{
    return m_viewers_peak_date_isSet;
}

bool OAIVideoStatsOverall::is_viewers_peak_date_Valid() const{
    return m_viewers_peak_date_isValid;
}

bool OAIVideoStatsOverall::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_average_watch_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_countries.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_watch_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_viewers_peak_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_viewers_peak_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVideoStatsOverall::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
