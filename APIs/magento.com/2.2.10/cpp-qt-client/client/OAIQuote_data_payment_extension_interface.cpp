/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQuote_data_payment_extension_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuote_data_payment_extension_interface::OAIQuote_data_payment_extension_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuote_data_payment_extension_interface::OAIQuote_data_payment_extension_interface() {
    this->initializeModel();
}

OAIQuote_data_payment_extension_interface::~OAIQuote_data_payment_extension_interface() {}

void OAIQuote_data_payment_extension_interface::initializeModel() {

    m_agreement_ids_isSet = false;
    m_agreement_ids_isValid = false;
}

void OAIQuote_data_payment_extension_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuote_data_payment_extension_interface::fromJsonObject(QJsonObject json) {

    m_agreement_ids_isValid = ::OpenAPI::fromJsonValue(m_agreement_ids, json[QString("agreement_ids")]);
    m_agreement_ids_isSet = !json[QString("agreement_ids")].isNull() && m_agreement_ids_isValid;
}

QString OAIQuote_data_payment_extension_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuote_data_payment_extension_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_agreement_ids.size() > 0) {
        obj.insert(QString("agreement_ids"), ::OpenAPI::toJsonValue(m_agreement_ids));
    }
    return obj;
}

QList<QString> OAIQuote_data_payment_extension_interface::getAgreementIds() const {
    return m_agreement_ids;
}
void OAIQuote_data_payment_extension_interface::setAgreementIds(const QList<QString> &agreement_ids) {
    m_agreement_ids = agreement_ids;
    m_agreement_ids_isSet = true;
}

bool OAIQuote_data_payment_extension_interface::is_agreement_ids_Set() const{
    return m_agreement_ids_isSet;
}

bool OAIQuote_data_payment_extension_interface::is_agreement_ids_Valid() const{
    return m_agreement_ids_isValid;
}

bool OAIQuote_data_payment_extension_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_agreement_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuote_data_payment_extension_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
