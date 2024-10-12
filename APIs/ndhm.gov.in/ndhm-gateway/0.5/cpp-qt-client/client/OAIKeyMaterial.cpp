/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIKeyMaterial.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIKeyMaterial::OAIKeyMaterial(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIKeyMaterial::OAIKeyMaterial() {
    this->initializeModel();
}

OAIKeyMaterial::~OAIKeyMaterial() {}

void OAIKeyMaterial::initializeModel() {

    m_crypto_alg_isSet = false;
    m_crypto_alg_isValid = false;

    m_curve_isSet = false;
    m_curve_isValid = false;

    m_dh_public_key_isSet = false;
    m_dh_public_key_isValid = false;

    m_nonce_isSet = false;
    m_nonce_isValid = false;
}

void OAIKeyMaterial::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIKeyMaterial::fromJsonObject(QJsonObject json) {

    m_crypto_alg_isValid = ::OpenAPI::fromJsonValue(m_crypto_alg, json[QString("cryptoAlg")]);
    m_crypto_alg_isSet = !json[QString("cryptoAlg")].isNull() && m_crypto_alg_isValid;

    m_curve_isValid = ::OpenAPI::fromJsonValue(m_curve, json[QString("curve")]);
    m_curve_isSet = !json[QString("curve")].isNull() && m_curve_isValid;

    m_dh_public_key_isValid = ::OpenAPI::fromJsonValue(m_dh_public_key, json[QString("dhPublicKey")]);
    m_dh_public_key_isSet = !json[QString("dhPublicKey")].isNull() && m_dh_public_key_isValid;

    m_nonce_isValid = ::OpenAPI::fromJsonValue(m_nonce, json[QString("nonce")]);
    m_nonce_isSet = !json[QString("nonce")].isNull() && m_nonce_isValid;
}

QString OAIKeyMaterial::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIKeyMaterial::asJsonObject() const {
    QJsonObject obj;
    if (m_crypto_alg_isSet) {
        obj.insert(QString("cryptoAlg"), ::OpenAPI::toJsonValue(m_crypto_alg));
    }
    if (m_curve_isSet) {
        obj.insert(QString("curve"), ::OpenAPI::toJsonValue(m_curve));
    }
    if (m_dh_public_key.isSet()) {
        obj.insert(QString("dhPublicKey"), ::OpenAPI::toJsonValue(m_dh_public_key));
    }
    if (m_nonce_isSet) {
        obj.insert(QString("nonce"), ::OpenAPI::toJsonValue(m_nonce));
    }
    return obj;
}

QString OAIKeyMaterial::getCryptoAlg() const {
    return m_crypto_alg;
}
void OAIKeyMaterial::setCryptoAlg(const QString &crypto_alg) {
    m_crypto_alg = crypto_alg;
    m_crypto_alg_isSet = true;
}

bool OAIKeyMaterial::is_crypto_alg_Set() const{
    return m_crypto_alg_isSet;
}

bool OAIKeyMaterial::is_crypto_alg_Valid() const{
    return m_crypto_alg_isValid;
}

QString OAIKeyMaterial::getCurve() const {
    return m_curve;
}
void OAIKeyMaterial::setCurve(const QString &curve) {
    m_curve = curve;
    m_curve_isSet = true;
}

bool OAIKeyMaterial::is_curve_Set() const{
    return m_curve_isSet;
}

bool OAIKeyMaterial::is_curve_Valid() const{
    return m_curve_isValid;
}

OAIKeyObject OAIKeyMaterial::getDhPublicKey() const {
    return m_dh_public_key;
}
void OAIKeyMaterial::setDhPublicKey(const OAIKeyObject &dh_public_key) {
    m_dh_public_key = dh_public_key;
    m_dh_public_key_isSet = true;
}

bool OAIKeyMaterial::is_dh_public_key_Set() const{
    return m_dh_public_key_isSet;
}

bool OAIKeyMaterial::is_dh_public_key_Valid() const{
    return m_dh_public_key_isValid;
}

QString OAIKeyMaterial::getNonce() const {
    return m_nonce;
}
void OAIKeyMaterial::setNonce(const QString &nonce) {
    m_nonce = nonce;
    m_nonce_isSet = true;
}

bool OAIKeyMaterial::is_nonce_Set() const{
    return m_nonce_isSet;
}

bool OAIKeyMaterial::is_nonce_Valid() const{
    return m_nonce_isValid;
}

bool OAIKeyMaterial::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_crypto_alg_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_curve_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dh_public_key.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_nonce_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIKeyMaterial::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_crypto_alg_isValid && m_curve_isValid && m_dh_public_key_isValid && m_nonce_isValid && true;
}

} // namespace OpenAPI
