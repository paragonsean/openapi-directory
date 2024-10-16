/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAccountLink.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccountLink::OAIAccountLink(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccountLink::OAIAccountLink() {
    this->initializeModel();
}

OAIAccountLink::~OAIAccountLink() {}

void OAIAccountLink::initializeModel() {

    m_account_link_target_isSet = false;
    m_account_link_target_isValid = false;

    m_google_ads_customer_name_isSet = false;
    m_google_ads_customer_name_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAIAccountLink::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccountLink::fromJsonObject(QJsonObject json) {

    m_account_link_target_isValid = ::OpenAPI::fromJsonValue(m_account_link_target, json[QString("accountLinkTarget")]);
    m_account_link_target_isSet = !json[QString("accountLinkTarget")].isNull() && m_account_link_target_isValid;

    m_google_ads_customer_name_isValid = ::OpenAPI::fromJsonValue(m_google_ads_customer_name, json[QString("googleAdsCustomerName")]);
    m_google_ads_customer_name_isSet = !json[QString("googleAdsCustomerName")].isNull() && m_google_ads_customer_name_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;
}

QString OAIAccountLink::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccountLink::asJsonObject() const {
    QJsonObject obj;
    if (m_account_link_target.isSet()) {
        obj.insert(QString("accountLinkTarget"), ::OpenAPI::toJsonValue(m_account_link_target));
    }
    if (m_google_ads_customer_name_isSet) {
        obj.insert(QString("googleAdsCustomerName"), ::OpenAPI::toJsonValue(m_google_ads_customer_name));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

OAIAccountLinkTarget OAIAccountLink::getAccountLinkTarget() const {
    return m_account_link_target;
}
void OAIAccountLink::setAccountLinkTarget(const OAIAccountLinkTarget &account_link_target) {
    m_account_link_target = account_link_target;
    m_account_link_target_isSet = true;
}

bool OAIAccountLink::is_account_link_target_Set() const{
    return m_account_link_target_isSet;
}

bool OAIAccountLink::is_account_link_target_Valid() const{
    return m_account_link_target_isValid;
}

QString OAIAccountLink::getGoogleAdsCustomerName() const {
    return m_google_ads_customer_name;
}
void OAIAccountLink::setGoogleAdsCustomerName(const QString &google_ads_customer_name) {
    m_google_ads_customer_name = google_ads_customer_name;
    m_google_ads_customer_name_isSet = true;
}

bool OAIAccountLink::is_google_ads_customer_name_Set() const{
    return m_google_ads_customer_name_isSet;
}

bool OAIAccountLink::is_google_ads_customer_name_Valid() const{
    return m_google_ads_customer_name_isValid;
}

QString OAIAccountLink::getName() const {
    return m_name;
}
void OAIAccountLink::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAccountLink::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAccountLink::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAccountLink::getStatus() const {
    return m_status;
}
void OAIAccountLink::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIAccountLink::is_status_Set() const{
    return m_status_isSet;
}

bool OAIAccountLink::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIAccountLink::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_link_target.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_google_ads_customer_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccountLink::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
