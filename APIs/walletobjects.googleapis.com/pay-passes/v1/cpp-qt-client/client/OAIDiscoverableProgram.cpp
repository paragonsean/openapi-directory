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

#include "OAIDiscoverableProgram.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDiscoverableProgram::OAIDiscoverableProgram(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDiscoverableProgram::OAIDiscoverableProgram() {
    this->initializeModel();
}

OAIDiscoverableProgram::~OAIDiscoverableProgram() {}

void OAIDiscoverableProgram::initializeModel() {

    m_merchant_signin_info_isSet = false;
    m_merchant_signin_info_isValid = false;

    m_merchant_signup_info_isSet = false;
    m_merchant_signup_info_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIDiscoverableProgram::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDiscoverableProgram::fromJsonObject(QJsonObject json) {

    m_merchant_signin_info_isValid = ::OpenAPI::fromJsonValue(m_merchant_signin_info, json[QString("merchantSigninInfo")]);
    m_merchant_signin_info_isSet = !json[QString("merchantSigninInfo")].isNull() && m_merchant_signin_info_isValid;

    m_merchant_signup_info_isValid = ::OpenAPI::fromJsonValue(m_merchant_signup_info, json[QString("merchantSignupInfo")]);
    m_merchant_signup_info_isSet = !json[QString("merchantSignupInfo")].isNull() && m_merchant_signup_info_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIDiscoverableProgram::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDiscoverableProgram::asJsonObject() const {
    QJsonObject obj;
    if (m_merchant_signin_info.isSet()) {
        obj.insert(QString("merchantSigninInfo"), ::OpenAPI::toJsonValue(m_merchant_signin_info));
    }
    if (m_merchant_signup_info.isSet()) {
        obj.insert(QString("merchantSignupInfo"), ::OpenAPI::toJsonValue(m_merchant_signup_info));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

OAIDiscoverableProgramMerchantSigninInfo OAIDiscoverableProgram::getMerchantSigninInfo() const {
    return m_merchant_signin_info;
}
void OAIDiscoverableProgram::setMerchantSigninInfo(const OAIDiscoverableProgramMerchantSigninInfo &merchant_signin_info) {
    m_merchant_signin_info = merchant_signin_info;
    m_merchant_signin_info_isSet = true;
}

bool OAIDiscoverableProgram::is_merchant_signin_info_Set() const{
    return m_merchant_signin_info_isSet;
}

bool OAIDiscoverableProgram::is_merchant_signin_info_Valid() const{
    return m_merchant_signin_info_isValid;
}

OAIDiscoverableProgramMerchantSignupInfo OAIDiscoverableProgram::getMerchantSignupInfo() const {
    return m_merchant_signup_info;
}
void OAIDiscoverableProgram::setMerchantSignupInfo(const OAIDiscoverableProgramMerchantSignupInfo &merchant_signup_info) {
    m_merchant_signup_info = merchant_signup_info;
    m_merchant_signup_info_isSet = true;
}

bool OAIDiscoverableProgram::is_merchant_signup_info_Set() const{
    return m_merchant_signup_info_isSet;
}

bool OAIDiscoverableProgram::is_merchant_signup_info_Valid() const{
    return m_merchant_signup_info_isValid;
}

QString OAIDiscoverableProgram::getState() const {
    return m_state;
}
void OAIDiscoverableProgram::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIDiscoverableProgram::is_state_Set() const{
    return m_state_isSet;
}

bool OAIDiscoverableProgram::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIDiscoverableProgram::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_merchant_signin_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_signup_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDiscoverableProgram::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
