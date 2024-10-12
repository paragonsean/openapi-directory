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

#include "OAIHidOtpRequestPaylaod.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHidOtpRequestPaylaod::OAIHidOtpRequestPaylaod(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHidOtpRequestPaylaod::OAIHidOtpRequestPaylaod() {
    this->initializeModel();
}

OAIHidOtpRequestPaylaod::~OAIHidOtpRequestPaylaod() {}

void OAIHidOtpRequestPaylaod::initializeModel() {

    m_new_password_isSet = false;
    m_new_password_isValid = false;

    m_otp_isSet = false;
    m_otp_isValid = false;

    m_txn_id_isSet = false;
    m_txn_id_isValid = false;
}

void OAIHidOtpRequestPaylaod::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHidOtpRequestPaylaod::fromJsonObject(QJsonObject json) {

    m_new_password_isValid = ::OpenAPI::fromJsonValue(m_new_password, json[QString("newPassword")]);
    m_new_password_isSet = !json[QString("newPassword")].isNull() && m_new_password_isValid;

    m_otp_isValid = ::OpenAPI::fromJsonValue(m_otp, json[QString("otp")]);
    m_otp_isSet = !json[QString("otp")].isNull() && m_otp_isValid;

    m_txn_id_isValid = ::OpenAPI::fromJsonValue(m_txn_id, json[QString("txnId")]);
    m_txn_id_isSet = !json[QString("txnId")].isNull() && m_txn_id_isValid;
}

QString OAIHidOtpRequestPaylaod::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHidOtpRequestPaylaod::asJsonObject() const {
    QJsonObject obj;
    if (m_new_password_isSet) {
        obj.insert(QString("newPassword"), ::OpenAPI::toJsonValue(m_new_password));
    }
    if (m_otp_isSet) {
        obj.insert(QString("otp"), ::OpenAPI::toJsonValue(m_otp));
    }
    if (m_txn_id_isSet) {
        obj.insert(QString("txnId"), ::OpenAPI::toJsonValue(m_txn_id));
    }
    return obj;
}

QString OAIHidOtpRequestPaylaod::getNewPassword() const {
    return m_new_password;
}
void OAIHidOtpRequestPaylaod::setNewPassword(const QString &new_password) {
    m_new_password = new_password;
    m_new_password_isSet = true;
}

bool OAIHidOtpRequestPaylaod::is_new_password_Set() const{
    return m_new_password_isSet;
}

bool OAIHidOtpRequestPaylaod::is_new_password_Valid() const{
    return m_new_password_isValid;
}

QString OAIHidOtpRequestPaylaod::getOtp() const {
    return m_otp;
}
void OAIHidOtpRequestPaylaod::setOtp(const QString &otp) {
    m_otp = otp;
    m_otp_isSet = true;
}

bool OAIHidOtpRequestPaylaod::is_otp_Set() const{
    return m_otp_isSet;
}

bool OAIHidOtpRequestPaylaod::is_otp_Valid() const{
    return m_otp_isValid;
}

QString OAIHidOtpRequestPaylaod::getTxnId() const {
    return m_txn_id;
}
void OAIHidOtpRequestPaylaod::setTxnId(const QString &txn_id) {
    m_txn_id = txn_id;
    m_txn_id_isSet = true;
}

bool OAIHidOtpRequestPaylaod::is_txn_id_Set() const{
    return m_txn_id_isSet;
}

bool OAIHidOtpRequestPaylaod::is_txn_id_Valid() const{
    return m_txn_id_isValid;
}

bool OAIHidOtpRequestPaylaod::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_new_password_isSet) {
            isObjectUpdated = true;
            break;
        }

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

bool OAIHidOtpRequestPaylaod::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
