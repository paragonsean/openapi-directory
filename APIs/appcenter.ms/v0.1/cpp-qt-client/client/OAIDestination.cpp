/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDestination.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDestination::OAIDestination(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDestination::OAIDestination() {
    this->initializeModel();
}

OAIDestination::~OAIDestination() {}

void OAIDestination::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_is_latest_isSet = false;
    m_is_latest_isValid = false;

    m_publishing_status_isSet = false;
    m_publishing_status_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_destination_type_isSet = false;
    m_destination_type_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;
}

void OAIDestination::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDestination::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_is_latest_isValid = ::OpenAPI::fromJsonValue(m_is_latest, json[QString("is_latest")]);
    m_is_latest_isSet = !json[QString("is_latest")].isNull() && m_is_latest_isValid;

    m_publishing_status_isValid = ::OpenAPI::fromJsonValue(m_publishing_status, json[QString("publishing_status")]);
    m_publishing_status_isSet = !json[QString("publishing_status")].isNull() && m_publishing_status_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_destination_type_isValid = ::OpenAPI::fromJsonValue(m_destination_type, json[QString("destination_type")]);
    m_destination_type_isSet = !json[QString("destination_type")].isNull() && m_destination_type_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("display_name")]);
    m_display_name_isSet = !json[QString("display_name")].isNull() && m_display_name_isValid;
}

QString OAIDestination::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDestination::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_is_latest_isSet) {
        obj.insert(QString("is_latest"), ::OpenAPI::toJsonValue(m_is_latest));
    }
    if (m_publishing_status_isSet) {
        obj.insert(QString("publishing_status"), ::OpenAPI::toJsonValue(m_publishing_status));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_destination_type_isSet) {
        obj.insert(QString("destination_type"), ::OpenAPI::toJsonValue(m_destination_type));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("display_name"), ::OpenAPI::toJsonValue(m_display_name));
    }
    return obj;
}

QString OAIDestination::getId() const {
    return m_id;
}
void OAIDestination::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDestination::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDestination::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIDestination::getName() const {
    return m_name;
}
void OAIDestination::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDestination::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDestination::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIDestination::isIsLatest() const {
    return m_is_latest;
}
void OAIDestination::setIsLatest(const bool &is_latest) {
    m_is_latest = is_latest;
    m_is_latest_isSet = true;
}

bool OAIDestination::is_is_latest_Set() const{
    return m_is_latest_isSet;
}

bool OAIDestination::is_is_latest_Valid() const{
    return m_is_latest_isValid;
}

QString OAIDestination::getPublishingStatus() const {
    return m_publishing_status;
}
void OAIDestination::setPublishingStatus(const QString &publishing_status) {
    m_publishing_status = publishing_status;
    m_publishing_status_isSet = true;
}

bool OAIDestination::is_publishing_status_Set() const{
    return m_publishing_status_isSet;
}

bool OAIDestination::is_publishing_status_Valid() const{
    return m_publishing_status_isValid;
}

QString OAIDestination::getType() const {
    return m_type;
}
void OAIDestination::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIDestination::is_type_Set() const{
    return m_type_isSet;
}

bool OAIDestination::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIDestination::getDestinationType() const {
    return m_destination_type;
}
void OAIDestination::setDestinationType(const QString &destination_type) {
    m_destination_type = destination_type;
    m_destination_type_isSet = true;
}

bool OAIDestination::is_destination_type_Set() const{
    return m_destination_type_isSet;
}

bool OAIDestination::is_destination_type_Valid() const{
    return m_destination_type_isValid;
}

QString OAIDestination::getDisplayName() const {
    return m_display_name;
}
void OAIDestination::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIDestination::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIDestination::is_display_name_Valid() const{
    return m_display_name_isValid;
}

bool OAIDestination::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_latest_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publishing_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_destination_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDestination::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
