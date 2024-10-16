/**
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApiKeys.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApiKeys::OAIApiKeys(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApiKeys::OAIApiKeys() {
    this->initializeModel();
}

OAIApiKeys::~OAIApiKeys() {}

void OAIApiKeys::initializeModel() {

    m_apikeys_isSet = false;
    m_apikeys_isValid = false;
}

void OAIApiKeys::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApiKeys::fromJsonObject(QJsonObject json) {

    m_apikeys_isValid = ::OpenAPI::fromJsonValue(m_apikeys, json[QString("apikeys")]);
    m_apikeys_isSet = !json[QString("apikeys")].isNull() && m_apikeys_isValid;
}

QString OAIApiKeys::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApiKeys::asJsonObject() const {
    QJsonObject obj;
    if (m_apikeys.size() > 0) {
        obj.insert(QString("apikeys"), ::OpenAPI::toJsonValue(m_apikeys));
    }
    return obj;
}

QList<OAIApiKey> OAIApiKeys::getApikeys() const {
    return m_apikeys;
}
void OAIApiKeys::setApikeys(const QList<OAIApiKey> &apikeys) {
    m_apikeys = apikeys;
    m_apikeys_isSet = true;
}

bool OAIApiKeys::is_apikeys_Set() const{
    return m_apikeys_isSet;
}

bool OAIApiKeys::is_apikeys_Valid() const{
    return m_apikeys_isValid;
}

bool OAIApiKeys::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_apikeys.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApiKeys::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_apikeys_isValid && true;
}

} // namespace OpenAPI
