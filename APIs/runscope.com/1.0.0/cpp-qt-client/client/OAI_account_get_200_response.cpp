/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_account_get_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_account_get_200_response::OAI_account_get_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_account_get_200_response::OAI_account_get_200_response() {
    this->initializeModel();
}

OAI_account_get_200_response::~OAI_account_get_200_response() {}

void OAI_account_get_200_response::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_meta_isSet = false;
    m_meta_isValid = false;
}

void OAI_account_get_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_account_get_200_response::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_meta_isValid = ::OpenAPI::fromJsonValue(m_meta, json[QString("meta")]);
    m_meta_isSet = !json[QString("meta")].isNull() && m_meta_isValid;
}

QString OAI_account_get_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_account_get_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_meta.isSet()) {
        obj.insert(QString("meta"), ::OpenAPI::toJsonValue(m_meta));
    }
    return obj;
}

OAIAccount OAI_account_get_200_response::getData() const {
    return m_data;
}
void OAI_account_get_200_response::setData(const OAIAccount &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAI_account_get_200_response::is_data_Set() const{
    return m_data_isSet;
}

bool OAI_account_get_200_response::is_data_Valid() const{
    return m_data_isValid;
}

OAIMeta OAI_account_get_200_response::getMeta() const {
    return m_meta;
}
void OAI_account_get_200_response::setMeta(const OAIMeta &meta) {
    m_meta = meta;
    m_meta_isSet = true;
}

bool OAI_account_get_200_response::is_meta_Set() const{
    return m_meta_isSet;
}

bool OAI_account_get_200_response::is_meta_Valid() const{
    return m_meta_isValid;
}

bool OAI_account_get_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_account_get_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
