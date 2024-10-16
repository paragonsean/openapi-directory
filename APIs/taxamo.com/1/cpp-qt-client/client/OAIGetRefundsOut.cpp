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

#include "OAIGetRefundsOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetRefundsOut::OAIGetRefundsOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetRefundsOut::OAIGetRefundsOut() {
    this->initializeModel();
}

OAIGetRefundsOut::~OAIGetRefundsOut() {}

void OAIGetRefundsOut::initializeModel() {

    m_report_isSet = false;
    m_report_isValid = false;
}

void OAIGetRefundsOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetRefundsOut::fromJsonObject(QJsonObject json) {

    m_report_isValid = ::OpenAPI::fromJsonValue(m_report, json[QString("report")]);
    m_report_isSet = !json[QString("report")].isNull() && m_report_isValid;
}

QString OAIGetRefundsOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetRefundsOut::asJsonObject() const {
    QJsonObject obj;
    if (m_report.size() > 0) {
        obj.insert(QString("report"), ::OpenAPI::toJsonValue(m_report));
    }
    return obj;
}

QList<OAIReport> OAIGetRefundsOut::getReport() const {
    return m_report;
}
void OAIGetRefundsOut::setReport(const QList<OAIReport> &report) {
    m_report = report;
    m_report_isSet = true;
}

bool OAIGetRefundsOut::is_report_Set() const{
    return m_report_isSet;
}

bool OAIGetRefundsOut::is_report_Valid() const{
    return m_report_isValid;
}

bool OAIGetRefundsOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_report.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetRefundsOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
