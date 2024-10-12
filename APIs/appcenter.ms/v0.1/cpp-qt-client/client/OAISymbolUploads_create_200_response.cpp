/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISymbolUploads_create_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISymbolUploads_create_200_response::OAISymbolUploads_create_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISymbolUploads_create_200_response::OAISymbolUploads_create_200_response() {
    this->initializeModel();
}

OAISymbolUploads_create_200_response::~OAISymbolUploads_create_200_response() {}

void OAISymbolUploads_create_200_response::initializeModel() {

    m_expiration_date_isSet = false;
    m_expiration_date_isValid = false;

    m_symbol_upload_id_isSet = false;
    m_symbol_upload_id_isValid = false;

    m_upload_url_isSet = false;
    m_upload_url_isValid = false;
}

void OAISymbolUploads_create_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISymbolUploads_create_200_response::fromJsonObject(QJsonObject json) {

    m_expiration_date_isValid = ::OpenAPI::fromJsonValue(m_expiration_date, json[QString("expiration_date")]);
    m_expiration_date_isSet = !json[QString("expiration_date")].isNull() && m_expiration_date_isValid;

    m_symbol_upload_id_isValid = ::OpenAPI::fromJsonValue(m_symbol_upload_id, json[QString("symbol_upload_id")]);
    m_symbol_upload_id_isSet = !json[QString("symbol_upload_id")].isNull() && m_symbol_upload_id_isValid;

    m_upload_url_isValid = ::OpenAPI::fromJsonValue(m_upload_url, json[QString("upload_url")]);
    m_upload_url_isSet = !json[QString("upload_url")].isNull() && m_upload_url_isValid;
}

QString OAISymbolUploads_create_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISymbolUploads_create_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_expiration_date_isSet) {
        obj.insert(QString("expiration_date"), ::OpenAPI::toJsonValue(m_expiration_date));
    }
    if (m_symbol_upload_id_isSet) {
        obj.insert(QString("symbol_upload_id"), ::OpenAPI::toJsonValue(m_symbol_upload_id));
    }
    if (m_upload_url_isSet) {
        obj.insert(QString("upload_url"), ::OpenAPI::toJsonValue(m_upload_url));
    }
    return obj;
}

QDateTime OAISymbolUploads_create_200_response::getExpirationDate() const {
    return m_expiration_date;
}
void OAISymbolUploads_create_200_response::setExpirationDate(const QDateTime &expiration_date) {
    m_expiration_date = expiration_date;
    m_expiration_date_isSet = true;
}

bool OAISymbolUploads_create_200_response::is_expiration_date_Set() const{
    return m_expiration_date_isSet;
}

bool OAISymbolUploads_create_200_response::is_expiration_date_Valid() const{
    return m_expiration_date_isValid;
}

QString OAISymbolUploads_create_200_response::getSymbolUploadId() const {
    return m_symbol_upload_id;
}
void OAISymbolUploads_create_200_response::setSymbolUploadId(const QString &symbol_upload_id) {
    m_symbol_upload_id = symbol_upload_id;
    m_symbol_upload_id_isSet = true;
}

bool OAISymbolUploads_create_200_response::is_symbol_upload_id_Set() const{
    return m_symbol_upload_id_isSet;
}

bool OAISymbolUploads_create_200_response::is_symbol_upload_id_Valid() const{
    return m_symbol_upload_id_isValid;
}

QString OAISymbolUploads_create_200_response::getUploadUrl() const {
    return m_upload_url;
}
void OAISymbolUploads_create_200_response::setUploadUrl(const QString &upload_url) {
    m_upload_url = upload_url;
    m_upload_url_isSet = true;
}

bool OAISymbolUploads_create_200_response::is_upload_url_Set() const{
    return m_upload_url_isSet;
}

bool OAISymbolUploads_create_200_response::is_upload_url_Valid() const{
    return m_upload_url_isValid;
}

bool OAISymbolUploads_create_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_expiration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_symbol_upload_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upload_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISymbolUploads_create_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_expiration_date_isValid && m_symbol_upload_id_isValid && m_upload_url_isValid && true;
}

} // namespace OpenAPI
