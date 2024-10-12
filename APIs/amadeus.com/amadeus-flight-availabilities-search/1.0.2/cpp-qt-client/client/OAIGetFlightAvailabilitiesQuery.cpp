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

#include "OAIGetFlightAvailabilitiesQuery.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetFlightAvailabilitiesQuery::OAIGetFlightAvailabilitiesQuery(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetFlightAvailabilitiesQuery::OAIGetFlightAvailabilitiesQuery() {
    this->initializeModel();
}

OAIGetFlightAvailabilitiesQuery::~OAIGetFlightAvailabilitiesQuery() {}

void OAIGetFlightAvailabilitiesQuery::initializeModel() {

    m_origin_destinations_isSet = false;
    m_origin_destinations_isValid = false;

    m_search_criteria_isSet = false;
    m_search_criteria_isValid = false;

    m_sources_isSet = false;
    m_sources_isValid = false;

    m_travelers_isSet = false;
    m_travelers_isValid = false;
}

void OAIGetFlightAvailabilitiesQuery::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetFlightAvailabilitiesQuery::fromJsonObject(QJsonObject json) {

    m_origin_destinations_isValid = ::OpenAPI::fromJsonValue(m_origin_destinations, json[QString("originDestinations")]);
    m_origin_destinations_isSet = !json[QString("originDestinations")].isNull() && m_origin_destinations_isValid;

    m_search_criteria_isValid = ::OpenAPI::fromJsonValue(m_search_criteria, json[QString("searchCriteria")]);
    m_search_criteria_isSet = !json[QString("searchCriteria")].isNull() && m_search_criteria_isValid;

    m_sources_isValid = ::OpenAPI::fromJsonValue(m_sources, json[QString("sources")]);
    m_sources_isSet = !json[QString("sources")].isNull() && m_sources_isValid;

    m_travelers_isValid = ::OpenAPI::fromJsonValue(m_travelers, json[QString("travelers")]);
    m_travelers_isSet = !json[QString("travelers")].isNull() && m_travelers_isValid;
}

QString OAIGetFlightAvailabilitiesQuery::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetFlightAvailabilitiesQuery::asJsonObject() const {
    QJsonObject obj;
    if (m_origin_destinations.size() > 0) {
        obj.insert(QString("originDestinations"), ::OpenAPI::toJsonValue(m_origin_destinations));
    }
    if (m_search_criteria.isSet()) {
        obj.insert(QString("searchCriteria"), ::OpenAPI::toJsonValue(m_search_criteria));
    }
    if (m_sources.size() > 0) {
        obj.insert(QString("sources"), ::OpenAPI::toJsonValue(m_sources));
    }
    if (m_travelers.size() > 0) {
        obj.insert(QString("travelers"), ::OpenAPI::toJsonValue(m_travelers));
    }
    return obj;
}

QList<OAIExtended_OriginDestinationLight> OAIGetFlightAvailabilitiesQuery::getOriginDestinations() const {
    return m_origin_destinations;
}
void OAIGetFlightAvailabilitiesQuery::setOriginDestinations(const QList<OAIExtended_OriginDestinationLight> &origin_destinations) {
    m_origin_destinations = origin_destinations;
    m_origin_destinations_isSet = true;
}

bool OAIGetFlightAvailabilitiesQuery::is_origin_destinations_Set() const{
    return m_origin_destinations_isSet;
}

bool OAIGetFlightAvailabilitiesQuery::is_origin_destinations_Valid() const{
    return m_origin_destinations_isValid;
}

OAIExtended_SearchCriteria OAIGetFlightAvailabilitiesQuery::getSearchCriteria() const {
    return m_search_criteria;
}
void OAIGetFlightAvailabilitiesQuery::setSearchCriteria(const OAIExtended_SearchCriteria &search_criteria) {
    m_search_criteria = search_criteria;
    m_search_criteria_isSet = true;
}

bool OAIGetFlightAvailabilitiesQuery::is_search_criteria_Set() const{
    return m_search_criteria_isSet;
}

bool OAIGetFlightAvailabilitiesQuery::is_search_criteria_Valid() const{
    return m_search_criteria_isValid;
}

QList<OAIFlightOfferSource> OAIGetFlightAvailabilitiesQuery::getSources() const {
    return m_sources;
}
void OAIGetFlightAvailabilitiesQuery::setSources(const QList<OAIFlightOfferSource> &sources) {
    m_sources = sources;
    m_sources_isSet = true;
}

bool OAIGetFlightAvailabilitiesQuery::is_sources_Set() const{
    return m_sources_isSet;
}

bool OAIGetFlightAvailabilitiesQuery::is_sources_Valid() const{
    return m_sources_isValid;
}

QList<OAITravelerInfo> OAIGetFlightAvailabilitiesQuery::getTravelers() const {
    return m_travelers;
}
void OAIGetFlightAvailabilitiesQuery::setTravelers(const QList<OAITravelerInfo> &travelers) {
    m_travelers = travelers;
    m_travelers_isSet = true;
}

bool OAIGetFlightAvailabilitiesQuery::is_travelers_Set() const{
    return m_travelers_isSet;
}

bool OAIGetFlightAvailabilitiesQuery::is_travelers_Valid() const{
    return m_travelers_isValid;
}

bool OAIGetFlightAvailabilitiesQuery::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_origin_destinations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_criteria.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_sources.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_travelers.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetFlightAvailabilitiesQuery::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_origin_destinations_isValid && m_sources_isValid && m_travelers_isValid && true;
}

} // namespace OpenAPI
