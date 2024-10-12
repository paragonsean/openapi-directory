/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetFlightOffersQuery.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetFlightOffersQuery::OAIGetFlightOffersQuery(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetFlightOffersQuery::OAIGetFlightOffersQuery() {
    this->initializeModel();
}

OAIGetFlightOffersQuery::~OAIGetFlightOffersQuery() {}

void OAIGetFlightOffersQuery::initializeModel() {

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_origin_destinations_isSet = false;
    m_origin_destinations_isValid = false;

    m_search_criteria_isSet = false;
    m_search_criteria_isValid = false;

    m_sources_isSet = false;
    m_sources_isValid = false;

    m_travelers_isSet = false;
    m_travelers_isValid = false;
}

void OAIGetFlightOffersQuery::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetFlightOffersQuery::fromJsonObject(QJsonObject json) {

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("currencyCode")]);
    m_currency_code_isSet = !json[QString("currencyCode")].isNull() && m_currency_code_isValid;

    m_origin_destinations_isValid = ::OpenAPI::fromJsonValue(m_origin_destinations, json[QString("originDestinations")]);
    m_origin_destinations_isSet = !json[QString("originDestinations")].isNull() && m_origin_destinations_isValid;

    m_search_criteria_isValid = ::OpenAPI::fromJsonValue(m_search_criteria, json[QString("searchCriteria")]);
    m_search_criteria_isSet = !json[QString("searchCriteria")].isNull() && m_search_criteria_isValid;

    m_sources_isValid = ::OpenAPI::fromJsonValue(m_sources, json[QString("sources")]);
    m_sources_isSet = !json[QString("sources")].isNull() && m_sources_isValid;

    m_travelers_isValid = ::OpenAPI::fromJsonValue(m_travelers, json[QString("travelers")]);
    m_travelers_isSet = !json[QString("travelers")].isNull() && m_travelers_isValid;
}

QString OAIGetFlightOffersQuery::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetFlightOffersQuery::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_code_isSet) {
        obj.insert(QString("currencyCode"), ::OpenAPI::toJsonValue(m_currency_code));
    }
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

QString OAIGetFlightOffersQuery::getCurrencyCode() const {
    return m_currency_code;
}
void OAIGetFlightOffersQuery::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAIGetFlightOffersQuery::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAIGetFlightOffersQuery::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

QList<OAIOriginDestination> OAIGetFlightOffersQuery::getOriginDestinations() const {
    return m_origin_destinations;
}
void OAIGetFlightOffersQuery::setOriginDestinations(const QList<OAIOriginDestination> &origin_destinations) {
    m_origin_destinations = origin_destinations;
    m_origin_destinations_isSet = true;
}

bool OAIGetFlightOffersQuery::is_origin_destinations_Set() const{
    return m_origin_destinations_isSet;
}

bool OAIGetFlightOffersQuery::is_origin_destinations_Valid() const{
    return m_origin_destinations_isValid;
}

OAISearchCriteria OAIGetFlightOffersQuery::getSearchCriteria() const {
    return m_search_criteria;
}
void OAIGetFlightOffersQuery::setSearchCriteria(const OAISearchCriteria &search_criteria) {
    m_search_criteria = search_criteria;
    m_search_criteria_isSet = true;
}

bool OAIGetFlightOffersQuery::is_search_criteria_Set() const{
    return m_search_criteria_isSet;
}

bool OAIGetFlightOffersQuery::is_search_criteria_Valid() const{
    return m_search_criteria_isValid;
}

QList<OAIFlightOfferSource> OAIGetFlightOffersQuery::getSources() const {
    return m_sources;
}
void OAIGetFlightOffersQuery::setSources(const QList<OAIFlightOfferSource> &sources) {
    m_sources = sources;
    m_sources_isSet = true;
}

bool OAIGetFlightOffersQuery::is_sources_Set() const{
    return m_sources_isSet;
}

bool OAIGetFlightOffersQuery::is_sources_Valid() const{
    return m_sources_isValid;
}

QList<OAITraveler> OAIGetFlightOffersQuery::getTravelers() const {
    return m_travelers;
}
void OAIGetFlightOffersQuery::setTravelers(const QList<OAITraveler> &travelers) {
    m_travelers = travelers;
    m_travelers_isSet = true;
}

bool OAIGetFlightOffersQuery::is_travelers_Set() const{
    return m_travelers_isSet;
}

bool OAIGetFlightOffersQuery::is_travelers_Valid() const{
    return m_travelers_isValid;
}

bool OAIGetFlightOffersQuery::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

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

bool OAIGetFlightOffersQuery::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_origin_destinations_isValid && m_sources_isValid && m_travelers_isValid && true;
}

} // namespace OpenAPI
