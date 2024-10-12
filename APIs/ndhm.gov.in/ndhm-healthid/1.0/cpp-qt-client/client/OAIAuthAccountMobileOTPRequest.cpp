/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthAccountMobileOTPRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthAccountMobileOTPRequest::OAIAuthAccountMobileOTPRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthAccountMobileOTPRequest::OAIAuthAccountMobileOTPRequest() {
    this->initializeModel();
}

OAIAuthAccountMobileOTPRequest::~OAIAuthAccountMobileOTPRequest() {}

void OAIAuthAccountMobileOTPRequest::initializeModel() {

    m_otp_isSet = false;
    m_otp_isValid = false;

    m_txn_id_isSet = false;
    m_txn_id_isValid = false;
}

void OAIAuthAccountMobileOTPRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthAccountMobileOTPRequest::fromJsonObject(QJsonObject json) {

    m_otp_isValid = ::OpenAPI::fromJsonValue(m_otp, json[QString("otp")]);
    m_otp_isSet = !json[QString("otp")].isNull() && m_otp_isValid;

    m_txn_id_isValid = ::OpenAPI::fromJsonValue(m_txn_id, json[QString("txnId")]);
    m_txn_id_isSet = !json[QString("txnId")].isNull() && m_txn_id_isValid;
}

QString OAIAuthAccountMobileOTPRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthAccountMobileOTPRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_otp_isSet) {
        obj.insert(QString("otp"), ::OpenAPI::toJsonValue(m_otp));
    }
    if (m_txn_id_isSet) {
        obj.insert(QString("txnId"), ::OpenAPI::toJsonValue(m_txn_id));
    }
    return obj;
}

QString OAIAuthAccountMobileOTPRequest::getOtp() const {
    return m_otp;
}
void OAIAuthAccountMobileOTPRequest::setOtp(const QString &otp) {
    m_otp = otp;
    m_otp_isSet = true;
}

bool OAIAuthAccountMobileOTPRequest::is_otp_Set() const{
    return m_otp_isSet;
}

bool OAIAuthAccountMobileOTPRequest::is_otp_Valid() const{
    return m_otp_isValid;
}

QString OAIAuthAccountMobileOTPRequest::getTxnId() const {
    return m_txn_id;
}
void OAIAuthAccountMobileOTPRequest::setTxnId(const QString &txn_id) {
    m_txn_id = txn_id;
    m_txn_id_isSet = true;
}

bool OAIAuthAccountMobileOTPRequest::is_txn_id_Set() const{
    return m_txn_id_isSet;
}

bool OAIAuthAccountMobileOTPRequest::is_txn_id_Valid() const{
    return m_txn_id_isValid;
}

bool OAIAuthAccountMobileOTPRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_otp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_txn_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthAccountMobileOTPRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
