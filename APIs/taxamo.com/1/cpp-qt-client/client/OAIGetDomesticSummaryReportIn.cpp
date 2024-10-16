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

#include "OAIGetDomesticSummaryReportIn.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetDomesticSummaryReportIn::OAIGetDomesticSummaryReportIn(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetDomesticSummaryReportIn::OAIGetDomesticSummaryReportIn() {
    this->initializeModel();
}

OAIGetDomesticSummaryReportIn::~OAIGetDomesticSummaryReportIn() {}

void OAIGetDomesticSummaryReportIn::initializeModel() {

    m_country_code_isSet = false;
    m_country_code_isValid = false;

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_end_month_isSet = false;
    m_end_month_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_fx_date_type_isSet = false;
    m_fx_date_type_isValid = false;

    m_start_month_isSet = false;
    m_start_month_isValid = false;
}

void OAIGetDomesticSummaryReportIn::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetDomesticSummaryReportIn::fromJsonObject(QJsonObject json) {

    m_country_code_isValid = ::OpenAPI::fromJsonValue(m_country_code, json[QString("country_code")]);
    m_country_code_isSet = !json[QString("country_code")].isNull() && m_country_code_isValid;

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("currency_code")]);
    m_currency_code_isSet = !json[QString("currency_code")].isNull() && m_currency_code_isValid;

    m_end_month_isValid = ::OpenAPI::fromJsonValue(m_end_month, json[QString("end_month")]);
    m_end_month_isSet = !json[QString("end_month")].isNull() && m_end_month_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_fx_date_type_isValid = ::OpenAPI::fromJsonValue(m_fx_date_type, json[QString("fx_date_type")]);
    m_fx_date_type_isSet = !json[QString("fx_date_type")].isNull() && m_fx_date_type_isValid;

    m_start_month_isValid = ::OpenAPI::fromJsonValue(m_start_month, json[QString("start_month")]);
    m_start_month_isSet = !json[QString("start_month")].isNull() && m_start_month_isValid;
}

QString OAIGetDomesticSummaryReportIn::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetDomesticSummaryReportIn::asJsonObject() const {
    QJsonObject obj;
    if (m_country_code_isSet) {
        obj.insert(QString("country_code"), ::OpenAPI::toJsonValue(m_country_code));
    }
    if (m_currency_code_isSet) {
        obj.insert(QString("currency_code"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_end_month_isSet) {
        obj.insert(QString("end_month"), ::OpenAPI::toJsonValue(m_end_month));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_fx_date_type_isSet) {
        obj.insert(QString("fx_date_type"), ::OpenAPI::toJsonValue(m_fx_date_type));
    }
    if (m_start_month_isSet) {
        obj.insert(QString("start_month"), ::OpenAPI::toJsonValue(m_start_month));
    }
    return obj;
}

QString OAIGetDomesticSummaryReportIn::getCountryCode() const {
    return m_country_code;
}
void OAIGetDomesticSummaryReportIn::setCountryCode(const QString &country_code) {
    m_country_code = country_code;
    m_country_code_isSet = true;
}

bool OAIGetDomesticSummaryReportIn::is_country_code_Set() const{
    return m_country_code_isSet;
}

bool OAIGetDomesticSummaryReportIn::is_country_code_Valid() const{
    return m_country_code_isValid;
}

QString OAIGetDomesticSummaryReportIn::getCurrencyCode() const {
    return m_currency_code;
}
void OAIGetDomesticSummaryReportIn::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAIGetDomesticSummaryReportIn::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAIGetDomesticSummaryReportIn::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

QString OAIGetDomesticSummaryReportIn::getEndMonth() const {
    return m_end_month;
}
void OAIGetDomesticSummaryReportIn::setEndMonth(const QString &end_month) {
    m_end_month = end_month;
    m_end_month_isSet = true;
}

bool OAIGetDomesticSummaryReportIn::is_end_month_Set() const{
    return m_end_month_isSet;
}

bool OAIGetDomesticSummaryReportIn::is_end_month_Valid() const{
    return m_end_month_isValid;
}

QString OAIGetDomesticSummaryReportIn::getFormat() const {
    return m_format;
}
void OAIGetDomesticSummaryReportIn::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAIGetDomesticSummaryReportIn::is_format_Set() const{
    return m_format_isSet;
}

bool OAIGetDomesticSummaryReportIn::is_format_Valid() const{
    return m_format_isValid;
}

QString OAIGetDomesticSummaryReportIn::getFxDateType() const {
    return m_fx_date_type;
}
void OAIGetDomesticSummaryReportIn::setFxDateType(const QString &fx_date_type) {
    m_fx_date_type = fx_date_type;
    m_fx_date_type_isSet = true;
}

bool OAIGetDomesticSummaryReportIn::is_fx_date_type_Set() const{
    return m_fx_date_type_isSet;
}

bool OAIGetDomesticSummaryReportIn::is_fx_date_type_Valid() const{
    return m_fx_date_type_isValid;
}

QString OAIGetDomesticSummaryReportIn::getStartMonth() const {
    return m_start_month;
}
void OAIGetDomesticSummaryReportIn::setStartMonth(const QString &start_month) {
    m_start_month = start_month;
    m_start_month_isSet = true;
}

bool OAIGetDomesticSummaryReportIn::is_start_month_Set() const{
    return m_start_month_isSet;
}

bool OAIGetDomesticSummaryReportIn::is_start_month_Valid() const{
    return m_start_month_isValid;
}

bool OAIGetDomesticSummaryReportIn::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_month_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fx_date_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_month_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetDomesticSummaryReportIn::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_country_code_isValid && m_end_month_isValid && m_start_month_isValid && true;
}

} // namespace OpenAPI
