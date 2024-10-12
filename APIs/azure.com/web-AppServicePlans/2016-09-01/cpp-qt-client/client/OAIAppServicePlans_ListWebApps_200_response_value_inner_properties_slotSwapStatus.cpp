/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::initializeModel() {

    m_destination_slot_name_isSet = false;
    m_destination_slot_name_isValid = false;

    m_source_slot_name_isSet = false;
    m_source_slot_name_isValid = false;

    m_timestamp_utc_isSet = false;
    m_timestamp_utc_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::fromJsonObject(QJsonObject json) {

    m_destination_slot_name_isValid = ::OpenAPI::fromJsonValue(m_destination_slot_name, json[QString("destinationSlotName")]);
    m_destination_slot_name_isSet = !json[QString("destinationSlotName")].isNull() && m_destination_slot_name_isValid;

    m_source_slot_name_isValid = ::OpenAPI::fromJsonValue(m_source_slot_name, json[QString("sourceSlotName")]);
    m_source_slot_name_isSet = !json[QString("sourceSlotName")].isNull() && m_source_slot_name_isValid;

    m_timestamp_utc_isValid = ::OpenAPI::fromJsonValue(m_timestamp_utc, json[QString("timestampUtc")]);
    m_timestamp_utc_isSet = !json[QString("timestampUtc")].isNull() && m_timestamp_utc_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::asJsonObject() const {
    QJsonObject obj;
    if (m_destination_slot_name_isSet) {
        obj.insert(QString("destinationSlotName"), ::OpenAPI::toJsonValue(m_destination_slot_name));
    }
    if (m_source_slot_name_isSet) {
        obj.insert(QString("sourceSlotName"), ::OpenAPI::toJsonValue(m_source_slot_name));
    }
    if (m_timestamp_utc_isSet) {
        obj.insert(QString("timestampUtc"), ::OpenAPI::toJsonValue(m_timestamp_utc));
    }
    return obj;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::getDestinationSlotName() const {
    return m_destination_slot_name;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::setDestinationSlotName(const QString &destination_slot_name) {
    m_destination_slot_name = destination_slot_name;
    m_destination_slot_name_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::is_destination_slot_name_Set() const{
    return m_destination_slot_name_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::is_destination_slot_name_Valid() const{
    return m_destination_slot_name_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::getSourceSlotName() const {
    return m_source_slot_name;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::setSourceSlotName(const QString &source_slot_name) {
    m_source_slot_name = source_slot_name;
    m_source_slot_name_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::is_source_slot_name_Set() const{
    return m_source_slot_name_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::is_source_slot_name_Valid() const{
    return m_source_slot_name_isValid;
}

QDateTime OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::getTimestampUtc() const {
    return m_timestamp_utc;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::setTimestampUtc(const QDateTime &timestamp_utc) {
    m_timestamp_utc = timestamp_utc;
    m_timestamp_utc_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::is_timestamp_utc_Set() const{
    return m_timestamp_utc_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::is_timestamp_utc_Valid() const{
    return m_timestamp_utc_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_destination_slot_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_slot_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_utc_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_slotSwapStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
