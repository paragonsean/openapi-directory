/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDictionaries.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDictionaries::OAIDictionaries(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDictionaries::OAIDictionaries() {
    this->initializeModel();
}

OAIDictionaries::~OAIDictionaries() {}

void OAIDictionaries::initializeModel() {

    m_aircraft_isSet = false;
    m_aircraft_isValid = false;

    m_carriers_isSet = false;
    m_carriers_isValid = false;

    m_currencies_isSet = false;
    m_currencies_isValid = false;

    m_locations_isSet = false;
    m_locations_isValid = false;
}

void OAIDictionaries::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDictionaries::fromJsonObject(QJsonObject json) {

    m_aircraft_isValid = ::OpenAPI::fromJsonValue(m_aircraft, json[QString("aircraft")]);
    m_aircraft_isSet = !json[QString("aircraft")].isNull() && m_aircraft_isValid;

    m_carriers_isValid = ::OpenAPI::fromJsonValue(m_carriers, json[QString("carriers")]);
    m_carriers_isSet = !json[QString("carriers")].isNull() && m_carriers_isValid;

    m_currencies_isValid = ::OpenAPI::fromJsonValue(m_currencies, json[QString("currencies")]);
    m_currencies_isSet = !json[QString("currencies")].isNull() && m_currencies_isValid;

    m_locations_isValid = ::OpenAPI::fromJsonValue(m_locations, json[QString("locations")]);
    m_locations_isSet = !json[QString("locations")].isNull() && m_locations_isValid;
}

QString OAIDictionaries::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDictionaries::asJsonObject() const {
    QJsonObject obj;
    if (m_aircraft.size() > 0) {
        obj.insert(QString("aircraft"), ::OpenAPI::toJsonValue(m_aircraft));
    }
    if (m_carriers.size() > 0) {
        obj.insert(QString("carriers"), ::OpenAPI::toJsonValue(m_carriers));
    }
    if (m_currencies.size() > 0) {
        obj.insert(QString("currencies"), ::OpenAPI::toJsonValue(m_currencies));
    }
    if (m_locations.size() > 0) {
        obj.insert(QString("locations"), ::OpenAPI::toJsonValue(m_locations));
    }
    return obj;
}

QMap<QString, QString> OAIDictionaries::getAircraft() const {
    return m_aircraft;
}
void OAIDictionaries::setAircraft(const QMap<QString, QString> &aircraft) {
    m_aircraft = aircraft;
    m_aircraft_isSet = true;
}

bool OAIDictionaries::is_aircraft_Set() const{
    return m_aircraft_isSet;
}

bool OAIDictionaries::is_aircraft_Valid() const{
    return m_aircraft_isValid;
}

QMap<QString, QString> OAIDictionaries::getCarriers() const {
    return m_carriers;
}
void OAIDictionaries::setCarriers(const QMap<QString, QString> &carriers) {
    m_carriers = carriers;
    m_carriers_isSet = true;
}

bool OAIDictionaries::is_carriers_Set() const{
    return m_carriers_isSet;
}

bool OAIDictionaries::is_carriers_Valid() const{
    return m_carriers_isValid;
}

QMap<QString, QString> OAIDictionaries::getCurrencies() const {
    return m_currencies;
}
void OAIDictionaries::setCurrencies(const QMap<QString, QString> &currencies) {
    m_currencies = currencies;
    m_currencies_isSet = true;
}

bool OAIDictionaries::is_currencies_Set() const{
    return m_currencies_isSet;
}

bool OAIDictionaries::is_currencies_Valid() const{
    return m_currencies_isValid;
}

QMap<QString, OAILocationValue> OAIDictionaries::getLocations() const {
    return m_locations;
}
void OAIDictionaries::setLocations(const QMap<QString, OAILocationValue> &locations) {
    m_locations = locations;
    m_locations_isSet = true;
}

bool OAIDictionaries::is_locations_Set() const{
    return m_locations_isSet;
}

bool OAIDictionaries::is_locations_Valid() const{
    return m_locations_isValid;
}

bool OAIDictionaries::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aircraft.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_carriers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_currencies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_locations.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDictionaries::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
