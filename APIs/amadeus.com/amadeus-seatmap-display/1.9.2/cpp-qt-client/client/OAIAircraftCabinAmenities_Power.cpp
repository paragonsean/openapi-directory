/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAircraftCabinAmenities_Power.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAircraftCabinAmenities_Power::OAIAircraftCabinAmenities_Power(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAircraftCabinAmenities_Power::OAIAircraftCabinAmenities_Power() {
    this->initializeModel();
}

OAIAircraftCabinAmenities_Power::~OAIAircraftCabinAmenities_Power() {}

void OAIAircraftCabinAmenities_Power::initializeModel() {

    m_is_chargeable_isSet = false;
    m_is_chargeable_isValid = false;

    m_power_type_isSet = false;
    m_power_type_isValid = false;

    m_usb_type_isSet = false;
    m_usb_type_isValid = false;
}

void OAIAircraftCabinAmenities_Power::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAircraftCabinAmenities_Power::fromJsonObject(QJsonObject json) {

    m_is_chargeable_isValid = ::OpenAPI::fromJsonValue(m_is_chargeable, json[QString("isChargeable")]);
    m_is_chargeable_isSet = !json[QString("isChargeable")].isNull() && m_is_chargeable_isValid;

    m_power_type_isValid = ::OpenAPI::fromJsonValue(m_power_type, json[QString("powerType")]);
    m_power_type_isSet = !json[QString("powerType")].isNull() && m_power_type_isValid;

    m_usb_type_isValid = ::OpenAPI::fromJsonValue(m_usb_type, json[QString("usbType")]);
    m_usb_type_isSet = !json[QString("usbType")].isNull() && m_usb_type_isValid;
}

QString OAIAircraftCabinAmenities_Power::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAircraftCabinAmenities_Power::asJsonObject() const {
    QJsonObject obj;
    if (m_is_chargeable_isSet) {
        obj.insert(QString("isChargeable"), ::OpenAPI::toJsonValue(m_is_chargeable));
    }
    if (m_power_type_isSet) {
        obj.insert(QString("powerType"), ::OpenAPI::toJsonValue(m_power_type));
    }
    if (m_usb_type_isSet) {
        obj.insert(QString("usbType"), ::OpenAPI::toJsonValue(m_usb_type));
    }
    return obj;
}

bool OAIAircraftCabinAmenities_Power::isIsChargeable() const {
    return m_is_chargeable;
}
void OAIAircraftCabinAmenities_Power::setIsChargeable(const bool &is_chargeable) {
    m_is_chargeable = is_chargeable;
    m_is_chargeable_isSet = true;
}

bool OAIAircraftCabinAmenities_Power::is_is_chargeable_Set() const{
    return m_is_chargeable_isSet;
}

bool OAIAircraftCabinAmenities_Power::is_is_chargeable_Valid() const{
    return m_is_chargeable_isValid;
}

QString OAIAircraftCabinAmenities_Power::getPowerType() const {
    return m_power_type;
}
void OAIAircraftCabinAmenities_Power::setPowerType(const QString &power_type) {
    m_power_type = power_type;
    m_power_type_isSet = true;
}

bool OAIAircraftCabinAmenities_Power::is_power_type_Set() const{
    return m_power_type_isSet;
}

bool OAIAircraftCabinAmenities_Power::is_power_type_Valid() const{
    return m_power_type_isValid;
}

QString OAIAircraftCabinAmenities_Power::getUsbType() const {
    return m_usb_type;
}
void OAIAircraftCabinAmenities_Power::setUsbType(const QString &usb_type) {
    m_usb_type = usb_type;
    m_usb_type_isSet = true;
}

bool OAIAircraftCabinAmenities_Power::is_usb_type_Set() const{
    return m_usb_type_isSet;
}

bool OAIAircraftCabinAmenities_Power::is_usb_type_Valid() const{
    return m_usb_type_isValid;
}

bool OAIAircraftCabinAmenities_Power::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_chargeable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_power_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_usb_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAircraftCabinAmenities_Power::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
