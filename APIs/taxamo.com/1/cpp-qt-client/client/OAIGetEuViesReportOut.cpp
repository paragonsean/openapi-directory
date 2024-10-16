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

#include "OAIGetEuViesReportOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetEuViesReportOut::OAIGetEuViesReportOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetEuViesReportOut::OAIGetEuViesReportOut() {
    this->initializeModel();
}

OAIGetEuViesReportOut::~OAIGetEuViesReportOut() {}

void OAIGetEuViesReportOut::initializeModel() {

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_report_isSet = false;
    m_report_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;
}

void OAIGetEuViesReportOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetEuViesReportOut::fromJsonObject(QJsonObject json) {

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("currency_code")]);
    m_currency_code_isSet = !json[QString("currency_code")].isNull() && m_currency_code_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_report_isValid = ::OpenAPI::fromJsonValue(m_report, json[QString("report")]);
    m_report_isSet = !json[QString("report")].isNull() && m_report_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;
}

QString OAIGetEuViesReportOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetEuViesReportOut::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_code_isSet) {
        obj.insert(QString("currency_code"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_report.size() > 0) {
        obj.insert(QString("report"), ::OpenAPI::toJsonValue(m_report));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    return obj;
}

QString OAIGetEuViesReportOut::getCurrencyCode() const {
    return m_currency_code;
}
void OAIGetEuViesReportOut::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAIGetEuViesReportOut::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAIGetEuViesReportOut::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

QString OAIGetEuViesReportOut::getEndDate() const {
    return m_end_date;
}
void OAIGetEuViesReportOut::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIGetEuViesReportOut::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIGetEuViesReportOut::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QList<OAIReport> OAIGetEuViesReportOut::getReport() const {
    return m_report;
}
void OAIGetEuViesReportOut::setReport(const QList<OAIReport> &report) {
    m_report = report;
    m_report_isSet = true;
}

bool OAIGetEuViesReportOut::is_report_Set() const{
    return m_report_isSet;
}

bool OAIGetEuViesReportOut::is_report_Valid() const{
    return m_report_isValid;
}

QString OAIGetEuViesReportOut::getStartDate() const {
    return m_start_date;
}
void OAIGetEuViesReportOut::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIGetEuViesReportOut::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIGetEuViesReportOut::is_start_date_Valid() const{
    return m_start_date_isValid;
}

bool OAIGetEuViesReportOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetEuViesReportOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
