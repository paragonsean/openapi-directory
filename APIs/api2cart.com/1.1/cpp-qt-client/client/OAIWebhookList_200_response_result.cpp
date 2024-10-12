/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebhookList_200_response_result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebhookList_200_response_result::OAIWebhookList_200_response_result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebhookList_200_response_result::OAIWebhookList_200_response_result() {
    this->initializeModel();
}

OAIWebhookList_200_response_result::~OAIWebhookList_200_response_result() {}

void OAIWebhookList_200_response_result::initializeModel() {

    m_webhook_isSet = false;
    m_webhook_isValid = false;
}

void OAIWebhookList_200_response_result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebhookList_200_response_result::fromJsonObject(QJsonObject json) {

    m_webhook_isValid = ::OpenAPI::fromJsonValue(m_webhook, json[QString("webhook")]);
    m_webhook_isSet = !json[QString("webhook")].isNull() && m_webhook_isValid;
}

QString OAIWebhookList_200_response_result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebhookList_200_response_result::asJsonObject() const {
    QJsonObject obj;
    if (m_webhook.size() > 0) {
        obj.insert(QString("webhook"), ::OpenAPI::toJsonValue(m_webhook));
    }
    return obj;
}

QList<OAIWebhook> OAIWebhookList_200_response_result::getWebhook() const {
    return m_webhook;
}
void OAIWebhookList_200_response_result::setWebhook(const QList<OAIWebhook> &webhook) {
    m_webhook = webhook;
    m_webhook_isSet = true;
}

bool OAIWebhookList_200_response_result::is_webhook_Set() const{
    return m_webhook_isSet;
}

bool OAIWebhookList_200_response_result::is_webhook_Valid() const{
    return m_webhook_isValid;
}

bool OAIWebhookList_200_response_result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_webhook.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebhookList_200_response_result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
