/**
 * KumpeApps API
 * KKid API. Due to security concerns all calls to this API requires authentication. If you have access then you may use your KumpeApps username/password to authenticate. To gain access please use the contact developer link below.
 *
 * The version of the OpenAPI document: 5.0.0
 * Contact: helpdesk@kumpeapps.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI405.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI405::OAI405(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI405::OAI405() {
    this->initializeModel();
}

OAI405::~OAI405() {}

void OAI405::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAI405::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI405::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAI405::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI405::asJsonObject() const {
    QJsonObject obj;
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

QString OAI405::getError() const {
    return m_error;
}
void OAI405::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAI405::is_error_Set() const{
    return m_error_isSet;
}

bool OAI405::is_error_Valid() const{
    return m_error_isValid;
}

qint32 OAI405::getSuccess() const {
    return m_success;
}
void OAI405::setSuccess(const qint32 &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAI405::is_success_Set() const{
    return m_success_isSet;
}

bool OAI405::is_success_Valid() const{
    return m_success_isValid;
}

bool OAI405::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI405::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
