/**
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITravelerPricing.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITravelerPricing::OAITravelerPricing(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITravelerPricing::OAITravelerPricing() {
    this->initializeModel();
}

OAITravelerPricing::~OAITravelerPricing() {}

void OAITravelerPricing::initializeModel() {

    m_associated_adult_id_isSet = false;
    m_associated_adult_id_isValid = false;

    m_fare_details_by_segment_isSet = false;
    m_fare_details_by_segment_isValid = false;

    m_fare_option_isSet = false;
    m_fare_option_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_traveler_id_isSet = false;
    m_traveler_id_isValid = false;

    m_traveler_type_isSet = false;
    m_traveler_type_isValid = false;
}

void OAITravelerPricing::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITravelerPricing::fromJsonObject(QJsonObject json) {

    m_associated_adult_id_isValid = ::OpenAPI::fromJsonValue(m_associated_adult_id, json[QString("associatedAdultId")]);
    m_associated_adult_id_isSet = !json[QString("associatedAdultId")].isNull() && m_associated_adult_id_isValid;

    m_fare_details_by_segment_isValid = ::OpenAPI::fromJsonValue(m_fare_details_by_segment, json[QString("fareDetailsBySegment")]);
    m_fare_details_by_segment_isSet = !json[QString("fareDetailsBySegment")].isNull() && m_fare_details_by_segment_isValid;

    m_fare_option_isValid = ::OpenAPI::fromJsonValue(m_fare_option, json[QString("fareOption")]);
    m_fare_option_isSet = !json[QString("fareOption")].isNull() && m_fare_option_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_traveler_id_isValid = ::OpenAPI::fromJsonValue(m_traveler_id, json[QString("travelerId")]);
    m_traveler_id_isSet = !json[QString("travelerId")].isNull() && m_traveler_id_isValid;

    m_traveler_type_isValid = ::OpenAPI::fromJsonValue(m_traveler_type, json[QString("travelerType")]);
    m_traveler_type_isSet = !json[QString("travelerType")].isNull() && m_traveler_type_isValid;
}

QString OAITravelerPricing::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITravelerPricing::asJsonObject() const {
    QJsonObject obj;
    if (m_associated_adult_id_isSet) {
        obj.insert(QString("associatedAdultId"), ::OpenAPI::toJsonValue(m_associated_adult_id));
    }
    if (m_fare_details_by_segment.size() > 0) {
        obj.insert(QString("fareDetailsBySegment"), ::OpenAPI::toJsonValue(m_fare_details_by_segment));
    }
    if (m_fare_option.isSet()) {
        obj.insert(QString("fareOption"), ::OpenAPI::toJsonValue(m_fare_option));
    }
    if (m_price.isSet()) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_traveler_id_isSet) {
        obj.insert(QString("travelerId"), ::OpenAPI::toJsonValue(m_traveler_id));
    }
    if (m_traveler_type.isSet()) {
        obj.insert(QString("travelerType"), ::OpenAPI::toJsonValue(m_traveler_type));
    }
    return obj;
}

QString OAITravelerPricing::getAssociatedAdultId() const {
    return m_associated_adult_id;
}
void OAITravelerPricing::setAssociatedAdultId(const QString &associated_adult_id) {
    m_associated_adult_id = associated_adult_id;
    m_associated_adult_id_isSet = true;
}

bool OAITravelerPricing::is_associated_adult_id_Set() const{
    return m_associated_adult_id_isSet;
}

bool OAITravelerPricing::is_associated_adult_id_Valid() const{
    return m_associated_adult_id_isValid;
}

QList<OAIFareDetailsBySegment> OAITravelerPricing::getFareDetailsBySegment() const {
    return m_fare_details_by_segment;
}
void OAITravelerPricing::setFareDetailsBySegment(const QList<OAIFareDetailsBySegment> &fare_details_by_segment) {
    m_fare_details_by_segment = fare_details_by_segment;
    m_fare_details_by_segment_isSet = true;
}

bool OAITravelerPricing::is_fare_details_by_segment_Set() const{
    return m_fare_details_by_segment_isSet;
}

bool OAITravelerPricing::is_fare_details_by_segment_Valid() const{
    return m_fare_details_by_segment_isValid;
}

OAITravelerPricingFareOption OAITravelerPricing::getFareOption() const {
    return m_fare_option;
}
void OAITravelerPricing::setFareOption(const OAITravelerPricingFareOption &fare_option) {
    m_fare_option = fare_option;
    m_fare_option_isSet = true;
}

bool OAITravelerPricing::is_fare_option_Set() const{
    return m_fare_option_isSet;
}

bool OAITravelerPricing::is_fare_option_Valid() const{
    return m_fare_option_isValid;
}

OAIPrice OAITravelerPricing::getPrice() const {
    return m_price;
}
void OAITravelerPricing::setPrice(const OAIPrice &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAITravelerPricing::is_price_Set() const{
    return m_price_isSet;
}

bool OAITravelerPricing::is_price_Valid() const{
    return m_price_isValid;
}

QString OAITravelerPricing::getTravelerId() const {
    return m_traveler_id;
}
void OAITravelerPricing::setTravelerId(const QString &traveler_id) {
    m_traveler_id = traveler_id;
    m_traveler_id_isSet = true;
}

bool OAITravelerPricing::is_traveler_id_Set() const{
    return m_traveler_id_isSet;
}

bool OAITravelerPricing::is_traveler_id_Valid() const{
    return m_traveler_id_isValid;
}

OAITravelerType OAITravelerPricing::getTravelerType() const {
    return m_traveler_type;
}
void OAITravelerPricing::setTravelerType(const OAITravelerType &traveler_type) {
    m_traveler_type = traveler_type;
    m_traveler_type_isSet = true;
}

bool OAITravelerPricing::is_traveler_type_Set() const{
    return m_traveler_type_isSet;
}

bool OAITravelerPricing::is_traveler_type_Valid() const{
    return m_traveler_type_isValid;
}

bool OAITravelerPricing::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_associated_adult_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fare_details_by_segment.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_fare_option.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_price.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_traveler_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traveler_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITravelerPricing::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_fare_details_by_segment_isValid && m_fare_option_isValid && m_traveler_id_isValid && m_traveler_type_isValid && true;
}

} // namespace OpenAPI
