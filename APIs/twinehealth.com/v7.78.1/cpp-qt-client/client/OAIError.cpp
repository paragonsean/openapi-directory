/**
 * Fitbit Plus API
 * # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \"yaml\" file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. <!-- ReDoc-Inject: <security-definitions> -->  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user's identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters `page[size]` and `page[number]` to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a `links` object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=1`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=2`, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters `page[limit]` and `page[after]` to specify the max number of entries returned and identify where to begin the next page. Add `page[limit]` to the parameters to use cursor-based paging. The response will include a `links` object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[limit]=50`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, you will not see a duplicate entry when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[limit]=50&page[after]=<cursor>`.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against `meta.count`. Set `page[size]` or `page[limit]` to 0 to get only the count.  It is not valid to mix the two strategies. 
 *
 * The version of the OpenAPI document: v7.78.1
 * Contact: apiteam@twinehealth.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError::OAIError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError::OAIError() {
    this->initializeModel();
}

OAIError::~OAIError() {}

void OAIError::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_detail_isSet = false;
    m_detail_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_detail_isValid = ::OpenAPI::fromJsonValue(m_detail, json[QString("detail")]);
    m_detail_isSet = !json[QString("detail")].isNull() && m_detail_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_detail_isSet) {
        obj.insert(QString("detail"), ::OpenAPI::toJsonValue(m_detail));
    }
    if (m_source.isSet()) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAIError::getCode() const {
    return m_code;
}
void OAIError::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIError::is_code_Set() const{
    return m_code_isSet;
}

bool OAIError::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIError::getDetail() const {
    return m_detail;
}
void OAIError::setDetail(const QString &detail) {
    m_detail = detail;
    m_detail_isSet = true;
}

bool OAIError::is_detail_Set() const{
    return m_detail_isSet;
}

bool OAIError::is_detail_Valid() const{
    return m_detail_isValid;
}

OAIError_source OAIError::getSource() const {
    return m_source;
}
void OAIError::setSource(const OAIError_source &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIError::is_source_Set() const{
    return m_source_isSet;
}

bool OAIError::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIError::getStatus() const {
    return m_status;
}
void OAIError::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIError::is_status_Set() const{
    return m_status_isSet;
}

bool OAIError::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIError::getTitle() const {
    return m_title;
}
void OAIError::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIError::is_title_Set() const{
    return m_title_isSet;
}

bool OAIError::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
