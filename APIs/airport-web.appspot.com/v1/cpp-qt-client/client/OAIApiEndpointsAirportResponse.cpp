/**
 * airportsapi
 * Get name and website-URL for airports by ICAO code. Covered airports are mostly in Germany.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApiEndpointsAirportResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApiEndpointsAirportResponse::OAIApiEndpointsAirportResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApiEndpointsAirportResponse::OAIApiEndpointsAirportResponse() {
    this->initializeModel();
}

OAIApiEndpointsAirportResponse::~OAIApiEndpointsAirportResponse() {}

void OAIApiEndpointsAirportResponse::initializeModel() {

    m_icao_isSet = false;
    m_icao_isValid = false;

    m_last_update_isSet = false;
    m_last_update_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIApiEndpointsAirportResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApiEndpointsAirportResponse::fromJsonObject(QJsonObject json) {

    m_icao_isValid = ::OpenAPI::fromJsonValue(m_icao, json[QString("ICAO")]);
    m_icao_isSet = !json[QString("ICAO")].isNull() && m_icao_isValid;

    m_last_update_isValid = ::OpenAPI::fromJsonValue(m_last_update, json[QString("last_update")]);
    m_last_update_isSet = !json[QString("last_update")].isNull() && m_last_update_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIApiEndpointsAirportResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApiEndpointsAirportResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_icao_isSet) {
        obj.insert(QString("ICAO"), ::OpenAPI::toJsonValue(m_icao));
    }
    if (m_last_update_isSet) {
        obj.insert(QString("last_update"), ::OpenAPI::toJsonValue(m_last_update));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

QString OAIApiEndpointsAirportResponse::getIcao() const {
    return m_icao;
}
void OAIApiEndpointsAirportResponse::setIcao(const QString &icao) {
    m_icao = icao;
    m_icao_isSet = true;
}

bool OAIApiEndpointsAirportResponse::is_icao_Set() const{
    return m_icao_isSet;
}

bool OAIApiEndpointsAirportResponse::is_icao_Valid() const{
    return m_icao_isValid;
}

QString OAIApiEndpointsAirportResponse::getLastUpdate() const {
    return m_last_update;
}
void OAIApiEndpointsAirportResponse::setLastUpdate(const QString &last_update) {
    m_last_update = last_update;
    m_last_update_isSet = true;
}

bool OAIApiEndpointsAirportResponse::is_last_update_Set() const{
    return m_last_update_isSet;
}

bool OAIApiEndpointsAirportResponse::is_last_update_Valid() const{
    return m_last_update_isValid;
}

QString OAIApiEndpointsAirportResponse::getName() const {
    return m_name;
}
void OAIApiEndpointsAirportResponse::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIApiEndpointsAirportResponse::is_name_Set() const{
    return m_name_isSet;
}

bool OAIApiEndpointsAirportResponse::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIApiEndpointsAirportResponse::getUrl() const {
    return m_url;
}
void OAIApiEndpointsAirportResponse::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIApiEndpointsAirportResponse::is_url_Set() const{
    return m_url_isSet;
}

bool OAIApiEndpointsAirportResponse::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIApiEndpointsAirportResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_icao_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_update_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApiEndpointsAirportResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
