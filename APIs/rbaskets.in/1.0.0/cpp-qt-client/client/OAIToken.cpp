/**
 * Request Baskets API
 * RESTful API of [Request Baskets](https://rbaskets.in) service.  Request Baskets is an open source project of a service to collect HTTP requests and inspect them via RESTful API or web UI.  Check out the [project page](https://github.com/darklynx/request-baskets) for more detailed description. 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIToken.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIToken::OAIToken(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIToken::OAIToken() {
    this->initializeModel();
}

OAIToken::~OAIToken() {}

void OAIToken::initializeModel() {

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIToken::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIToken::fromJsonObject(QJsonObject json) {

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIToken::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIToken::asJsonObject() const {
    QJsonObject obj;
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

QString OAIToken::getToken() const {
    return m_token;
}
void OAIToken::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIToken::is_token_Set() const{
    return m_token_isSet;
}

bool OAIToken::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIToken::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIToken::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_token_isValid && true;
}

} // namespace OpenAPI
