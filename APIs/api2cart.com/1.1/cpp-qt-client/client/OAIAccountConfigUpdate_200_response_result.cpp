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

#include "OAIAccountConfigUpdate_200_response_result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccountConfigUpdate_200_response_result::OAIAccountConfigUpdate_200_response_result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccountConfigUpdate_200_response_result::OAIAccountConfigUpdate_200_response_result() {
    this->initializeModel();
}

OAIAccountConfigUpdate_200_response_result::~OAIAccountConfigUpdate_200_response_result() {}

void OAIAccountConfigUpdate_200_response_result::initializeModel() {

    m_updated_items_isSet = false;
    m_updated_items_isValid = false;
}

void OAIAccountConfigUpdate_200_response_result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccountConfigUpdate_200_response_result::fromJsonObject(QJsonObject json) {

    m_updated_items_isValid = ::OpenAPI::fromJsonValue(m_updated_items, json[QString("updated_items")]);
    m_updated_items_isSet = !json[QString("updated_items")].isNull() && m_updated_items_isValid;
}

QString OAIAccountConfigUpdate_200_response_result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccountConfigUpdate_200_response_result::asJsonObject() const {
    QJsonObject obj;
    if (m_updated_items_isSet) {
        obj.insert(QString("updated_items"), ::OpenAPI::toJsonValue(m_updated_items));
    }
    return obj;
}

qint32 OAIAccountConfigUpdate_200_response_result::getUpdatedItems() const {
    return m_updated_items;
}
void OAIAccountConfigUpdate_200_response_result::setUpdatedItems(const qint32 &updated_items) {
    m_updated_items = updated_items;
    m_updated_items_isSet = true;
}

bool OAIAccountConfigUpdate_200_response_result::is_updated_items_Set() const{
    return m_updated_items_isSet;
}

bool OAIAccountConfigUpdate_200_response_result::is_updated_items_Valid() const{
    return m_updated_items_isValid;
}

bool OAIAccountConfigUpdate_200_response_result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_updated_items_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccountConfigUpdate_200_response_result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
