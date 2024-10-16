/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPreviewFileResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPreviewFileResponse::OAIPreviewFileResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPreviewFileResponse::OAIPreviewFileResponse() {
    this->initializeModel();
}

OAIPreviewFileResponse::~OAIPreviewFileResponse() {}

void OAIPreviewFileResponse::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_response_status_isSet = false;
    m_response_status_isValid = false;
}

void OAIPreviewFileResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPreviewFileResponse::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_response_status_isValid = ::OpenAPI::fromJsonValue(m_response_status, json[QString("responseStatus")]);
    m_response_status_isSet = !json[QString("responseStatus")].isNull() && m_response_status_isValid;
}

QString OAIPreviewFileResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPreviewFileResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_response_status_isSet) {
        obj.insert(QString("responseStatus"), ::OpenAPI::toJsonValue(m_response_status));
    }
    return obj;
}

OAIPreviewFile OAIPreviewFileResponse::getData() const {
    return m_data;
}
void OAIPreviewFileResponse::setData(const OAIPreviewFile &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIPreviewFileResponse::is_data_Set() const{
    return m_data_isSet;
}

bool OAIPreviewFileResponse::is_data_Valid() const{
    return m_data_isValid;
}

qint32 OAIPreviewFileResponse::getResponseStatus() const {
    return m_response_status;
}
void OAIPreviewFileResponse::setResponseStatus(const qint32 &response_status) {
    m_response_status = response_status;
    m_response_status_isSet = true;
}

bool OAIPreviewFileResponse::is_response_status_Set() const{
    return m_response_status_isSet;
}

bool OAIPreviewFileResponse::is_response_status_Valid() const{
    return m_response_status_isValid;
}

bool OAIPreviewFileResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_response_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPreviewFileResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
