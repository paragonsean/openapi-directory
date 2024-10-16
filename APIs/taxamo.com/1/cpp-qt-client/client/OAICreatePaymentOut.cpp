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

#include "OAICreatePaymentOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreatePaymentOut::OAICreatePaymentOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreatePaymentOut::OAICreatePaymentOut() {
    this->initializeModel();
}

OAICreatePaymentOut::~OAICreatePaymentOut() {}

void OAICreatePaymentOut::initializeModel() {

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAICreatePaymentOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreatePaymentOut::fromJsonObject(QJsonObject json) {

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAICreatePaymentOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreatePaymentOut::asJsonObject() const {
    QJsonObject obj;
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

bool OAICreatePaymentOut::isSuccess() const {
    return m_success;
}
void OAICreatePaymentOut::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAICreatePaymentOut::is_success_Set() const{
    return m_success_isSet;
}

bool OAICreatePaymentOut::is_success_Valid() const{
    return m_success_isValid;
}

bool OAICreatePaymentOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreatePaymentOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
