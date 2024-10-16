/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPayer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayer::OAIPayer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayer::OAIPayer() {
    this->initializeModel();
}

OAIPayer::~OAIPayer() {}

void OAIPayer::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIPayer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayer::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIPayer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayer::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIPayer::getEmail() const {
    return m_email;
}
void OAIPayer::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIPayer::is_email_Set() const{
    return m_email_isSet;
}

bool OAIPayer::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIPayer::getName() const {
    return m_name;
}
void OAIPayer::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPayer::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPayer::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIPayer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPayer::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
