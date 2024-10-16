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

#include "OAIEstimateListExpandVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEstimateListExpandVO::OAIEstimateListExpandVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEstimateListExpandVO::OAIEstimateListExpandVO() {
    this->initializeModel();
}

OAIEstimateListExpandVO::~OAIEstimateListExpandVO() {}

void OAIEstimateListExpandVO::initializeModel() {

    m_result_isSet = false;
    m_result_isValid = false;

    m_status_code_isSet = false;
    m_status_code_isValid = false;

    m_status_reason_isSet = false;
    m_status_reason_isValid = false;
}

void OAIEstimateListExpandVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEstimateListExpandVO::fromJsonObject(QJsonObject json) {

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("result")]);
    m_result_isSet = !json[QString("result")].isNull() && m_result_isValid;

    m_status_code_isValid = ::OpenAPI::fromJsonValue(m_status_code, json[QString("status_code")]);
    m_status_code_isSet = !json[QString("status_code")].isNull() && m_status_code_isValid;

    m_status_reason_isValid = ::OpenAPI::fromJsonValue(m_status_reason, json[QString("status_reason")]);
    m_status_reason_isSet = !json[QString("status_reason")].isNull() && m_status_reason_isValid;
}

QString OAIEstimateListExpandVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEstimateListExpandVO::asJsonObject() const {
    QJsonObject obj;
    if (m_result.size() > 0) {
        obj.insert(QString("result"), ::OpenAPI::toJsonValue(m_result));
    }
    if (m_status_code_isSet) {
        obj.insert(QString("status_code"), ::OpenAPI::toJsonValue(m_status_code));
    }
    if (m_status_reason_isSet) {
        obj.insert(QString("status_reason"), ::OpenAPI::toJsonValue(m_status_reason));
    }
    return obj;
}

QList<OAIEstimateBaseVO> OAIEstimateListExpandVO::getResult() const {
    return m_result;
}
void OAIEstimateListExpandVO::setResult(const QList<OAIEstimateBaseVO> &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAIEstimateListExpandVO::is_result_Set() const{
    return m_result_isSet;
}

bool OAIEstimateListExpandVO::is_result_Valid() const{
    return m_result_isValid;
}

qint32 OAIEstimateListExpandVO::getStatusCode() const {
    return m_status_code;
}
void OAIEstimateListExpandVO::setStatusCode(const qint32 &status_code) {
    m_status_code = status_code;
    m_status_code_isSet = true;
}

bool OAIEstimateListExpandVO::is_status_code_Set() const{
    return m_status_code_isSet;
}

bool OAIEstimateListExpandVO::is_status_code_Valid() const{
    return m_status_code_isValid;
}

QString OAIEstimateListExpandVO::getStatusReason() const {
    return m_status_reason;
}
void OAIEstimateListExpandVO::setStatusReason(const QString &status_reason) {
    m_status_reason = status_reason;
    m_status_reason_isSet = true;
}

bool OAIEstimateListExpandVO::is_status_reason_Set() const{
    return m_status_reason_isSet;
}

bool OAIEstimateListExpandVO::is_status_reason_Valid() const{
    return m_status_reason_isValid;
}

bool OAIEstimateListExpandVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_result.size() > 0) {
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

bool OAIEstimateListExpandVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
