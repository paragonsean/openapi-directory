/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOperationBatchStatusResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOperationBatchStatusResponse::OAIOperationBatchStatusResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOperationBatchStatusResponse::OAIOperationBatchStatusResponse() {
    this->initializeModel();
}

OAIOperationBatchStatusResponse::~OAIOperationBatchStatusResponse() {}

void OAIOperationBatchStatusResponse::initializeModel() {

    m_items_isSet = false;
    m_items_isValid = false;
}

void OAIOperationBatchStatusResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOperationBatchStatusResponse::fromJsonObject(QJsonObject json) {

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;
}

QString OAIOperationBatchStatusResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOperationBatchStatusResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    return obj;
}

QList<OAIOperationBatchStatusResponseItem> OAIOperationBatchStatusResponse::getItems() const {
    return m_items;
}
void OAIOperationBatchStatusResponse::setItems(const QList<OAIOperationBatchStatusResponseItem> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIOperationBatchStatusResponse::is_items_Set() const{
    return m_items_isSet;
}

bool OAIOperationBatchStatusResponse::is_items_Valid() const{
    return m_items_isValid;
}

bool OAIOperationBatchStatusResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOperationBatchStatusResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
