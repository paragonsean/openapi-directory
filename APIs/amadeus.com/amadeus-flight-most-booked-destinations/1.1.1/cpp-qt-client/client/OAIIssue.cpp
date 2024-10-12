/**
 * Flight Most Booked Destinations
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.1.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIssue.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssue::OAIIssue(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssue::OAIIssue() {
    this->initializeModel();
}

OAIIssue::~OAIIssue() {}

void OAIIssue::initializeModel() {

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

void OAIIssue::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssue::fromJsonObject(QJsonObject json) {

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

QString OAIIssue::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssue::asJsonObject() const {
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

qint64 OAIIssue::getCode() const {
    return m_code;
}
void OAIIssue::setCode(const qint64 &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIIssue::is_code_Set() const{
    return m_code_isSet;
}

bool OAIIssue::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIIssue::getDetail() const {
    return m_detail;
}
void OAIIssue::setDetail(const QString &detail) {
    m_detail = detail;
    m_detail_isSet = true;
}

bool OAIIssue::is_detail_Set() const{
    return m_detail_isSet;
}

bool OAIIssue::is_detail_Valid() const{
    return m_detail_isValid;
}

OAIIssue_Source OAIIssue::getSource() const {
    return m_source;
}
void OAIIssue::setSource(const OAIIssue_Source &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIIssue::is_source_Set() const{
    return m_source_isSet;
}

bool OAIIssue::is_source_Valid() const{
    return m_source_isValid;
}

qint32 OAIIssue::getStatus() const {
    return m_status;
}
void OAIIssue::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIIssue::is_status_Set() const{
    return m_status_isSet;
}

bool OAIIssue::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIIssue::getTitle() const {
    return m_title;
}
void OAIIssue::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIIssue::is_title_Set() const{
    return m_title_isSet;
}

bool OAIIssue::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIIssue::isSet() const {
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

bool OAIIssue::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
