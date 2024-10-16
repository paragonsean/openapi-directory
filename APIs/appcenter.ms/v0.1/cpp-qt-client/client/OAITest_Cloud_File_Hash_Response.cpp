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

#include "OAITest_Cloud_File_Hash_Response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITest_Cloud_File_Hash_Response::OAITest_Cloud_File_Hash_Response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITest_Cloud_File_Hash_Response::OAITest_Cloud_File_Hash_Response() {
    this->initializeModel();
}

OAITest_Cloud_File_Hash_Response::~OAITest_Cloud_File_Hash_Response() {}

void OAITest_Cloud_File_Hash_Response::initializeModel() {

    m_checksum_isSet = false;
    m_checksum_isValid = false;

    m_file_type_isSet = false;
    m_file_type_isValid = false;

    m_relative_path_isSet = false;
    m_relative_path_isValid = false;

    m_upload_status_isSet = false;
    m_upload_status_isValid = false;
}

void OAITest_Cloud_File_Hash_Response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITest_Cloud_File_Hash_Response::fromJsonObject(QJsonObject json) {

    m_checksum_isValid = ::OpenAPI::fromJsonValue(m_checksum, json[QString("checksum")]);
    m_checksum_isSet = !json[QString("checksum")].isNull() && m_checksum_isValid;

    m_file_type_isValid = ::OpenAPI::fromJsonValue(m_file_type, json[QString("fileType")]);
    m_file_type_isSet = !json[QString("fileType")].isNull() && m_file_type_isValid;

    m_relative_path_isValid = ::OpenAPI::fromJsonValue(m_relative_path, json[QString("relativePath")]);
    m_relative_path_isSet = !json[QString("relativePath")].isNull() && m_relative_path_isValid;

    m_upload_status_isValid = ::OpenAPI::fromJsonValue(m_upload_status, json[QString("uploadStatus")]);
    m_upload_status_isSet = !json[QString("uploadStatus")].isNull() && m_upload_status_isValid;
}

QString OAITest_Cloud_File_Hash_Response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITest_Cloud_File_Hash_Response::asJsonObject() const {
    QJsonObject obj;
    if (m_checksum_isSet) {
        obj.insert(QString("checksum"), ::OpenAPI::toJsonValue(m_checksum));
    }
    if (m_file_type_isSet) {
        obj.insert(QString("fileType"), ::OpenAPI::toJsonValue(m_file_type));
    }
    if (m_relative_path_isSet) {
        obj.insert(QString("relativePath"), ::OpenAPI::toJsonValue(m_relative_path));
    }
    if (m_upload_status.isSet()) {
        obj.insert(QString("uploadStatus"), ::OpenAPI::toJsonValue(m_upload_status));
    }
    return obj;
}

QString OAITest_Cloud_File_Hash_Response::getChecksum() const {
    return m_checksum;
}
void OAITest_Cloud_File_Hash_Response::setChecksum(const QString &checksum) {
    m_checksum = checksum;
    m_checksum_isSet = true;
}

bool OAITest_Cloud_File_Hash_Response::is_checksum_Set() const{
    return m_checksum_isSet;
}

bool OAITest_Cloud_File_Hash_Response::is_checksum_Valid() const{
    return m_checksum_isValid;
}

QString OAITest_Cloud_File_Hash_Response::getFileType() const {
    return m_file_type;
}
void OAITest_Cloud_File_Hash_Response::setFileType(const QString &file_type) {
    m_file_type = file_type;
    m_file_type_isSet = true;
}

bool OAITest_Cloud_File_Hash_Response::is_file_type_Set() const{
    return m_file_type_isSet;
}

bool OAITest_Cloud_File_Hash_Response::is_file_type_Valid() const{
    return m_file_type_isValid;
}

QString OAITest_Cloud_File_Hash_Response::getRelativePath() const {
    return m_relative_path;
}
void OAITest_Cloud_File_Hash_Response::setRelativePath(const QString &relative_path) {
    m_relative_path = relative_path;
    m_relative_path_isSet = true;
}

bool OAITest_Cloud_File_Hash_Response::is_relative_path_Set() const{
    return m_relative_path_isSet;
}

bool OAITest_Cloud_File_Hash_Response::is_relative_path_Valid() const{
    return m_relative_path_isValid;
}

OAITest_Cloud_Hash_Upload_Status OAITest_Cloud_File_Hash_Response::getUploadStatus() const {
    return m_upload_status;
}
void OAITest_Cloud_File_Hash_Response::setUploadStatus(const OAITest_Cloud_Hash_Upload_Status &upload_status) {
    m_upload_status = upload_status;
    m_upload_status_isSet = true;
}

bool OAITest_Cloud_File_Hash_Response::is_upload_status_Set() const{
    return m_upload_status_isSet;
}

bool OAITest_Cloud_File_Hash_Response::is_upload_status_Valid() const{
    return m_upload_status_isValid;
}

bool OAITest_Cloud_File_Hash_Response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_checksum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relative_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upload_status.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITest_Cloud_File_Hash_Response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_checksum_isValid && m_file_type_isValid && m_upload_status_isValid && true;
}

} // namespace OpenAPI
