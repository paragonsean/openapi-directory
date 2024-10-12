/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPricingOptions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPricingOptions::OAIPricingOptions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPricingOptions::OAIPricingOptions() {
    this->initializeModel();
}

OAIPricingOptions::~OAIPricingOptions() {}

void OAIPricingOptions::initializeModel() {

    m_fare_type_isSet = false;
    m_fare_type_isValid = false;

    m_included_checked_bags_only_isSet = false;
    m_included_checked_bags_only_isValid = false;

    m_no_penalty_fare_isSet = false;
    m_no_penalty_fare_isValid = false;

    m_no_restriction_fare_isSet = false;
    m_no_restriction_fare_isValid = false;

    m_refundable_fare_isSet = false;
    m_refundable_fare_isValid = false;
}

void OAIPricingOptions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPricingOptions::fromJsonObject(QJsonObject json) {

    m_fare_type_isValid = ::OpenAPI::fromJsonValue(m_fare_type, json[QString("fareType")]);
    m_fare_type_isSet = !json[QString("fareType")].isNull() && m_fare_type_isValid;

    m_included_checked_bags_only_isValid = ::OpenAPI::fromJsonValue(m_included_checked_bags_only, json[QString("includedCheckedBagsOnly")]);
    m_included_checked_bags_only_isSet = !json[QString("includedCheckedBagsOnly")].isNull() && m_included_checked_bags_only_isValid;

    m_no_penalty_fare_isValid = ::OpenAPI::fromJsonValue(m_no_penalty_fare, json[QString("noPenaltyFare")]);
    m_no_penalty_fare_isSet = !json[QString("noPenaltyFare")].isNull() && m_no_penalty_fare_isValid;

    m_no_restriction_fare_isValid = ::OpenAPI::fromJsonValue(m_no_restriction_fare, json[QString("noRestrictionFare")]);
    m_no_restriction_fare_isSet = !json[QString("noRestrictionFare")].isNull() && m_no_restriction_fare_isValid;

    m_refundable_fare_isValid = ::OpenAPI::fromJsonValue(m_refundable_fare, json[QString("refundableFare")]);
    m_refundable_fare_isSet = !json[QString("refundableFare")].isNull() && m_refundable_fare_isValid;
}

QString OAIPricingOptions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPricingOptions::asJsonObject() const {
    QJsonObject obj;
    if (m_fare_type.size() > 0) {
        obj.insert(QString("fareType"), ::OpenAPI::toJsonValue(m_fare_type));
    }
    if (m_included_checked_bags_only_isSet) {
        obj.insert(QString("includedCheckedBagsOnly"), ::OpenAPI::toJsonValue(m_included_checked_bags_only));
    }
    if (m_no_penalty_fare_isSet) {
        obj.insert(QString("noPenaltyFare"), ::OpenAPI::toJsonValue(m_no_penalty_fare));
    }
    if (m_no_restriction_fare_isSet) {
        obj.insert(QString("noRestrictionFare"), ::OpenAPI::toJsonValue(m_no_restriction_fare));
    }
    if (m_refundable_fare_isSet) {
        obj.insert(QString("refundableFare"), ::OpenAPI::toJsonValue(m_refundable_fare));
    }
    return obj;
}

QList<QString> OAIPricingOptions::getFareType() const {
    return m_fare_type;
}
void OAIPricingOptions::setFareType(const QList<QString> &fare_type) {
    m_fare_type = fare_type;
    m_fare_type_isSet = true;
}

bool OAIPricingOptions::is_fare_type_Set() const{
    return m_fare_type_isSet;
}

bool OAIPricingOptions::is_fare_type_Valid() const{
    return m_fare_type_isValid;
}

bool OAIPricingOptions::isIncludedCheckedBagsOnly() const {
    return m_included_checked_bags_only;
}
void OAIPricingOptions::setIncludedCheckedBagsOnly(const bool &included_checked_bags_only) {
    m_included_checked_bags_only = included_checked_bags_only;
    m_included_checked_bags_only_isSet = true;
}

bool OAIPricingOptions::is_included_checked_bags_only_Set() const{
    return m_included_checked_bags_only_isSet;
}

bool OAIPricingOptions::is_included_checked_bags_only_Valid() const{
    return m_included_checked_bags_only_isValid;
}

bool OAIPricingOptions::isNoPenaltyFare() const {
    return m_no_penalty_fare;
}
void OAIPricingOptions::setNoPenaltyFare(const bool &no_penalty_fare) {
    m_no_penalty_fare = no_penalty_fare;
    m_no_penalty_fare_isSet = true;
}

bool OAIPricingOptions::is_no_penalty_fare_Set() const{
    return m_no_penalty_fare_isSet;
}

bool OAIPricingOptions::is_no_penalty_fare_Valid() const{
    return m_no_penalty_fare_isValid;
}

bool OAIPricingOptions::isNoRestrictionFare() const {
    return m_no_restriction_fare;
}
void OAIPricingOptions::setNoRestrictionFare(const bool &no_restriction_fare) {
    m_no_restriction_fare = no_restriction_fare;
    m_no_restriction_fare_isSet = true;
}

bool OAIPricingOptions::is_no_restriction_fare_Set() const{
    return m_no_restriction_fare_isSet;
}

bool OAIPricingOptions::is_no_restriction_fare_Valid() const{
    return m_no_restriction_fare_isValid;
}

bool OAIPricingOptions::isRefundableFare() const {
    return m_refundable_fare;
}
void OAIPricingOptions::setRefundableFare(const bool &refundable_fare) {
    m_refundable_fare = refundable_fare;
    m_refundable_fare_isSet = true;
}

bool OAIPricingOptions::is_refundable_fare_Set() const{
    return m_refundable_fare_isSet;
}

bool OAIPricingOptions::is_refundable_fare_Valid() const{
    return m_refundable_fare_isValid;
}

bool OAIPricingOptions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fare_type.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_included_checked_bags_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_penalty_fare_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_restriction_fare_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refundable_fare_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPricingOptions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
