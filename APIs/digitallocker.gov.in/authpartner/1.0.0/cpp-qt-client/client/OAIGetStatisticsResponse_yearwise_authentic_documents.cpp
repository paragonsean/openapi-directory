/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetStatisticsResponse_yearwise_authentic_documents.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetStatisticsResponse_yearwise_authentic_documents::OAIGetStatisticsResponse_yearwise_authentic_documents(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetStatisticsResponse_yearwise_authentic_documents::OAIGetStatisticsResponse_yearwise_authentic_documents() {
    this->initializeModel();
}

OAIGetStatisticsResponse_yearwise_authentic_documents::~OAIGetStatisticsResponse_yearwise_authentic_documents() {}

void OAIGetStatisticsResponse_yearwise_authentic_documents::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_details1_isSet = false;
    m_details1_isValid = false;

    m_details2_isSet = false;
    m_details2_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_year_isSet = false;
    m_year_isValid = false;
}

void OAIGetStatisticsResponse_yearwise_authentic_documents::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetStatisticsResponse_yearwise_authentic_documents::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_details1_isValid = ::OpenAPI::fromJsonValue(m_details1, json[QString("details1")]);
    m_details1_isSet = !json[QString("details1")].isNull() && m_details1_isValid;

    m_details2_isValid = ::OpenAPI::fromJsonValue(m_details2, json[QString("details2")]);
    m_details2_isSet = !json[QString("details2")].isNull() && m_details2_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_year_isValid = ::OpenAPI::fromJsonValue(m_year, json[QString("year")]);
    m_year_isSet = !json[QString("year")].isNull() && m_year_isValid;
}

QString OAIGetStatisticsResponse_yearwise_authentic_documents::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetStatisticsResponse_yearwise_authentic_documents::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_details.isSet()) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_details1.isSet()) {
        obj.insert(QString("details1"), ::OpenAPI::toJsonValue(m_details1));
    }
    if (m_details2.isSet()) {
        obj.insert(QString("details2"), ::OpenAPI::toJsonValue(m_details2));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_year_isSet) {
        obj.insert(QString("year"), ::OpenAPI::toJsonValue(m_year));
    }
    return obj;
}

qint32 OAIGetStatisticsResponse_yearwise_authentic_documents::getCount() const {
    return m_count;
}
void OAIGetStatisticsResponse_yearwise_authentic_documents::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_count_Set() const{
    return m_count_isSet;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_count_Valid() const{
    return m_count_isValid;
}

OAIGetStatisticsResponse_yearwise_authentic_documents_details OAIGetStatisticsResponse_yearwise_authentic_documents::getDetails() const {
    return m_details;
}
void OAIGetStatisticsResponse_yearwise_authentic_documents::setDetails(const OAIGetStatisticsResponse_yearwise_authentic_documents_details &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_details_Set() const{
    return m_details_isSet;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_details_Valid() const{
    return m_details_isValid;
}

OAIGetStatisticsResponse_yearwise_authentic_documents_details1 OAIGetStatisticsResponse_yearwise_authentic_documents::getDetails1() const {
    return m_details1;
}
void OAIGetStatisticsResponse_yearwise_authentic_documents::setDetails1(const OAIGetStatisticsResponse_yearwise_authentic_documents_details1 &details1) {
    m_details1 = details1;
    m_details1_isSet = true;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_details1_Set() const{
    return m_details1_isSet;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_details1_Valid() const{
    return m_details1_isValid;
}

OAIGetStatisticsResponse_yearwise_authentic_documents_details2 OAIGetStatisticsResponse_yearwise_authentic_documents::getDetails2() const {
    return m_details2;
}
void OAIGetStatisticsResponse_yearwise_authentic_documents::setDetails2(const OAIGetStatisticsResponse_yearwise_authentic_documents_details2 &details2) {
    m_details2 = details2;
    m_details2_isSet = true;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_details2_Set() const{
    return m_details2_isSet;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_details2_Valid() const{
    return m_details2_isValid;
}

qint32 OAIGetStatisticsResponse_yearwise_authentic_documents::getId() const {
    return m_id;
}
void OAIGetStatisticsResponse_yearwise_authentic_documents::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIGetStatisticsResponse_yearwise_authentic_documents::getYear() const {
    return m_year;
}
void OAIGetStatisticsResponse_yearwise_authentic_documents::setYear(const qint32 &year) {
    m_year = year;
    m_year_isSet = true;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_year_Set() const{
    return m_year_isSet;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::is_year_Valid() const{
    return m_year_isValid;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_details1.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_details2.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetStatisticsResponse_yearwise_authentic_documents::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
