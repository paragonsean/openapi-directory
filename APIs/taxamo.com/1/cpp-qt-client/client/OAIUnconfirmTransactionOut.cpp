/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUnconfirmTransactionOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUnconfirmTransactionOut::OAIUnconfirmTransactionOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUnconfirmTransactionOut::OAIUnconfirmTransactionOut() {
    this->initializeModel();
}

OAIUnconfirmTransactionOut::~OAIUnconfirmTransactionOut() {}

void OAIUnconfirmTransactionOut::initializeModel() {

    m_storage_required_fields_isSet = false;
    m_storage_required_fields_isValid = false;

    m_tax_required_fields_isSet = false;
    m_tax_required_fields_isValid = false;

    m_transaction_isSet = false;
    m_transaction_isValid = false;
}

void OAIUnconfirmTransactionOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUnconfirmTransactionOut::fromJsonObject(QJsonObject json) {

    m_storage_required_fields_isValid = ::OpenAPI::fromJsonValue(m_storage_required_fields, json[QString("storage_required_fields")]);
    m_storage_required_fields_isSet = !json[QString("storage_required_fields")].isNull() && m_storage_required_fields_isValid;

    m_tax_required_fields_isValid = ::OpenAPI::fromJsonValue(m_tax_required_fields, json[QString("tax_required_fields")]);
    m_tax_required_fields_isSet = !json[QString("tax_required_fields")].isNull() && m_tax_required_fields_isValid;

    m_transaction_isValid = ::OpenAPI::fromJsonValue(m_transaction, json[QString("transaction")]);
    m_transaction_isSet = !json[QString("transaction")].isNull() && m_transaction_isValid;
}

QString OAIUnconfirmTransactionOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUnconfirmTransactionOut::asJsonObject() const {
    QJsonObject obj;
    if (m_storage_required_fields.size() > 0) {
        obj.insert(QString("storage_required_fields"), ::OpenAPI::toJsonValue(m_storage_required_fields));
    }
    if (m_tax_required_fields.size() > 0) {
        obj.insert(QString("tax_required_fields"), ::OpenAPI::toJsonValue(m_tax_required_fields));
    }
    if (m_transaction.isSet()) {
        obj.insert(QString("transaction"), ::OpenAPI::toJsonValue(m_transaction));
    }
    return obj;
}

QList<OAIStorage_required_fields> OAIUnconfirmTransactionOut::getStorageRequiredFields() const {
    return m_storage_required_fields;
}
void OAIUnconfirmTransactionOut::setStorageRequiredFields(const QList<OAIStorage_required_fields> &storage_required_fields) {
    m_storage_required_fields = storage_required_fields;
    m_storage_required_fields_isSet = true;
}

bool OAIUnconfirmTransactionOut::is_storage_required_fields_Set() const{
    return m_storage_required_fields_isSet;
}

bool OAIUnconfirmTransactionOut::is_storage_required_fields_Valid() const{
    return m_storage_required_fields_isValid;
}

QList<OAITax_required_fields> OAIUnconfirmTransactionOut::getTaxRequiredFields() const {
    return m_tax_required_fields;
}
void OAIUnconfirmTransactionOut::setTaxRequiredFields(const QList<OAITax_required_fields> &tax_required_fields) {
    m_tax_required_fields = tax_required_fields;
    m_tax_required_fields_isSet = true;
}

bool OAIUnconfirmTransactionOut::is_tax_required_fields_Set() const{
    return m_tax_required_fields_isSet;
}

bool OAIUnconfirmTransactionOut::is_tax_required_fields_Valid() const{
    return m_tax_required_fields_isValid;
}

OAITransaction OAIUnconfirmTransactionOut::getTransaction() const {
    return m_transaction;
}
void OAIUnconfirmTransactionOut::setTransaction(const OAITransaction &transaction) {
    m_transaction = transaction;
    m_transaction_isSet = true;
}

bool OAIUnconfirmTransactionOut::is_transaction_Set() const{
    return m_transaction_isSet;
}

bool OAIUnconfirmTransactionOut::is_transaction_Valid() const{
    return m_transaction_isValid;
}

bool OAIUnconfirmTransactionOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_storage_required_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_required_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUnconfirmTransactionOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
