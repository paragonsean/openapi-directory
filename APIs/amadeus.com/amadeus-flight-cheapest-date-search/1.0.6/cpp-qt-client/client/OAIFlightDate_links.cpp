/**
 * Flight Cheapest Date Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.6
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFlightDate_links.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlightDate_links::OAIFlightDate_links(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlightDate_links::OAIFlightDate_links() {
    this->initializeModel();
}

OAIFlightDate_links::~OAIFlightDate_links() {}

void OAIFlightDate_links::initializeModel() {

    m_flight_destinations_isSet = false;
    m_flight_destinations_isValid = false;

    m_flight_offers_isSet = false;
    m_flight_offers_isValid = false;
}

void OAIFlightDate_links::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlightDate_links::fromJsonObject(QJsonObject json) {

    m_flight_destinations_isValid = ::OpenAPI::fromJsonValue(m_flight_destinations, json[QString("flightDestinations")]);
    m_flight_destinations_isSet = !json[QString("flightDestinations")].isNull() && m_flight_destinations_isValid;

    m_flight_offers_isValid = ::OpenAPI::fromJsonValue(m_flight_offers, json[QString("flightOffers")]);
    m_flight_offers_isSet = !json[QString("flightOffers")].isNull() && m_flight_offers_isValid;
}

QString OAIFlightDate_links::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlightDate_links::asJsonObject() const {
    QJsonObject obj;
    if (m_flight_destinations_isSet) {
        obj.insert(QString("flightDestinations"), ::OpenAPI::toJsonValue(m_flight_destinations));
    }
    if (m_flight_offers_isSet) {
        obj.insert(QString("flightOffers"), ::OpenAPI::toJsonValue(m_flight_offers));
    }
    return obj;
}

QString OAIFlightDate_links::getFlightDestinations() const {
    return m_flight_destinations;
}
void OAIFlightDate_links::setFlightDestinations(const QString &flight_destinations) {
    m_flight_destinations = flight_destinations;
    m_flight_destinations_isSet = true;
}

bool OAIFlightDate_links::is_flight_destinations_Set() const{
    return m_flight_destinations_isSet;
}

bool OAIFlightDate_links::is_flight_destinations_Valid() const{
    return m_flight_destinations_isValid;
}

QString OAIFlightDate_links::getFlightOffers() const {
    return m_flight_offers;
}
void OAIFlightDate_links::setFlightOffers(const QString &flight_offers) {
    m_flight_offers = flight_offers;
    m_flight_offers_isSet = true;
}

bool OAIFlightDate_links::is_flight_offers_Set() const{
    return m_flight_offers_isSet;
}

bool OAIFlightDate_links::is_flight_offers_Valid() const{
    return m_flight_offers_isValid;
}

bool OAIFlightDate_links::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_flight_destinations_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flight_offers_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFlightDate_links::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
