/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserLockout.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserLockout::OAIUserLockout(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserLockout::OAIUserLockout() {
    this->initializeModel();
}

OAIUserLockout::~OAIUserLockout() {}

void OAIUserLockout::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_lockout_period_isSet = false;
    m_lockout_period_isValid = false;

    m_max_number_of_login_failures_isSet = false;
    m_max_number_of_login_failures_isValid = false;
}

void OAIUserLockout::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserLockout::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_lockout_period_isValid = ::OpenAPI::fromJsonValue(m_lockout_period, json[QString("lockoutPeriod")]);
    m_lockout_period_isSet = !json[QString("lockoutPeriod")].isNull() && m_lockout_period_isValid;

    m_max_number_of_login_failures_isValid = ::OpenAPI::fromJsonValue(m_max_number_of_login_failures, json[QString("maxNumberOfLoginFailures")]);
    m_max_number_of_login_failures_isSet = !json[QString("maxNumberOfLoginFailures")].isNull() && m_max_number_of_login_failures_isValid;
}

QString OAIUserLockout::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserLockout::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_lockout_period_isSet) {
        obj.insert(QString("lockoutPeriod"), ::OpenAPI::toJsonValue(m_lockout_period));
    }
    if (m_max_number_of_login_failures_isSet) {
        obj.insert(QString("maxNumberOfLoginFailures"), ::OpenAPI::toJsonValue(m_max_number_of_login_failures));
    }
    return obj;
}

bool OAIUserLockout::isEnabled() const {
    return m_enabled;
}
void OAIUserLockout::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIUserLockout::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIUserLockout::is_enabled_Valid() const{
    return m_enabled_isValid;
}

qint32 OAIUserLockout::getLockoutPeriod() const {
    return m_lockout_period;
}
void OAIUserLockout::setLockoutPeriod(const qint32 &lockout_period) {
    m_lockout_period = lockout_period;
    m_lockout_period_isSet = true;
}

bool OAIUserLockout::is_lockout_period_Set() const{
    return m_lockout_period_isSet;
}

bool OAIUserLockout::is_lockout_period_Valid() const{
    return m_lockout_period_isValid;
}

qint32 OAIUserLockout::getMaxNumberOfLoginFailures() const {
    return m_max_number_of_login_failures;
}
void OAIUserLockout::setMaxNumberOfLoginFailures(const qint32 &max_number_of_login_failures) {
    m_max_number_of_login_failures = max_number_of_login_failures;
    m_max_number_of_login_failures_isSet = true;
}

bool OAIUserLockout::is_max_number_of_login_failures_Set() const{
    return m_max_number_of_login_failures_isSet;
}

bool OAIUserLockout::is_max_number_of_login_failures_Valid() const{
    return m_max_number_of_login_failures_isValid;
}

bool OAIUserLockout::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lockout_period_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_number_of_login_failures_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserLockout::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_enabled_isValid && true;
}

} // namespace OpenAPI
