/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProjectListVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProjectListVO::OAIProjectListVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProjectListVO::OAIProjectListVO() {
    this->initializeModel();
}

OAIProjectListVO::~OAIProjectListVO() {}

void OAIProjectListVO::initializeModel() {

    m_results_isSet = false;
    m_results_isValid = false;

    m_status_code_isSet = false;
    m_status_code_isValid = false;

    m_status_reason_isSet = false;
    m_status_reason_isValid = false;
}

void OAIProjectListVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProjectListVO::fromJsonObject(QJsonObject json) {

    m_results_isValid = ::OpenAPI::fromJsonValue(m_results, json[QString("results")]);
    m_results_isSet = !json[QString("results")].isNull() && m_results_isValid;

    m_status_code_isValid = ::OpenAPI::fromJsonValue(m_status_code, json[QString("status_code")]);
    m_status_code_isSet = !json[QString("status_code")].isNull() && m_status_code_isValid;

    m_status_reason_isValid = ::OpenAPI::fromJsonValue(m_status_reason, json[QString("status_reason")]);
    m_status_reason_isSet = !json[QString("status_reason")].isNull() && m_status_reason_isValid;
}

QString OAIProjectListVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProjectListVO::asJsonObject() const {
    QJsonObject obj;
    if (m_results.size() > 0) {
        obj.insert(QString("results"), ::OpenAPI::toJsonValue(m_results));
    }
    if (m_status_code_isSet) {
        obj.insert(QString("status_code"), ::OpenAPI::toJsonValue(m_status_code));
    }
    if (m_status_reason_isSet) {
        obj.insert(QString("status_reason"), ::OpenAPI::toJsonValue(m_status_reason));
    }
    return obj;
}

QList<OAIProjectSimpleVO> OAIProjectListVO::getResults() const {
    return m_results;
}
void OAIProjectListVO::setResults(const QList<OAIProjectSimpleVO> &results) {
    m_results = results;
    m_results_isSet = true;
}

bool OAIProjectListVO::is_results_Set() const{
    return m_results_isSet;
}

bool OAIProjectListVO::is_results_Valid() const{
    return m_results_isValid;
}

qint32 OAIProjectListVO::getStatusCode() const {
    return m_status_code;
}
void OAIProjectListVO::setStatusCode(const qint32 &status_code) {
    m_status_code = status_code;
    m_status_code_isSet = true;
}

bool OAIProjectListVO::is_status_code_Set() const{
    return m_status_code_isSet;
}

bool OAIProjectListVO::is_status_code_Valid() const{
    return m_status_code_isValid;
}

QString OAIProjectListVO::getStatusReason() const {
    return m_status_reason;
}
void OAIProjectListVO::setStatusReason(const QString &status_reason) {
    m_status_reason = status_reason;
    m_status_reason_isSet = true;
}

bool OAIProjectListVO::is_status_reason_Set() const{
    return m_status_reason_isSet;
}

bool OAIProjectListVO::is_status_reason_Valid() const{
    return m_status_reason_isValid;
}

bool OAIProjectListVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_reason_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProjectListVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
