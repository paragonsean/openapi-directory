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

#include "OAICertKeyPathPair.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICertKeyPathPair::OAICertKeyPathPair(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICertKeyPathPair::OAICertKeyPathPair() {
    this->initializeModel();
}

OAICertKeyPathPair::~OAICertKeyPathPair() {}

void OAICertKeyPathPair::initializeModel() {

    m_certificate_path_isSet = false;
    m_certificate_path_isValid = false;

    m_key_path_isSet = false;
    m_key_path_isValid = false;
}

void OAICertKeyPathPair::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICertKeyPathPair::fromJsonObject(QJsonObject json) {

    m_certificate_path_isValid = ::OpenAPI::fromJsonValue(m_certificate_path, json[QString("certificate_path")]);
    m_certificate_path_isSet = !json[QString("certificate_path")].isNull() && m_certificate_path_isValid;

    m_key_path_isValid = ::OpenAPI::fromJsonValue(m_key_path, json[QString("key_path")]);
    m_key_path_isSet = !json[QString("key_path")].isNull() && m_key_path_isValid;
}

QString OAICertKeyPathPair::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICertKeyPathPair::asJsonObject() const {
    QJsonObject obj;
    if (m_certificate_path_isSet) {
        obj.insert(QString("certificate_path"), ::OpenAPI::toJsonValue(m_certificate_path));
    }
    if (m_key_path_isSet) {
        obj.insert(QString("key_path"), ::OpenAPI::toJsonValue(m_key_path));
    }
    return obj;
}

QString OAICertKeyPathPair::getCertificatePath() const {
    return m_certificate_path;
}
void OAICertKeyPathPair::setCertificatePath(const QString &certificate_path) {
    m_certificate_path = certificate_path;
    m_certificate_path_isSet = true;
}

bool OAICertKeyPathPair::is_certificate_path_Set() const{
    return m_certificate_path_isSet;
}

bool OAICertKeyPathPair::is_certificate_path_Valid() const{
    return m_certificate_path_isValid;
}

QString OAICertKeyPathPair::getKeyPath() const {
    return m_key_path;
}
void OAICertKeyPathPair::setKeyPath(const QString &key_path) {
    m_key_path = key_path;
    m_key_path_isSet = true;
}

bool OAICertKeyPathPair::is_key_path_Set() const{
    return m_key_path_isSet;
}

bool OAICertKeyPathPair::is_key_path_Valid() const{
    return m_key_path_isValid;
}

bool OAICertKeyPathPair::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_certificate_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_path_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICertKeyPathPair::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_certificate_path_isValid && m_key_path_isValid && true;
}

} // namespace OpenAPI
