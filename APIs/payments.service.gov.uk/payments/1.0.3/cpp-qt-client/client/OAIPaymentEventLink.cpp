/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPaymentEventLink.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentEventLink::OAIPaymentEventLink(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentEventLink::OAIPaymentEventLink() {
    this->initializeModel();
}

OAIPaymentEventLink::~OAIPaymentEventLink() {}

void OAIPaymentEventLink::initializeModel() {

    m_payment_url_isSet = false;
    m_payment_url_isValid = false;
}

void OAIPaymentEventLink::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaymentEventLink::fromJsonObject(QJsonObject json) {

    m_payment_url_isValid = ::OpenAPI::fromJsonValue(m_payment_url, json[QString("payment_url")]);
    m_payment_url_isSet = !json[QString("payment_url")].isNull() && m_payment_url_isValid;
}

QString OAIPaymentEventLink::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaymentEventLink::asJsonObject() const {
    QJsonObject obj;
    if (m_payment_url.isSet()) {
        obj.insert(QString("payment_url"), ::OpenAPI::toJsonValue(m_payment_url));
    }
    return obj;
}

OAILink OAIPaymentEventLink::getPaymentUrl() const {
    return m_payment_url;
}
void OAIPaymentEventLink::setPaymentUrl(const OAILink &payment_url) {
    m_payment_url = payment_url;
    m_payment_url_isSet = true;
}

bool OAIPaymentEventLink::is_payment_url_Set() const{
    return m_payment_url_isSet;
}

bool OAIPaymentEventLink::is_payment_url_Valid() const{
    return m_payment_url_isValid;
}

bool OAIPaymentEventLink::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_payment_url.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPaymentEventLink::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
