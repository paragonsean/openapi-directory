/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICertificateRepresentation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICertificateRepresentation::OAICertificateRepresentation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICertificateRepresentation::OAICertificateRepresentation() {
    this->initializeModel();
}

OAICertificateRepresentation::~OAICertificateRepresentation() {}

void OAICertificateRepresentation::initializeModel() {

    m_certificate_isSet = false;
    m_certificate_isValid = false;

    m_kid_isSet = false;
    m_kid_isValid = false;

    m_private_key_isSet = false;
    m_private_key_isValid = false;

    m_public_key_isSet = false;
    m_public_key_isValid = false;
}

void OAICertificateRepresentation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICertificateRepresentation::fromJsonObject(QJsonObject json) {

    m_certificate_isValid = ::OpenAPI::fromJsonValue(m_certificate, json[QString("certificate")]);
    m_certificate_isSet = !json[QString("certificate")].isNull() && m_certificate_isValid;

    m_kid_isValid = ::OpenAPI::fromJsonValue(m_kid, json[QString("kid")]);
    m_kid_isSet = !json[QString("kid")].isNull() && m_kid_isValid;

    m_private_key_isValid = ::OpenAPI::fromJsonValue(m_private_key, json[QString("privateKey")]);
    m_private_key_isSet = !json[QString("privateKey")].isNull() && m_private_key_isValid;

    m_public_key_isValid = ::OpenAPI::fromJsonValue(m_public_key, json[QString("publicKey")]);
    m_public_key_isSet = !json[QString("publicKey")].isNull() && m_public_key_isValid;
}

QString OAICertificateRepresentation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICertificateRepresentation::asJsonObject() const {
    QJsonObject obj;
    if (m_certificate_isSet) {
        obj.insert(QString("certificate"), ::OpenAPI::toJsonValue(m_certificate));
    }
    if (m_kid_isSet) {
        obj.insert(QString("kid"), ::OpenAPI::toJsonValue(m_kid));
    }
    if (m_private_key_isSet) {
        obj.insert(QString("privateKey"), ::OpenAPI::toJsonValue(m_private_key));
    }
    if (m_public_key_isSet) {
        obj.insert(QString("publicKey"), ::OpenAPI::toJsonValue(m_public_key));
    }
    return obj;
}

QString OAICertificateRepresentation::getCertificate() const {
    return m_certificate;
}
void OAICertificateRepresentation::setCertificate(const QString &certificate) {
    m_certificate = certificate;
    m_certificate_isSet = true;
}

bool OAICertificateRepresentation::is_certificate_Set() const{
    return m_certificate_isSet;
}

bool OAICertificateRepresentation::is_certificate_Valid() const{
    return m_certificate_isValid;
}

QString OAICertificateRepresentation::getKid() const {
    return m_kid;
}
void OAICertificateRepresentation::setKid(const QString &kid) {
    m_kid = kid;
    m_kid_isSet = true;
}

bool OAICertificateRepresentation::is_kid_Set() const{
    return m_kid_isSet;
}

bool OAICertificateRepresentation::is_kid_Valid() const{
    return m_kid_isValid;
}

QString OAICertificateRepresentation::getPrivateKey() const {
    return m_private_key;
}
void OAICertificateRepresentation::setPrivateKey(const QString &private_key) {
    m_private_key = private_key;
    m_private_key_isSet = true;
}

bool OAICertificateRepresentation::is_private_key_Set() const{
    return m_private_key_isSet;
}

bool OAICertificateRepresentation::is_private_key_Valid() const{
    return m_private_key_isValid;
}

QString OAICertificateRepresentation::getPublicKey() const {
    return m_public_key;
}
void OAICertificateRepresentation::setPublicKey(const QString &public_key) {
    m_public_key = public_key;
    m_public_key_isSet = true;
}

bool OAICertificateRepresentation::is_public_key_Set() const{
    return m_public_key_isSet;
}

bool OAICertificateRepresentation::is_public_key_Valid() const{
    return m_public_key_isValid;
}

bool OAICertificateRepresentation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_certificate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_private_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_key_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICertificateRepresentation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
