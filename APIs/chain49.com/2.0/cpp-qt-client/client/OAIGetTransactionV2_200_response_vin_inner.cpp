/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetTransactionV2_200_response_vin_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetTransactionV2_200_response_vin_inner::OAIGetTransactionV2_200_response_vin_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetTransactionV2_200_response_vin_inner::OAIGetTransactionV2_200_response_vin_inner() {
    this->initializeModel();
}

OAIGetTransactionV2_200_response_vin_inner::~OAIGetTransactionV2_200_response_vin_inner() {}

void OAIGetTransactionV2_200_response_vin_inner::initializeModel() {

    m_addresses_isSet = false;
    m_addresses_isValid = false;

    m_hex_isSet = false;
    m_hex_isValid = false;

    m_is_address_isSet = false;
    m_is_address_isValid = false;

    m_n_isSet = false;
    m_n_isValid = false;

    m_sequence_isSet = false;
    m_sequence_isValid = false;

    m_txid_isSet = false;
    m_txid_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;

    m_vout_isSet = false;
    m_vout_isValid = false;
}

void OAIGetTransactionV2_200_response_vin_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetTransactionV2_200_response_vin_inner::fromJsonObject(QJsonObject json) {

    m_addresses_isValid = ::OpenAPI::fromJsonValue(m_addresses, json[QString("addresses")]);
    m_addresses_isSet = !json[QString("addresses")].isNull() && m_addresses_isValid;

    m_hex_isValid = ::OpenAPI::fromJsonValue(m_hex, json[QString("hex")]);
    m_hex_isSet = !json[QString("hex")].isNull() && m_hex_isValid;

    m_is_address_isValid = ::OpenAPI::fromJsonValue(m_is_address, json[QString("isAddress")]);
    m_is_address_isSet = !json[QString("isAddress")].isNull() && m_is_address_isValid;

    m_n_isValid = ::OpenAPI::fromJsonValue(m_n, json[QString("n")]);
    m_n_isSet = !json[QString("n")].isNull() && m_n_isValid;

    m_sequence_isValid = ::OpenAPI::fromJsonValue(m_sequence, json[QString("sequence")]);
    m_sequence_isSet = !json[QString("sequence")].isNull() && m_sequence_isValid;

    m_txid_isValid = ::OpenAPI::fromJsonValue(m_txid, json[QString("txid")]);
    m_txid_isSet = !json[QString("txid")].isNull() && m_txid_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_vout_isValid = ::OpenAPI::fromJsonValue(m_vout, json[QString("vout")]);
    m_vout_isSet = !json[QString("vout")].isNull() && m_vout_isValid;
}

QString OAIGetTransactionV2_200_response_vin_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetTransactionV2_200_response_vin_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_addresses.size() > 0) {
        obj.insert(QString("addresses"), ::OpenAPI::toJsonValue(m_addresses));
    }
    if (m_hex_isSet) {
        obj.insert(QString("hex"), ::OpenAPI::toJsonValue(m_hex));
    }
    if (m_is_address_isSet) {
        obj.insert(QString("isAddress"), ::OpenAPI::toJsonValue(m_is_address));
    }
    if (m_n_isSet) {
        obj.insert(QString("n"), ::OpenAPI::toJsonValue(m_n));
    }
    if (m_sequence_isSet) {
        obj.insert(QString("sequence"), ::OpenAPI::toJsonValue(m_sequence));
    }
    if (m_txid_isSet) {
        obj.insert(QString("txid"), ::OpenAPI::toJsonValue(m_txid));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_vout_isSet) {
        obj.insert(QString("vout"), ::OpenAPI::toJsonValue(m_vout));
    }
    return obj;
}

QList<QString> OAIGetTransactionV2_200_response_vin_inner::getAddresses() const {
    return m_addresses;
}
void OAIGetTransactionV2_200_response_vin_inner::setAddresses(const QList<QString> &addresses) {
    m_addresses = addresses;
    m_addresses_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_addresses_Set() const{
    return m_addresses_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_addresses_Valid() const{
    return m_addresses_isValid;
}

QString OAIGetTransactionV2_200_response_vin_inner::getHex() const {
    return m_hex;
}
void OAIGetTransactionV2_200_response_vin_inner::setHex(const QString &hex) {
    m_hex = hex;
    m_hex_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_hex_Set() const{
    return m_hex_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_hex_Valid() const{
    return m_hex_isValid;
}

bool OAIGetTransactionV2_200_response_vin_inner::isIsAddress() const {
    return m_is_address;
}
void OAIGetTransactionV2_200_response_vin_inner::setIsAddress(const bool &is_address) {
    m_is_address = is_address;
    m_is_address_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_is_address_Set() const{
    return m_is_address_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_is_address_Valid() const{
    return m_is_address_isValid;
}

qint32 OAIGetTransactionV2_200_response_vin_inner::getN() const {
    return m_n;
}
void OAIGetTransactionV2_200_response_vin_inner::setN(const qint32 &n) {
    m_n = n;
    m_n_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_n_Set() const{
    return m_n_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_n_Valid() const{
    return m_n_isValid;
}

qint32 OAIGetTransactionV2_200_response_vin_inner::getSequence() const {
    return m_sequence;
}
void OAIGetTransactionV2_200_response_vin_inner::setSequence(const qint32 &sequence) {
    m_sequence = sequence;
    m_sequence_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_sequence_Set() const{
    return m_sequence_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_sequence_Valid() const{
    return m_sequence_isValid;
}

QString OAIGetTransactionV2_200_response_vin_inner::getTxid() const {
    return m_txid;
}
void OAIGetTransactionV2_200_response_vin_inner::setTxid(const QString &txid) {
    m_txid = txid;
    m_txid_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_txid_Set() const{
    return m_txid_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_txid_Valid() const{
    return m_txid_isValid;
}

QString OAIGetTransactionV2_200_response_vin_inner::getValue() const {
    return m_value;
}
void OAIGetTransactionV2_200_response_vin_inner::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_value_Valid() const{
    return m_value_isValid;
}

qint32 OAIGetTransactionV2_200_response_vin_inner::getVout() const {
    return m_vout;
}
void OAIGetTransactionV2_200_response_vin_inner::setVout(const qint32 &vout) {
    m_vout = vout;
    m_vout_isSet = true;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_vout_Set() const{
    return m_vout_isSet;
}

bool OAIGetTransactionV2_200_response_vin_inner::is_vout_Valid() const{
    return m_vout_isValid;
}

bool OAIGetTransactionV2_200_response_vin_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hex_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_n_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sequence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_txid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vout_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetTransactionV2_200_response_vin_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
