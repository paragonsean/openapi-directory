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

#include "OAICalculateTaxIn.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICalculateTaxIn::OAICalculateTaxIn(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICalculateTaxIn::OAICalculateTaxIn() {
    this->initializeModel();
}

OAICalculateTaxIn::~OAICalculateTaxIn() {}

void OAICalculateTaxIn::initializeModel() {

    m_transaction_isSet = false;
    m_transaction_isValid = false;
}

void OAICalculateTaxIn::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICalculateTaxIn::fromJsonObject(QJsonObject json) {

    m_transaction_isValid = ::OpenAPI::fromJsonValue(m_transaction, json[QString("transaction")]);
    m_transaction_isSet = !json[QString("transaction")].isNull() && m_transaction_isValid;
}

QString OAICalculateTaxIn::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICalculateTaxIn::asJsonObject() const {
    QJsonObject obj;
    if (m_transaction.isSet()) {
        obj.insert(QString("transaction"), ::OpenAPI::toJsonValue(m_transaction));
    }
    return obj;
}

OAIInput_transaction OAICalculateTaxIn::getTransaction() const {
    return m_transaction;
}
void OAICalculateTaxIn::setTransaction(const OAIInput_transaction &transaction) {
    m_transaction = transaction;
    m_transaction_isSet = true;
}

bool OAICalculateTaxIn::is_transaction_Set() const{
    return m_transaction_isSet;
}

bool OAICalculateTaxIn::is_transaction_Valid() const{
    return m_transaction_isValid;
}

bool OAICalculateTaxIn::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_transaction.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICalculateTaxIn::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_transaction_isValid && true;
}

} // namespace OpenAPI
