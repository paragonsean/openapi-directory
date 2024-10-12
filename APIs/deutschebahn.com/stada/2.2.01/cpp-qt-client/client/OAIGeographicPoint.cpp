/**
 * Stationsdatenbereitstellung
 * An API providing master data for German railway stations by DB Station&Service AG.
 *
 * The version of the OpenAPI document: 2.2.01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGeographicPoint.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGeographicPoint::OAIGeographicPoint(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGeographicPoint::OAIGeographicPoint() {
    this->initializeModel();
}

OAIGeographicPoint::~OAIGeographicPoint() {}

void OAIGeographicPoint::initializeModel() {

    m_coordinates_isSet = false;
    m_coordinates_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIGeographicPoint::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGeographicPoint::fromJsonObject(QJsonObject json) {

    m_coordinates_isValid = ::OpenAPI::fromJsonValue(m_coordinates, json[QString("coordinates")]);
    m_coordinates_isSet = !json[QString("coordinates")].isNull() && m_coordinates_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIGeographicPoint::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGeographicPoint::asJsonObject() const {
    QJsonObject obj;
    if (m_coordinates.size() > 0) {
        obj.insert(QString("coordinates"), ::OpenAPI::toJsonValue(m_coordinates));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<double> OAIGeographicPoint::getCoordinates() const {
    return m_coordinates;
}
void OAIGeographicPoint::setCoordinates(const QList<double> &coordinates) {
    m_coordinates = coordinates;
    m_coordinates_isSet = true;
}

bool OAIGeographicPoint::is_coordinates_Set() const{
    return m_coordinates_isSet;
}

bool OAIGeographicPoint::is_coordinates_Valid() const{
    return m_coordinates_isValid;
}

QString OAIGeographicPoint::getType() const {
    return m_type;
}
void OAIGeographicPoint::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGeographicPoint::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGeographicPoint::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIGeographicPoint::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_coordinates.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGeographicPoint::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
