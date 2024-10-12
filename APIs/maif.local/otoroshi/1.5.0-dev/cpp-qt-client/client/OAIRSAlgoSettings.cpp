/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRSAlgoSettings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRSAlgoSettings::OAIRSAlgoSettings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRSAlgoSettings::OAIRSAlgoSettings() {
    this->initializeModel();
}

OAIRSAlgoSettings::~OAIRSAlgoSettings() {}

void OAIRSAlgoSettings::initializeModel() {

    m_private_key_isSet = false;
    m_private_key_isValid = false;

    m_public_key_isSet = false;
    m_public_key_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIRSAlgoSettings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRSAlgoSettings::fromJsonObject(QJsonObject json) {

    m_private_key_isValid = ::OpenAPI::fromJsonValue(m_private_key, json[QString("privateKey")]);
    m_private_key_isSet = !json[QString("privateKey")].isNull() && m_private_key_isValid;

    m_public_key_isValid = ::OpenAPI::fromJsonValue(m_public_key, json[QString("publicKey")]);
    m_public_key_isSet = !json[QString("publicKey")].isNull() && m_public_key_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIRSAlgoSettings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRSAlgoSettings::asJsonObject() const {
    QJsonObject obj;
    if (m_private_key_isSet) {
        obj.insert(QString("privateKey"), ::OpenAPI::toJsonValue(m_private_key));
    }
    if (m_public_key_isSet) {
        obj.insert(QString("publicKey"), ::OpenAPI::toJsonValue(m_public_key));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIRSAlgoSettings::getPrivateKey() const {
    return m_private_key;
}
void OAIRSAlgoSettings::setPrivateKey(const QString &private_key) {
    m_private_key = private_key;
    m_private_key_isSet = true;
}

bool OAIRSAlgoSettings::is_private_key_Set() const{
    return m_private_key_isSet;
}

bool OAIRSAlgoSettings::is_private_key_Valid() const{
    return m_private_key_isValid;
}

QString OAIRSAlgoSettings::getPublicKey() const {
    return m_public_key;
}
void OAIRSAlgoSettings::setPublicKey(const QString &public_key) {
    m_public_key = public_key;
    m_public_key_isSet = true;
}

bool OAIRSAlgoSettings::is_public_key_Set() const{
    return m_public_key_isSet;
}

bool OAIRSAlgoSettings::is_public_key_Valid() const{
    return m_public_key_isValid;
}

qint32 OAIRSAlgoSettings::getSize() const {
    return m_size;
}
void OAIRSAlgoSettings::setSize(const qint32 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIRSAlgoSettings::is_size_Set() const{
    return m_size_isSet;
}

bool OAIRSAlgoSettings::is_size_Valid() const{
    return m_size_isValid;
}

QString OAIRSAlgoSettings::getType() const {
    return m_type;
}
void OAIRSAlgoSettings::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIRSAlgoSettings::is_type_Set() const{
    return m_type_isSet;
}

bool OAIRSAlgoSettings::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIRSAlgoSettings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_private_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRSAlgoSettings::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_public_key_isValid && m_size_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
