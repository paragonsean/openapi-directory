/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetOrganizationInventoryDevices_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationInventoryDevices_200_response_inner::OAIGetOrganizationInventoryDevices_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationInventoryDevices_200_response_inner::OAIGetOrganizationInventoryDevices_200_response_inner() {
    this->initializeModel();
}

OAIGetOrganizationInventoryDevices_200_response_inner::~OAIGetOrganizationInventoryDevices_200_response_inner() {}

void OAIGetOrganizationInventoryDevices_200_response_inner::initializeModel() {

    m_claimed_at_isSet = false;
    m_claimed_at_isValid = false;

    m_license_expiration_date_isSet = false;
    m_license_expiration_date_isValid = false;

    m_mac_isSet = false;
    m_mac_isValid = false;

    m_model_isSet = false;
    m_model_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_network_id_isSet = false;
    m_network_id_isValid = false;

    m_order_number_isSet = false;
    m_order_number_isValid = false;

    m_product_type_isSet = false;
    m_product_type_isValid = false;

    m_serial_isSet = false;
    m_serial_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAIGetOrganizationInventoryDevices_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationInventoryDevices_200_response_inner::fromJsonObject(QJsonObject json) {

    m_claimed_at_isValid = ::OpenAPI::fromJsonValue(m_claimed_at, json[QString("claimedAt")]);
    m_claimed_at_isSet = !json[QString("claimedAt")].isNull() && m_claimed_at_isValid;

    m_license_expiration_date_isValid = ::OpenAPI::fromJsonValue(m_license_expiration_date, json[QString("licenseExpirationDate")]);
    m_license_expiration_date_isSet = !json[QString("licenseExpirationDate")].isNull() && m_license_expiration_date_isValid;

    m_mac_isValid = ::OpenAPI::fromJsonValue(m_mac, json[QString("mac")]);
    m_mac_isSet = !json[QString("mac")].isNull() && m_mac_isValid;

    m_model_isValid = ::OpenAPI::fromJsonValue(m_model, json[QString("model")]);
    m_model_isSet = !json[QString("model")].isNull() && m_model_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_network_id_isValid = ::OpenAPI::fromJsonValue(m_network_id, json[QString("networkId")]);
    m_network_id_isSet = !json[QString("networkId")].isNull() && m_network_id_isValid;

    m_order_number_isValid = ::OpenAPI::fromJsonValue(m_order_number, json[QString("orderNumber")]);
    m_order_number_isSet = !json[QString("orderNumber")].isNull() && m_order_number_isValid;

    m_product_type_isValid = ::OpenAPI::fromJsonValue(m_product_type, json[QString("productType")]);
    m_product_type_isSet = !json[QString("productType")].isNull() && m_product_type_isValid;

    m_serial_isValid = ::OpenAPI::fromJsonValue(m_serial, json[QString("serial")]);
    m_serial_isSet = !json[QString("serial")].isNull() && m_serial_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationInventoryDevices_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_claimed_at_isSet) {
        obj.insert(QString("claimedAt"), ::OpenAPI::toJsonValue(m_claimed_at));
    }
    if (m_license_expiration_date_isSet) {
        obj.insert(QString("licenseExpirationDate"), ::OpenAPI::toJsonValue(m_license_expiration_date));
    }
    if (m_mac_isSet) {
        obj.insert(QString("mac"), ::OpenAPI::toJsonValue(m_mac));
    }
    if (m_model_isSet) {
        obj.insert(QString("model"), ::OpenAPI::toJsonValue(m_model));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_network_id_isSet) {
        obj.insert(QString("networkId"), ::OpenAPI::toJsonValue(m_network_id));
    }
    if (m_order_number_isSet) {
        obj.insert(QString("orderNumber"), ::OpenAPI::toJsonValue(m_order_number));
    }
    if (m_product_type_isSet) {
        obj.insert(QString("productType"), ::OpenAPI::toJsonValue(m_product_type));
    }
    if (m_serial_isSet) {
        obj.insert(QString("serial"), ::OpenAPI::toJsonValue(m_serial));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

QDateTime OAIGetOrganizationInventoryDevices_200_response_inner::getClaimedAt() const {
    return m_claimed_at;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setClaimedAt(const QDateTime &claimed_at) {
    m_claimed_at = claimed_at;
    m_claimed_at_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_claimed_at_Set() const{
    return m_claimed_at_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_claimed_at_Valid() const{
    return m_claimed_at_isValid;
}

QDateTime OAIGetOrganizationInventoryDevices_200_response_inner::getLicenseExpirationDate() const {
    return m_license_expiration_date;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setLicenseExpirationDate(const QDateTime &license_expiration_date) {
    m_license_expiration_date = license_expiration_date;
    m_license_expiration_date_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_license_expiration_date_Set() const{
    return m_license_expiration_date_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_license_expiration_date_Valid() const{
    return m_license_expiration_date_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::getMac() const {
    return m_mac;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setMac(const QString &mac) {
    m_mac = mac;
    m_mac_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_mac_Set() const{
    return m_mac_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_mac_Valid() const{
    return m_mac_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::getModel() const {
    return m_model;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setModel(const QString &model) {
    m_model = model;
    m_model_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_model_Set() const{
    return m_model_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_model_Valid() const{
    return m_model_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::getName() const {
    return m_name;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::getNetworkId() const {
    return m_network_id;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setNetworkId(const QString &network_id) {
    m_network_id = network_id;
    m_network_id_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_network_id_Set() const{
    return m_network_id_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_network_id_Valid() const{
    return m_network_id_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::getOrderNumber() const {
    return m_order_number;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setOrderNumber(const QString &order_number) {
    m_order_number = order_number;
    m_order_number_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_order_number_Set() const{
    return m_order_number_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_order_number_Valid() const{
    return m_order_number_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::getProductType() const {
    return m_product_type;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setProductType(const QString &product_type) {
    m_product_type = product_type;
    m_product_type_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_product_type_Set() const{
    return m_product_type_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_product_type_Valid() const{
    return m_product_type_isValid;
}

QString OAIGetOrganizationInventoryDevices_200_response_inner::getSerial() const {
    return m_serial;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setSerial(const QString &serial) {
    m_serial = serial;
    m_serial_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_serial_Set() const{
    return m_serial_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_serial_Valid() const{
    return m_serial_isValid;
}

QList<QString> OAIGetOrganizationInventoryDevices_200_response_inner::getTags() const {
    return m_tags;
}
void OAIGetOrganizationInventoryDevices_200_response_inner::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_claimed_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_license_expiration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mac_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_network_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_serial_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationInventoryDevices_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
