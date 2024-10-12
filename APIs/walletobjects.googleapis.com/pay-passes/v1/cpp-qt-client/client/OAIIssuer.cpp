/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIssuer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssuer::OAIIssuer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssuer::OAIIssuer() {
    this->initializeModel();
}

OAIIssuer::~OAIIssuer() {}

void OAIIssuer::initializeModel() {

    m_contact_info_isSet = false;
    m_contact_info_isValid = false;

    m_homepage_url_isSet = false;
    m_homepage_url_isValid = false;

    m_issuer_id_isSet = false;
    m_issuer_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_smart_tap_merchant_data_isSet = false;
    m_smart_tap_merchant_data_isValid = false;
}

void OAIIssuer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssuer::fromJsonObject(QJsonObject json) {

    m_contact_info_isValid = ::OpenAPI::fromJsonValue(m_contact_info, json[QString("contactInfo")]);
    m_contact_info_isSet = !json[QString("contactInfo")].isNull() && m_contact_info_isValid;

    m_homepage_url_isValid = ::OpenAPI::fromJsonValue(m_homepage_url, json[QString("homepageUrl")]);
    m_homepage_url_isSet = !json[QString("homepageUrl")].isNull() && m_homepage_url_isValid;

    m_issuer_id_isValid = ::OpenAPI::fromJsonValue(m_issuer_id, json[QString("issuerId")]);
    m_issuer_id_isSet = !json[QString("issuerId")].isNull() && m_issuer_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_smart_tap_merchant_data_isValid = ::OpenAPI::fromJsonValue(m_smart_tap_merchant_data, json[QString("smartTapMerchantData")]);
    m_smart_tap_merchant_data_isSet = !json[QString("smartTapMerchantData")].isNull() && m_smart_tap_merchant_data_isValid;
}

QString OAIIssuer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssuer::asJsonObject() const {
    QJsonObject obj;
    if (m_contact_info.isSet()) {
        obj.insert(QString("contactInfo"), ::OpenAPI::toJsonValue(m_contact_info));
    }
    if (m_homepage_url_isSet) {
        obj.insert(QString("homepageUrl"), ::OpenAPI::toJsonValue(m_homepage_url));
    }
    if (m_issuer_id_isSet) {
        obj.insert(QString("issuerId"), ::OpenAPI::toJsonValue(m_issuer_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_smart_tap_merchant_data.isSet()) {
        obj.insert(QString("smartTapMerchantData"), ::OpenAPI::toJsonValue(m_smart_tap_merchant_data));
    }
    return obj;
}

OAIIssuerContactInfo OAIIssuer::getContactInfo() const {
    return m_contact_info;
}
void OAIIssuer::setContactInfo(const OAIIssuerContactInfo &contact_info) {
    m_contact_info = contact_info;
    m_contact_info_isSet = true;
}

bool OAIIssuer::is_contact_info_Set() const{
    return m_contact_info_isSet;
}

bool OAIIssuer::is_contact_info_Valid() const{
    return m_contact_info_isValid;
}

QString OAIIssuer::getHomepageUrl() const {
    return m_homepage_url;
}
void OAIIssuer::setHomepageUrl(const QString &homepage_url) {
    m_homepage_url = homepage_url;
    m_homepage_url_isSet = true;
}

bool OAIIssuer::is_homepage_url_Set() const{
    return m_homepage_url_isSet;
}

bool OAIIssuer::is_homepage_url_Valid() const{
    return m_homepage_url_isValid;
}

QString OAIIssuer::getIssuerId() const {
    return m_issuer_id;
}
void OAIIssuer::setIssuerId(const QString &issuer_id) {
    m_issuer_id = issuer_id;
    m_issuer_id_isSet = true;
}

bool OAIIssuer::is_issuer_id_Set() const{
    return m_issuer_id_isSet;
}

bool OAIIssuer::is_issuer_id_Valid() const{
    return m_issuer_id_isValid;
}

QString OAIIssuer::getName() const {
    return m_name;
}
void OAIIssuer::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIIssuer::is_name_Set() const{
    return m_name_isSet;
}

bool OAIIssuer::is_name_Valid() const{
    return m_name_isValid;
}

OAISmartTapMerchantData OAIIssuer::getSmartTapMerchantData() const {
    return m_smart_tap_merchant_data;
}
void OAIIssuer::setSmartTapMerchantData(const OAISmartTapMerchantData &smart_tap_merchant_data) {
    m_smart_tap_merchant_data = smart_tap_merchant_data;
    m_smart_tap_merchant_data_isSet = true;
}

bool OAIIssuer::is_smart_tap_merchant_data_Set() const{
    return m_smart_tap_merchant_data_isSet;
}

bool OAIIssuer::is_smart_tap_merchant_data_Valid() const{
    return m_smart_tap_merchant_data_isValid;
}

bool OAIIssuer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contact_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_homepage_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issuer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_smart_tap_merchant_data.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIssuer::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
