/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOtherMethod.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOtherMethod::OAIOtherMethod(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOtherMethod::OAIOtherMethod() {
    this->initializeModel();
}

OAIOtherMethod::~OAIOtherMethod() {}

void OAIOtherMethod::initializeModel() {

    m_flight_offer_ids_isSet = false;
    m_flight_offer_ids_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;
}

void OAIOtherMethod::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOtherMethod::fromJsonObject(QJsonObject json) {

    m_flight_offer_ids_isValid = ::OpenAPI::fromJsonValue(m_flight_offer_ids, json[QString("flightOfferIds")]);
    m_flight_offer_ids_isSet = !json[QString("flightOfferIds")].isNull() && m_flight_offer_ids_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;
}

QString OAIOtherMethod::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOtherMethod::asJsonObject() const {
    QJsonObject obj;
    if (m_flight_offer_ids.size() > 0) {
        obj.insert(QString("flightOfferIds"), ::OpenAPI::toJsonValue(m_flight_offer_ids));
    }
    if (m_method.isSet()) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    return obj;
}

QList<QString> OAIOtherMethod::getFlightOfferIds() const {
    return m_flight_offer_ids;
}
void OAIOtherMethod::setFlightOfferIds(const QList<QString> &flight_offer_ids) {
    m_flight_offer_ids = flight_offer_ids;
    m_flight_offer_ids_isSet = true;
}

bool OAIOtherMethod::is_flight_offer_ids_Set() const{
    return m_flight_offer_ids_isSet;
}

bool OAIOtherMethod::is_flight_offer_ids_Valid() const{
    return m_flight_offer_ids_isValid;
}

OAIOtherPaymentMethod OAIOtherMethod::getMethod() const {
    return m_method;
}
void OAIOtherMethod::setMethod(const OAIOtherPaymentMethod &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIOtherMethod::is_method_Set() const{
    return m_method_isSet;
}

bool OAIOtherMethod::is_method_Valid() const{
    return m_method_isValid;
}

bool OAIOtherMethod::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_flight_offer_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_method.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOtherMethod::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
