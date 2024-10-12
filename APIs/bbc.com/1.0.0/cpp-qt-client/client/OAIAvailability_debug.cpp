/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAvailability_debug.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAvailability_debug::OAIAvailability_debug(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAvailability_debug::OAIAvailability_debug() {
    this->initializeModel();
}

OAIAvailability_debug::~OAIAvailability_debug() {}

void OAIAvailability_debug::initializeModel() {

    m_availability_of_isSet = false;
    m_availability_of_isValid = false;

    m_media_profile_groups_isSet = false;
    m_media_profile_groups_isValid = false;

    m_service_isSet = false;
    m_service_isValid = false;

    m_territory_isSet = false;
    m_territory_isValid = false;
}

void OAIAvailability_debug::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAvailability_debug::fromJsonObject(QJsonObject json) {

    m_availability_of_isValid = ::OpenAPI::fromJsonValue(m_availability_of, json[QString("availability_of")]);
    m_availability_of_isSet = !json[QString("availability_of")].isNull() && m_availability_of_isValid;

    m_media_profile_groups_isValid = ::OpenAPI::fromJsonValue(m_media_profile_groups, json[QString("media_profile_groups")]);
    m_media_profile_groups_isSet = !json[QString("media_profile_groups")].isNull() && m_media_profile_groups_isValid;

    m_service_isValid = ::OpenAPI::fromJsonValue(m_service, json[QString("service")]);
    m_service_isSet = !json[QString("service")].isNull() && m_service_isValid;

    m_territory_isValid = ::OpenAPI::fromJsonValue(m_territory, json[QString("territory")]);
    m_territory_isSet = !json[QString("territory")].isNull() && m_territory_isValid;
}

QString OAIAvailability_debug::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAvailability_debug::asJsonObject() const {
    QJsonObject obj;
    if (m_availability_of.isSet()) {
        obj.insert(QString("availability_of"), ::OpenAPI::toJsonValue(m_availability_of));
    }
    if (m_media_profile_groups.isSet()) {
        obj.insert(QString("media_profile_groups"), ::OpenAPI::toJsonValue(m_media_profile_groups));
    }
    if (m_service.isSet()) {
        obj.insert(QString("service"), ::OpenAPI::toJsonValue(m_service));
    }
    if (m_territory_isSet) {
        obj.insert(QString("territory"), ::OpenAPI::toJsonValue(m_territory));
    }
    return obj;
}

OAIPidReference OAIAvailability_debug::getAvailabilityOf() const {
    return m_availability_of;
}
void OAIAvailability_debug::setAvailabilityOf(const OAIPidReference &availability_of) {
    m_availability_of = availability_of;
    m_availability_of_isSet = true;
}

bool OAIAvailability_debug::is_availability_of_Set() const{
    return m_availability_of_isSet;
}

bool OAIAvailability_debug::is_availability_of_Valid() const{
    return m_availability_of_isValid;
}

OAIMedia_profile_groups OAIAvailability_debug::getMediaProfileGroups() const {
    return m_media_profile_groups;
}
void OAIAvailability_debug::setMediaProfileGroups(const OAIMedia_profile_groups &media_profile_groups) {
    m_media_profile_groups = media_profile_groups;
    m_media_profile_groups_isSet = true;
}

bool OAIAvailability_debug::is_media_profile_groups_Set() const{
    return m_media_profile_groups_isSet;
}

bool OAIAvailability_debug::is_media_profile_groups_Valid() const{
    return m_media_profile_groups_isValid;
}

OAIServiceReference OAIAvailability_debug::getService() const {
    return m_service;
}
void OAIAvailability_debug::setService(const OAIServiceReference &service) {
    m_service = service;
    m_service_isSet = true;
}

bool OAIAvailability_debug::is_service_Set() const{
    return m_service_isSet;
}

bool OAIAvailability_debug::is_service_Valid() const{
    return m_service_isValid;
}

QString OAIAvailability_debug::getTerritory() const {
    return m_territory;
}
void OAIAvailability_debug::setTerritory(const QString &territory) {
    m_territory = territory;
    m_territory_isSet = true;
}

bool OAIAvailability_debug::is_territory_Set() const{
    return m_territory_isSet;
}

bool OAIAvailability_debug::is_territory_Valid() const{
    return m_territory_isValid;
}

bool OAIAvailability_debug::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_availability_of.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_media_profile_groups.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_service.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_territory_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAvailability_debug::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_availability_of_isValid && true;
}

} // namespace OpenAPI
