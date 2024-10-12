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

#include "OAIDiscoverableProgramMerchantSignupInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDiscoverableProgramMerchantSignupInfo::OAIDiscoverableProgramMerchantSignupInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDiscoverableProgramMerchantSignupInfo::OAIDiscoverableProgramMerchantSignupInfo() {
    this->initializeModel();
}

OAIDiscoverableProgramMerchantSignupInfo::~OAIDiscoverableProgramMerchantSignupInfo() {}

void OAIDiscoverableProgramMerchantSignupInfo::initializeModel() {

    m_signup_shared_datas_isSet = false;
    m_signup_shared_datas_isValid = false;

    m_signup_website_isSet = false;
    m_signup_website_isValid = false;
}

void OAIDiscoverableProgramMerchantSignupInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDiscoverableProgramMerchantSignupInfo::fromJsonObject(QJsonObject json) {

    m_signup_shared_datas_isValid = ::OpenAPI::fromJsonValue(m_signup_shared_datas, json[QString("signupSharedDatas")]);
    m_signup_shared_datas_isSet = !json[QString("signupSharedDatas")].isNull() && m_signup_shared_datas_isValid;

    m_signup_website_isValid = ::OpenAPI::fromJsonValue(m_signup_website, json[QString("signupWebsite")]);
    m_signup_website_isSet = !json[QString("signupWebsite")].isNull() && m_signup_website_isValid;
}

QString OAIDiscoverableProgramMerchantSignupInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDiscoverableProgramMerchantSignupInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_signup_shared_datas.size() > 0) {
        obj.insert(QString("signupSharedDatas"), ::OpenAPI::toJsonValue(m_signup_shared_datas));
    }
    if (m_signup_website.isSet()) {
        obj.insert(QString("signupWebsite"), ::OpenAPI::toJsonValue(m_signup_website));
    }
    return obj;
}

QList<QString> OAIDiscoverableProgramMerchantSignupInfo::getSignupSharedDatas() const {
    return m_signup_shared_datas;
}
void OAIDiscoverableProgramMerchantSignupInfo::setSignupSharedDatas(const QList<QString> &signup_shared_datas) {
    m_signup_shared_datas = signup_shared_datas;
    m_signup_shared_datas_isSet = true;
}

bool OAIDiscoverableProgramMerchantSignupInfo::is_signup_shared_datas_Set() const{
    return m_signup_shared_datas_isSet;
}

bool OAIDiscoverableProgramMerchantSignupInfo::is_signup_shared_datas_Valid() const{
    return m_signup_shared_datas_isValid;
}

OAIUri OAIDiscoverableProgramMerchantSignupInfo::getSignupWebsite() const {
    return m_signup_website;
}
void OAIDiscoverableProgramMerchantSignupInfo::setSignupWebsite(const OAIUri &signup_website) {
    m_signup_website = signup_website;
    m_signup_website_isSet = true;
}

bool OAIDiscoverableProgramMerchantSignupInfo::is_signup_website_Set() const{
    return m_signup_website_isSet;
}

bool OAIDiscoverableProgramMerchantSignupInfo::is_signup_website_Valid() const{
    return m_signup_website_isValid;
}

bool OAIDiscoverableProgramMerchantSignupInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_signup_shared_datas.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_signup_website.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDiscoverableProgramMerchantSignupInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
