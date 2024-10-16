/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetTransactionsStatsOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetTransactionsStatsOut::OAIGetTransactionsStatsOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetTransactionsStatsOut::OAIGetTransactionsStatsOut() {
    this->initializeModel();
}

OAIGetTransactionsStatsOut::~OAIGetTransactionsStatsOut() {}

void OAIGetTransactionsStatsOut::initializeModel() {

    m_by_status_isSet = false;
    m_by_status_isValid = false;
}

void OAIGetTransactionsStatsOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetTransactionsStatsOut::fromJsonObject(QJsonObject json) {

    m_by_status_isValid = ::OpenAPI::fromJsonValue(m_by_status, json[QString("by_status")]);
    m_by_status_isSet = !json[QString("by_status")].isNull() && m_by_status_isValid;
}

QString OAIGetTransactionsStatsOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetTransactionsStatsOut::asJsonObject() const {
    QJsonObject obj;
    if (m_by_status.isSet()) {
        obj.insert(QString("by_status"), ::OpenAPI::toJsonValue(m_by_status));
    }
    return obj;
}

OAIBy_status OAIGetTransactionsStatsOut::getByStatus() const {
    return m_by_status;
}
void OAIGetTransactionsStatsOut::setByStatus(const OAIBy_status &by_status) {
    m_by_status = by_status;
    m_by_status_isSet = true;
}

bool OAIGetTransactionsStatsOut::is_by_status_Set() const{
    return m_by_status_isSet;
}

bool OAIGetTransactionsStatsOut::is_by_status_Valid() const{
    return m_by_status_isValid;
}

bool OAIGetTransactionsStatsOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_by_status.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetTransactionsStatsOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
