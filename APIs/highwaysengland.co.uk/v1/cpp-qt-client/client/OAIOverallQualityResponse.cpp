/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOverallQualityResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOverallQualityResponse::OAIOverallQualityResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOverallQualityResponse::OAIOverallQualityResponse() {
    this->initializeModel();
}

OAIOverallQualityResponse::~OAIOverallQualityResponse() {}

void OAIOverallQualityResponse::initializeModel() {

    m_data_quality_isSet = false;
    m_data_quality_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_row_count_isSet = false;
    m_row_count_isValid = false;

    m_sites_isSet = false;
    m_sites_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;
}

void OAIOverallQualityResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOverallQualityResponse::fromJsonObject(QJsonObject json) {

    m_data_quality_isValid = ::OpenAPI::fromJsonValue(m_data_quality, json[QString("data_quality")]);
    m_data_quality_isSet = !json[QString("data_quality")].isNull() && m_data_quality_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_row_count_isValid = ::OpenAPI::fromJsonValue(m_row_count, json[QString("row_count")]);
    m_row_count_isSet = !json[QString("row_count")].isNull() && m_row_count_isValid;

    m_sites_isValid = ::OpenAPI::fromJsonValue(m_sites, json[QString("sites")]);
    m_sites_isSet = !json[QString("sites")].isNull() && m_sites_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;
}

QString OAIOverallQualityResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOverallQualityResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_data_quality_isSet) {
        obj.insert(QString("data_quality"), ::OpenAPI::toJsonValue(m_data_quality));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_row_count_isSet) {
        obj.insert(QString("row_count"), ::OpenAPI::toJsonValue(m_row_count));
    }
    if (m_sites_isSet) {
        obj.insert(QString("sites"), ::OpenAPI::toJsonValue(m_sites));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    return obj;
}

qint32 OAIOverallQualityResponse::getDataQuality() const {
    return m_data_quality;
}
void OAIOverallQualityResponse::setDataQuality(const qint32 &data_quality) {
    m_data_quality = data_quality;
    m_data_quality_isSet = true;
}

bool OAIOverallQualityResponse::is_data_quality_Set() const{
    return m_data_quality_isSet;
}

bool OAIOverallQualityResponse::is_data_quality_Valid() const{
    return m_data_quality_isValid;
}

QString OAIOverallQualityResponse::getEndDate() const {
    return m_end_date;
}
void OAIOverallQualityResponse::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIOverallQualityResponse::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIOverallQualityResponse::is_end_date_Valid() const{
    return m_end_date_isValid;
}

qint32 OAIOverallQualityResponse::getRowCount() const {
    return m_row_count;
}
void OAIOverallQualityResponse::setRowCount(const qint32 &row_count) {
    m_row_count = row_count;
    m_row_count_isSet = true;
}

bool OAIOverallQualityResponse::is_row_count_Set() const{
    return m_row_count_isSet;
}

bool OAIOverallQualityResponse::is_row_count_Valid() const{
    return m_row_count_isValid;
}

QString OAIOverallQualityResponse::getSites() const {
    return m_sites;
}
void OAIOverallQualityResponse::setSites(const QString &sites) {
    m_sites = sites;
    m_sites_isSet = true;
}

bool OAIOverallQualityResponse::is_sites_Set() const{
    return m_sites_isSet;
}

bool OAIOverallQualityResponse::is_sites_Valid() const{
    return m_sites_isValid;
}

QString OAIOverallQualityResponse::getStartDate() const {
    return m_start_date;
}
void OAIOverallQualityResponse::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIOverallQualityResponse::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIOverallQualityResponse::is_start_date_Valid() const{
    return m_start_date_isValid;
}

bool OAIOverallQualityResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_quality_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sites_isSet) {
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

bool OAIOverallQualityResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
