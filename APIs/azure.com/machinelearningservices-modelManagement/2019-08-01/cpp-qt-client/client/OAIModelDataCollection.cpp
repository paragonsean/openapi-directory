/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIModelDataCollection.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIModelDataCollection::OAIModelDataCollection(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIModelDataCollection::OAIModelDataCollection() {
    this->initializeModel();
}

OAIModelDataCollection::~OAIModelDataCollection() {}

void OAIModelDataCollection::initializeModel() {

    m_event_hub_enabled_isSet = false;
    m_event_hub_enabled_isValid = false;

    m_storage_enabled_isSet = false;
    m_storage_enabled_isValid = false;
}

void OAIModelDataCollection::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIModelDataCollection::fromJsonObject(QJsonObject json) {

    m_event_hub_enabled_isValid = ::OpenAPI::fromJsonValue(m_event_hub_enabled, json[QString("eventHubEnabled")]);
    m_event_hub_enabled_isSet = !json[QString("eventHubEnabled")].isNull() && m_event_hub_enabled_isValid;

    m_storage_enabled_isValid = ::OpenAPI::fromJsonValue(m_storage_enabled, json[QString("storageEnabled")]);
    m_storage_enabled_isSet = !json[QString("storageEnabled")].isNull() && m_storage_enabled_isValid;
}

QString OAIModelDataCollection::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIModelDataCollection::asJsonObject() const {
    QJsonObject obj;
    if (m_event_hub_enabled_isSet) {
        obj.insert(QString("eventHubEnabled"), ::OpenAPI::toJsonValue(m_event_hub_enabled));
    }
    if (m_storage_enabled_isSet) {
        obj.insert(QString("storageEnabled"), ::OpenAPI::toJsonValue(m_storage_enabled));
    }
    return obj;
}

bool OAIModelDataCollection::isEventHubEnabled() const {
    return m_event_hub_enabled;
}
void OAIModelDataCollection::setEventHubEnabled(const bool &event_hub_enabled) {
    m_event_hub_enabled = event_hub_enabled;
    m_event_hub_enabled_isSet = true;
}

bool OAIModelDataCollection::is_event_hub_enabled_Set() const{
    return m_event_hub_enabled_isSet;
}

bool OAIModelDataCollection::is_event_hub_enabled_Valid() const{
    return m_event_hub_enabled_isValid;
}

bool OAIModelDataCollection::isStorageEnabled() const {
    return m_storage_enabled;
}
void OAIModelDataCollection::setStorageEnabled(const bool &storage_enabled) {
    m_storage_enabled = storage_enabled;
    m_storage_enabled_isSet = true;
}

bool OAIModelDataCollection::is_storage_enabled_Set() const{
    return m_storage_enabled_isSet;
}

bool OAIModelDataCollection::is_storage_enabled_Valid() const{
    return m_storage_enabled_isValid;
}

bool OAIModelDataCollection::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_event_hub_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_storage_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIModelDataCollection::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
