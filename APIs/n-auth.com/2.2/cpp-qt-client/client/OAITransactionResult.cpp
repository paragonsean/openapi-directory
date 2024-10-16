/**
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITransactionResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransactionResult::OAITransactionResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransactionResult::OAITransactionResult() {
    this->initializeModel();
}

OAITransactionResult::~OAITransactionResult() {}

void OAITransactionResult::initializeModel() {

    m_tstatus_isSet = false;
    m_tstatus_isValid = false;
}

void OAITransactionResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransactionResult::fromJsonObject(QJsonObject json) {

    m_tstatus_isValid = ::OpenAPI::fromJsonValue(m_tstatus, json[QString("tstatus")]);
    m_tstatus_isSet = !json[QString("tstatus")].isNull() && m_tstatus_isValid;
}

QString OAITransactionResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransactionResult::asJsonObject() const {
    QJsonObject obj;
    if (m_tstatus_isSet) {
        obj.insert(QString("tstatus"), ::OpenAPI::toJsonValue(m_tstatus));
    }
    return obj;
}

QString OAITransactionResult::getTstatus() const {
    return m_tstatus;
}
void OAITransactionResult::setTstatus(const QString &tstatus) {
    m_tstatus = tstatus;
    m_tstatus_isSet = true;
}

bool OAITransactionResult::is_tstatus_Set() const{
    return m_tstatus_isSet;
}

bool OAITransactionResult::is_tstatus_Valid() const{
    return m_tstatus_isValid;
}

bool OAITransactionResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_tstatus_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITransactionResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
