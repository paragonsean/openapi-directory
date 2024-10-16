/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateSystem_Models_PagedClientStatusMetadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateSystem_Models_PagedClientStatusMetadata::OAIUpdateSystem_Models_PagedClientStatusMetadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateSystem_Models_PagedClientStatusMetadata::OAIUpdateSystem_Models_PagedClientStatusMetadata() {
    this->initializeModel();
}

OAIUpdateSystem_Models_PagedClientStatusMetadata::~OAIUpdateSystem_Models_PagedClientStatusMetadata() {}

void OAIUpdateSystem_Models_PagedClientStatusMetadata::initializeModel() {

    m_limit_isSet = false;
    m_limit_isValid = false;

    m_offset_isSet = false;
    m_offset_isValid = false;

    m_report_result_expected_isSet = false;
    m_report_result_expected_isValid = false;

    m_report_result_label_isSet = false;
    m_report_result_label_isValid = false;

    m_report_value_label_isSet = false;
    m_report_value_label_isValid = false;

    m_total_count_isSet = false;
    m_total_count_isValid = false;
}

void OAIUpdateSystem_Models_PagedClientStatusMetadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateSystem_Models_PagedClientStatusMetadata::fromJsonObject(QJsonObject json) {

    m_limit_isValid = ::OpenAPI::fromJsonValue(m_limit, json[QString("Limit")]);
    m_limit_isSet = !json[QString("Limit")].isNull() && m_limit_isValid;

    m_offset_isValid = ::OpenAPI::fromJsonValue(m_offset, json[QString("Offset")]);
    m_offset_isSet = !json[QString("Offset")].isNull() && m_offset_isValid;

    m_report_result_expected_isValid = ::OpenAPI::fromJsonValue(m_report_result_expected, json[QString("ReportResultExpected")]);
    m_report_result_expected_isSet = !json[QString("ReportResultExpected")].isNull() && m_report_result_expected_isValid;

    m_report_result_label_isValid = ::OpenAPI::fromJsonValue(m_report_result_label, json[QString("ReportResultLabel")]);
    m_report_result_label_isSet = !json[QString("ReportResultLabel")].isNull() && m_report_result_label_isValid;

    m_report_value_label_isValid = ::OpenAPI::fromJsonValue(m_report_value_label, json[QString("ReportValueLabel")]);
    m_report_value_label_isSet = !json[QString("ReportValueLabel")].isNull() && m_report_value_label_isValid;

    m_total_count_isValid = ::OpenAPI::fromJsonValue(m_total_count, json[QString("TotalCount")]);
    m_total_count_isSet = !json[QString("TotalCount")].isNull() && m_total_count_isValid;
}

QString OAIUpdateSystem_Models_PagedClientStatusMetadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateSystem_Models_PagedClientStatusMetadata::asJsonObject() const {
    QJsonObject obj;
    if (m_limit_isSet) {
        obj.insert(QString("Limit"), ::OpenAPI::toJsonValue(m_limit));
    }
    if (m_offset_isSet) {
        obj.insert(QString("Offset"), ::OpenAPI::toJsonValue(m_offset));
    }
    if (m_report_result_expected_isSet) {
        obj.insert(QString("ReportResultExpected"), ::OpenAPI::toJsonValue(m_report_result_expected));
    }
    if (m_report_result_label_isSet) {
        obj.insert(QString("ReportResultLabel"), ::OpenAPI::toJsonValue(m_report_result_label));
    }
    if (m_report_value_label_isSet) {
        obj.insert(QString("ReportValueLabel"), ::OpenAPI::toJsonValue(m_report_value_label));
    }
    if (m_total_count_isSet) {
        obj.insert(QString("TotalCount"), ::OpenAPI::toJsonValue(m_total_count));
    }
    return obj;
}

qint32 OAIUpdateSystem_Models_PagedClientStatusMetadata::getLimit() const {
    return m_limit;
}
void OAIUpdateSystem_Models_PagedClientStatusMetadata::setLimit(const qint32 &limit) {
    m_limit = limit;
    m_limit_isSet = true;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_limit_Set() const{
    return m_limit_isSet;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_limit_Valid() const{
    return m_limit_isValid;
}

qint32 OAIUpdateSystem_Models_PagedClientStatusMetadata::getOffset() const {
    return m_offset;
}
void OAIUpdateSystem_Models_PagedClientStatusMetadata::setOffset(const qint32 &offset) {
    m_offset = offset;
    m_offset_isSet = true;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_offset_Set() const{
    return m_offset_isSet;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_offset_Valid() const{
    return m_offset_isValid;
}

QString OAIUpdateSystem_Models_PagedClientStatusMetadata::getReportResultExpected() const {
    return m_report_result_expected;
}
void OAIUpdateSystem_Models_PagedClientStatusMetadata::setReportResultExpected(const QString &report_result_expected) {
    m_report_result_expected = report_result_expected;
    m_report_result_expected_isSet = true;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_report_result_expected_Set() const{
    return m_report_result_expected_isSet;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_report_result_expected_Valid() const{
    return m_report_result_expected_isValid;
}

QString OAIUpdateSystem_Models_PagedClientStatusMetadata::getReportResultLabel() const {
    return m_report_result_label;
}
void OAIUpdateSystem_Models_PagedClientStatusMetadata::setReportResultLabel(const QString &report_result_label) {
    m_report_result_label = report_result_label;
    m_report_result_label_isSet = true;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_report_result_label_Set() const{
    return m_report_result_label_isSet;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_report_result_label_Valid() const{
    return m_report_result_label_isValid;
}

QString OAIUpdateSystem_Models_PagedClientStatusMetadata::getReportValueLabel() const {
    return m_report_value_label;
}
void OAIUpdateSystem_Models_PagedClientStatusMetadata::setReportValueLabel(const QString &report_value_label) {
    m_report_value_label = report_value_label;
    m_report_value_label_isSet = true;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_report_value_label_Set() const{
    return m_report_value_label_isSet;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_report_value_label_Valid() const{
    return m_report_value_label_isValid;
}

qint32 OAIUpdateSystem_Models_PagedClientStatusMetadata::getTotalCount() const {
    return m_total_count;
}
void OAIUpdateSystem_Models_PagedClientStatusMetadata::setTotalCount(const qint32 &total_count) {
    m_total_count = total_count;
    m_total_count_isSet = true;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_total_count_Set() const{
    return m_total_count_isSet;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::is_total_count_Valid() const{
    return m_total_count_isValid;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offset_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_result_expected_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_result_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_value_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateSystem_Models_PagedClientStatusMetadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_limit_isValid && m_offset_isValid && m_report_result_expected_isValid && m_report_result_label_isValid && m_report_value_label_isValid && m_total_count_isValid && true;
}

} // namespace OpenAPI
