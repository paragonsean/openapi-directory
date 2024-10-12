/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOriginDestinationLight.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOriginDestinationLight::OAIOriginDestinationLight(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOriginDestinationLight::OAIOriginDestinationLight() {
    this->initializeModel();
}

OAIOriginDestinationLight::~OAIOriginDestinationLight() {}

void OAIOriginDestinationLight::initializeModel() {

    m_destination_location_code_isSet = false;
    m_destination_location_code_isValid = false;

    m_excluded_connection_points_isSet = false;
    m_excluded_connection_points_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_included_connection_points_isSet = false;
    m_included_connection_points_isValid = false;

    m_origin_location_code_isSet = false;
    m_origin_location_code_isValid = false;
}

void OAIOriginDestinationLight::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOriginDestinationLight::fromJsonObject(QJsonObject json) {

    m_destination_location_code_isValid = ::OpenAPI::fromJsonValue(m_destination_location_code, json[QString("destinationLocationCode")]);
    m_destination_location_code_isSet = !json[QString("destinationLocationCode")].isNull() && m_destination_location_code_isValid;

    m_excluded_connection_points_isValid = ::OpenAPI::fromJsonValue(m_excluded_connection_points, json[QString("excludedConnectionPoints")]);
    m_excluded_connection_points_isSet = !json[QString("excludedConnectionPoints")].isNull() && m_excluded_connection_points_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_included_connection_points_isValid = ::OpenAPI::fromJsonValue(m_included_connection_points, json[QString("includedConnectionPoints")]);
    m_included_connection_points_isSet = !json[QString("includedConnectionPoints")].isNull() && m_included_connection_points_isValid;

    m_origin_location_code_isValid = ::OpenAPI::fromJsonValue(m_origin_location_code, json[QString("originLocationCode")]);
    m_origin_location_code_isSet = !json[QString("originLocationCode")].isNull() && m_origin_location_code_isValid;
}

QString OAIOriginDestinationLight::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOriginDestinationLight::asJsonObject() const {
    QJsonObject obj;
    if (m_destination_location_code_isSet) {
        obj.insert(QString("destinationLocationCode"), ::OpenAPI::toJsonValue(m_destination_location_code));
    }
    if (m_excluded_connection_points.size() > 0) {
        obj.insert(QString("excludedConnectionPoints"), ::OpenAPI::toJsonValue(m_excluded_connection_points));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_included_connection_points.size() > 0) {
        obj.insert(QString("includedConnectionPoints"), ::OpenAPI::toJsonValue(m_included_connection_points));
    }
    if (m_origin_location_code_isSet) {
        obj.insert(QString("originLocationCode"), ::OpenAPI::toJsonValue(m_origin_location_code));
    }
    return obj;
}

QString OAIOriginDestinationLight::getDestinationLocationCode() const {
    return m_destination_location_code;
}
void OAIOriginDestinationLight::setDestinationLocationCode(const QString &destination_location_code) {
    m_destination_location_code = destination_location_code;
    m_destination_location_code_isSet = true;
}

bool OAIOriginDestinationLight::is_destination_location_code_Set() const{
    return m_destination_location_code_isSet;
}

bool OAIOriginDestinationLight::is_destination_location_code_Valid() const{
    return m_destination_location_code_isValid;
}

QList<QString> OAIOriginDestinationLight::getExcludedConnectionPoints() const {
    return m_excluded_connection_points;
}
void OAIOriginDestinationLight::setExcludedConnectionPoints(const QList<QString> &excluded_connection_points) {
    m_excluded_connection_points = excluded_connection_points;
    m_excluded_connection_points_isSet = true;
}

bool OAIOriginDestinationLight::is_excluded_connection_points_Set() const{
    return m_excluded_connection_points_isSet;
}

bool OAIOriginDestinationLight::is_excluded_connection_points_Valid() const{
    return m_excluded_connection_points_isValid;
}

QString OAIOriginDestinationLight::getId() const {
    return m_id;
}
void OAIOriginDestinationLight::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOriginDestinationLight::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOriginDestinationLight::is_id_Valid() const{
    return m_id_isValid;
}

QList<QString> OAIOriginDestinationLight::getIncludedConnectionPoints() const {
    return m_included_connection_points;
}
void OAIOriginDestinationLight::setIncludedConnectionPoints(const QList<QString> &included_connection_points) {
    m_included_connection_points = included_connection_points;
    m_included_connection_points_isSet = true;
}

bool OAIOriginDestinationLight::is_included_connection_points_Set() const{
    return m_included_connection_points_isSet;
}

bool OAIOriginDestinationLight::is_included_connection_points_Valid() const{
    return m_included_connection_points_isValid;
}

QString OAIOriginDestinationLight::getOriginLocationCode() const {
    return m_origin_location_code;
}
void OAIOriginDestinationLight::setOriginLocationCode(const QString &origin_location_code) {
    m_origin_location_code = origin_location_code;
    m_origin_location_code_isSet = true;
}

bool OAIOriginDestinationLight::is_origin_location_code_Set() const{
    return m_origin_location_code_isSet;
}

bool OAIOriginDestinationLight::is_origin_location_code_Valid() const{
    return m_origin_location_code_isValid;
}

bool OAIOriginDestinationLight::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_destination_location_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_excluded_connection_points.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_included_connection_points.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_origin_location_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOriginDestinationLight::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
