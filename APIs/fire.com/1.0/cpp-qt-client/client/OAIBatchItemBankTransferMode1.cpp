/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBatchItemBankTransferMode1.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBatchItemBankTransferMode1::OAIBatchItemBankTransferMode1(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBatchItemBankTransferMode1::OAIBatchItemBankTransferMode1() {
    this->initializeModel();
}

OAIBatchItemBankTransferMode1::~OAIBatchItemBankTransferMode1() {}

void OAIBatchItemBankTransferMode1::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_ican_from_isSet = false;
    m_ican_from_isValid = false;

    m_my_ref_isSet = false;
    m_my_ref_isValid = false;

    m_payee_id_isSet = false;
    m_payee_id_isValid = false;

    m_payee_type_isSet = false;
    m_payee_type_isValid = false;

    m_your_ref_isSet = false;
    m_your_ref_isValid = false;
}

void OAIBatchItemBankTransferMode1::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBatchItemBankTransferMode1::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_ican_from_isValid = ::OpenAPI::fromJsonValue(m_ican_from, json[QString("icanFrom")]);
    m_ican_from_isSet = !json[QString("icanFrom")].isNull() && m_ican_from_isValid;

    m_my_ref_isValid = ::OpenAPI::fromJsonValue(m_my_ref, json[QString("myRef")]);
    m_my_ref_isSet = !json[QString("myRef")].isNull() && m_my_ref_isValid;

    m_payee_id_isValid = ::OpenAPI::fromJsonValue(m_payee_id, json[QString("payeeId")]);
    m_payee_id_isSet = !json[QString("payeeId")].isNull() && m_payee_id_isValid;

    m_payee_type_isValid = ::OpenAPI::fromJsonValue(m_payee_type, json[QString("payeeType")]);
    m_payee_type_isSet = !json[QString("payeeType")].isNull() && m_payee_type_isValid;

    m_your_ref_isValid = ::OpenAPI::fromJsonValue(m_your_ref, json[QString("yourRef")]);
    m_your_ref_isSet = !json[QString("yourRef")].isNull() && m_your_ref_isValid;
}

QString OAIBatchItemBankTransferMode1::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBatchItemBankTransferMode1::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_ican_from_isSet) {
        obj.insert(QString("icanFrom"), ::OpenAPI::toJsonValue(m_ican_from));
    }
    if (m_my_ref_isSet) {
        obj.insert(QString("myRef"), ::OpenAPI::toJsonValue(m_my_ref));
    }
    if (m_payee_id_isSet) {
        obj.insert(QString("payeeId"), ::OpenAPI::toJsonValue(m_payee_id));
    }
    if (m_payee_type_isSet) {
        obj.insert(QString("payeeType"), ::OpenAPI::toJsonValue(m_payee_type));
    }
    if (m_your_ref_isSet) {
        obj.insert(QString("yourRef"), ::OpenAPI::toJsonValue(m_your_ref));
    }
    return obj;
}

qint64 OAIBatchItemBankTransferMode1::getAmount() const {
    return m_amount;
}
void OAIBatchItemBankTransferMode1::setAmount(const qint64 &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIBatchItemBankTransferMode1::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIBatchItemBankTransferMode1::is_amount_Valid() const{
    return m_amount_isValid;
}

qint64 OAIBatchItemBankTransferMode1::getIcanFrom() const {
    return m_ican_from;
}
void OAIBatchItemBankTransferMode1::setIcanFrom(const qint64 &ican_from) {
    m_ican_from = ican_from;
    m_ican_from_isSet = true;
}

bool OAIBatchItemBankTransferMode1::is_ican_from_Set() const{
    return m_ican_from_isSet;
}

bool OAIBatchItemBankTransferMode1::is_ican_from_Valid() const{
    return m_ican_from_isValid;
}

QString OAIBatchItemBankTransferMode1::getMyRef() const {
    return m_my_ref;
}
void OAIBatchItemBankTransferMode1::setMyRef(const QString &my_ref) {
    m_my_ref = my_ref;
    m_my_ref_isSet = true;
}

bool OAIBatchItemBankTransferMode1::is_my_ref_Set() const{
    return m_my_ref_isSet;
}

bool OAIBatchItemBankTransferMode1::is_my_ref_Valid() const{
    return m_my_ref_isValid;
}

qint64 OAIBatchItemBankTransferMode1::getPayeeId() const {
    return m_payee_id;
}
void OAIBatchItemBankTransferMode1::setPayeeId(const qint64 &payee_id) {
    m_payee_id = payee_id;
    m_payee_id_isSet = true;
}

bool OAIBatchItemBankTransferMode1::is_payee_id_Set() const{
    return m_payee_id_isSet;
}

bool OAIBatchItemBankTransferMode1::is_payee_id_Valid() const{
    return m_payee_id_isValid;
}

QString OAIBatchItemBankTransferMode1::getPayeeType() const {
    return m_payee_type;
}
void OAIBatchItemBankTransferMode1::setPayeeType(const QString &payee_type) {
    m_payee_type = payee_type;
    m_payee_type_isSet = true;
}

bool OAIBatchItemBankTransferMode1::is_payee_type_Set() const{
    return m_payee_type_isSet;
}

bool OAIBatchItemBankTransferMode1::is_payee_type_Valid() const{
    return m_payee_type_isValid;
}

QString OAIBatchItemBankTransferMode1::getYourRef() const {
    return m_your_ref;
}
void OAIBatchItemBankTransferMode1::setYourRef(const QString &your_ref) {
    m_your_ref = your_ref;
    m_your_ref_isSet = true;
}

bool OAIBatchItemBankTransferMode1::is_your_ref_Set() const{
    return m_your_ref_isSet;
}

bool OAIBatchItemBankTransferMode1::is_your_ref_Valid() const{
    return m_your_ref_isValid;
}

bool OAIBatchItemBankTransferMode1::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ican_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_my_ref_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payee_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_your_ref_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBatchItemBankTransferMode1::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
