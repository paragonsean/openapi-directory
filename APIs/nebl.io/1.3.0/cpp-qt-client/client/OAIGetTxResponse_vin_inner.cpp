/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetTxResponse_vin_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetTxResponse_vin_inner::OAIGetTxResponse_vin_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetTxResponse_vin_inner::OAIGetTxResponse_vin_inner() {
    this->initializeModel();
}

OAIGetTxResponse_vin_inner::~OAIGetTxResponse_vin_inner() {}

void OAIGetTxResponse_vin_inner::initializeModel() {

    m_n_isSet = false;
    m_n_isValid = false;

    m_script_sig_isSet = false;
    m_script_sig_isValid = false;

    m_sequence_isSet = false;
    m_sequence_isValid = false;

    m_txid_isSet = false;
    m_txid_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;

    m_value_sat_isSet = false;
    m_value_sat_isValid = false;

    m_vout_isSet = false;
    m_vout_isValid = false;
}

void OAIGetTxResponse_vin_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetTxResponse_vin_inner::fromJsonObject(QJsonObject json) {

    m_n_isValid = ::OpenAPI::fromJsonValue(m_n, json[QString("n")]);
    m_n_isSet = !json[QString("n")].isNull() && m_n_isValid;

    m_script_sig_isValid = ::OpenAPI::fromJsonValue(m_script_sig, json[QString("scriptSig")]);
    m_script_sig_isSet = !json[QString("scriptSig")].isNull() && m_script_sig_isValid;

    m_sequence_isValid = ::OpenAPI::fromJsonValue(m_sequence, json[QString("sequence")]);
    m_sequence_isSet = !json[QString("sequence")].isNull() && m_sequence_isValid;

    m_txid_isValid = ::OpenAPI::fromJsonValue(m_txid, json[QString("txid")]);
    m_txid_isSet = !json[QString("txid")].isNull() && m_txid_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_value_sat_isValid = ::OpenAPI::fromJsonValue(m_value_sat, json[QString("valueSat")]);
    m_value_sat_isSet = !json[QString("valueSat")].isNull() && m_value_sat_isValid;

    m_vout_isValid = ::OpenAPI::fromJsonValue(m_vout, json[QString("vout")]);
    m_vout_isSet = !json[QString("vout")].isNull() && m_vout_isValid;
}

QString OAIGetTxResponse_vin_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetTxResponse_vin_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_n_isSet) {
        obj.insert(QString("n"), ::OpenAPI::toJsonValue(m_n));
    }
    if (m_script_sig.isSet()) {
        obj.insert(QString("scriptSig"), ::OpenAPI::toJsonValue(m_script_sig));
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
    if (m_value_sat_isSet) {
        obj.insert(QString("valueSat"), ::OpenAPI::toJsonValue(m_value_sat));
    }
    if (m_vout_isSet) {
        obj.insert(QString("vout"), ::OpenAPI::toJsonValue(m_vout));
    }
    return obj;
}

double OAIGetTxResponse_vin_inner::getN() const {
    return m_n;
}
void OAIGetTxResponse_vin_inner::setN(const double &n) {
    m_n = n;
    m_n_isSet = true;
}

bool OAIGetTxResponse_vin_inner::is_n_Set() const{
    return m_n_isSet;
}

bool OAIGetTxResponse_vin_inner::is_n_Valid() const{
    return m_n_isValid;
}

OAIGetTransactionInfoResponse_vin_inner_scriptSig OAIGetTxResponse_vin_inner::getScriptSig() const {
    return m_script_sig;
}
void OAIGetTxResponse_vin_inner::setScriptSig(const OAIGetTransactionInfoResponse_vin_inner_scriptSig &script_sig) {
    m_script_sig = script_sig;
    m_script_sig_isSet = true;
}

bool OAIGetTxResponse_vin_inner::is_script_sig_Set() const{
    return m_script_sig_isSet;
}

bool OAIGetTxResponse_vin_inner::is_script_sig_Valid() const{
    return m_script_sig_isValid;
}

double OAIGetTxResponse_vin_inner::getSequence() const {
    return m_sequence;
}
void OAIGetTxResponse_vin_inner::setSequence(const double &sequence) {
    m_sequence = sequence;
    m_sequence_isSet = true;
}

bool OAIGetTxResponse_vin_inner::is_sequence_Set() const{
    return m_sequence_isSet;
}

bool OAIGetTxResponse_vin_inner::is_sequence_Valid() const{
    return m_sequence_isValid;
}

QString OAIGetTxResponse_vin_inner::getTxid() const {
    return m_txid;
}
void OAIGetTxResponse_vin_inner::setTxid(const QString &txid) {
    m_txid = txid;
    m_txid_isSet = true;
}

bool OAIGetTxResponse_vin_inner::is_txid_Set() const{
    return m_txid_isSet;
}

bool OAIGetTxResponse_vin_inner::is_txid_Valid() const{
    return m_txid_isValid;
}

double OAIGetTxResponse_vin_inner::getValue() const {
    return m_value;
}
void OAIGetTxResponse_vin_inner::setValue(const double &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIGetTxResponse_vin_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIGetTxResponse_vin_inner::is_value_Valid() const{
    return m_value_isValid;
}

double OAIGetTxResponse_vin_inner::getValueSat() const {
    return m_value_sat;
}
void OAIGetTxResponse_vin_inner::setValueSat(const double &value_sat) {
    m_value_sat = value_sat;
    m_value_sat_isSet = true;
}

bool OAIGetTxResponse_vin_inner::is_value_sat_Set() const{
    return m_value_sat_isSet;
}

bool OAIGetTxResponse_vin_inner::is_value_sat_Valid() const{
    return m_value_sat_isValid;
}

double OAIGetTxResponse_vin_inner::getVout() const {
    return m_vout;
}
void OAIGetTxResponse_vin_inner::setVout(const double &vout) {
    m_vout = vout;
    m_vout_isSet = true;
}

bool OAIGetTxResponse_vin_inner::is_vout_Set() const{
    return m_vout_isSet;
}

bool OAIGetTxResponse_vin_inner::is_vout_Valid() const{
    return m_vout_isValid;
}

bool OAIGetTxResponse_vin_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_n_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_script_sig.isSet()) {
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

        if (m_value_sat_isSet) {
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

bool OAIGetTxResponse_vin_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
