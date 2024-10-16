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

#include "OAIAdditional_currencies.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAdditional_currencies::OAIAdditional_currencies(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAdditional_currencies::OAIAdditional_currencies() {
    this->initializeModel();
}

OAIAdditional_currencies::~OAIAdditional_currencies() {}

void OAIAdditional_currencies::initializeModel() {

    m_invoice_isSet = false;
    m_invoice_isValid = false;
}

void OAIAdditional_currencies::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAdditional_currencies::fromJsonObject(QJsonObject json) {

    m_invoice_isValid = ::OpenAPI::fromJsonValue(m_invoice, json[QString("invoice")]);
    m_invoice_isSet = !json[QString("invoice")].isNull() && m_invoice_isValid;
}

QString OAIAdditional_currencies::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAdditional_currencies::asJsonObject() const {
    QJsonObject obj;
    if (m_invoice.isSet()) {
        obj.insert(QString("invoice"), ::OpenAPI::toJsonValue(m_invoice));
    }
    return obj;
}

OAIAdditional_currency OAIAdditional_currencies::getInvoice() const {
    return m_invoice;
}
void OAIAdditional_currencies::setInvoice(const OAIAdditional_currency &invoice) {
    m_invoice = invoice;
    m_invoice_isSet = true;
}

bool OAIAdditional_currencies::is_invoice_Set() const{
    return m_invoice_isSet;
}

bool OAIAdditional_currencies::is_invoice_Valid() const{
    return m_invoice_isValid;
}

bool OAIAdditional_currencies::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_invoice.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAdditional_currencies::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
