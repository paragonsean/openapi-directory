/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAccessTokenDescription.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccessTokenDescription::OAIAccessTokenDescription(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccessTokenDescription::OAIAccessTokenDescription() {
    this->initializeModel();
}

OAIAccessTokenDescription::~OAIAccessTokenDescription() {}

void OAIAccessTokenDescription::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;
}

void OAIAccessTokenDescription::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccessTokenDescription::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;
}

QString OAIAccessTokenDescription::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccessTokenDescription::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    return obj;
}

QString OAIAccessTokenDescription::getDescription() const {
    return m_description;
}
void OAIAccessTokenDescription::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAccessTokenDescription::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAccessTokenDescription::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIAccessTokenDescription::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccessTokenDescription::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_description_isValid && true;
}

} // namespace OpenAPI
