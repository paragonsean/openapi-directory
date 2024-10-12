/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILocationWarnings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILocationWarnings::OAILocationWarnings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILocationWarnings::OAILocationWarnings() {
    this->initializeModel();
}

OAILocationWarnings::~OAILocationWarnings() {}

void OAILocationWarnings::initializeModel() {

    m_entity_id_isSet = false;
    m_entity_id_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_warnings_isSet = false;
    m_warnings_isValid = false;
}

void OAILocationWarnings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILocationWarnings::fromJsonObject(QJsonObject json) {

    m_entity_id_isValid = ::OpenAPI::fromJsonValue(m_entity_id, json[QString("entity_id")]);
    m_entity_id_isSet = !json[QString("entity_id")].isNull() && m_entity_id_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_warnings_isValid = ::OpenAPI::fromJsonValue(m_warnings, json[QString("warnings")]);
    m_warnings_isSet = !json[QString("warnings")].isNull() && m_warnings_isValid;
}

QString OAILocationWarnings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILocationWarnings::asJsonObject() const {
    QJsonObject obj;
    if (m_entity_id_isSet) {
        obj.insert(QString("entity_id"), ::OpenAPI::toJsonValue(m_entity_id));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_warnings.size() > 0) {
        obj.insert(QString("warnings"), ::OpenAPI::toJsonValue(m_warnings));
    }
    return obj;
}

qint64 OAILocationWarnings::getEntityId() const {
    return m_entity_id;
}
void OAILocationWarnings::setEntityId(const qint64 &entity_id) {
    m_entity_id = entity_id;
    m_entity_id_isSet = true;
}

bool OAILocationWarnings::is_entity_id_Set() const{
    return m_entity_id_isSet;
}

bool OAILocationWarnings::is_entity_id_Valid() const{
    return m_entity_id_isValid;
}

QString OAILocationWarnings::getLocation() const {
    return m_location;
}
void OAILocationWarnings::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAILocationWarnings::is_location_Set() const{
    return m_location_isSet;
}

bool OAILocationWarnings::is_location_Valid() const{
    return m_location_isValid;
}

QList<QString> OAILocationWarnings::getWarnings() const {
    return m_warnings;
}
void OAILocationWarnings::setWarnings(const QList<QString> &warnings) {
    m_warnings = warnings;
    m_warnings_isSet = true;
}

bool OAILocationWarnings::is_warnings_Set() const{
    return m_warnings_isSet;
}

bool OAILocationWarnings::is_warnings_Valid() const{
    return m_warnings_isValid;
}

bool OAILocationWarnings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_entity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_warnings.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILocationWarnings::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_entity_id_isValid && m_location_isValid && m_warnings_isValid && true;
}

} // namespace OpenAPI
