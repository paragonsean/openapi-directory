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

#include "OAIDataSubjectRighBlobContainerInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDataSubjectRighBlobContainerInfo::OAIDataSubjectRighBlobContainerInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDataSubjectRighBlobContainerInfo::OAIDataSubjectRighBlobContainerInfo() {
    this->initializeModel();
}

OAIDataSubjectRighBlobContainerInfo::~OAIDataSubjectRighBlobContainerInfo() {}

void OAIDataSubjectRighBlobContainerInfo::initializeModel() {

    m_blob_path_isSet = false;
    m_blob_path_isValid = false;

    m_sas_uri_isSet = false;
    m_sas_uri_isValid = false;
}

void OAIDataSubjectRighBlobContainerInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDataSubjectRighBlobContainerInfo::fromJsonObject(QJsonObject json) {

    m_blob_path_isValid = ::OpenAPI::fromJsonValue(m_blob_path, json[QString("blobPath")]);
    m_blob_path_isSet = !json[QString("blobPath")].isNull() && m_blob_path_isValid;

    m_sas_uri_isValid = ::OpenAPI::fromJsonValue(m_sas_uri, json[QString("sasUri")]);
    m_sas_uri_isSet = !json[QString("sasUri")].isNull() && m_sas_uri_isValid;
}

QString OAIDataSubjectRighBlobContainerInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDataSubjectRighBlobContainerInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_blob_path_isSet) {
        obj.insert(QString("blobPath"), ::OpenAPI::toJsonValue(m_blob_path));
    }
    if (m_sas_uri_isSet) {
        obj.insert(QString("sasUri"), ::OpenAPI::toJsonValue(m_sas_uri));
    }
    return obj;
}

QString OAIDataSubjectRighBlobContainerInfo::getBlobPath() const {
    return m_blob_path;
}
void OAIDataSubjectRighBlobContainerInfo::setBlobPath(const QString &blob_path) {
    m_blob_path = blob_path;
    m_blob_path_isSet = true;
}

bool OAIDataSubjectRighBlobContainerInfo::is_blob_path_Set() const{
    return m_blob_path_isSet;
}

bool OAIDataSubjectRighBlobContainerInfo::is_blob_path_Valid() const{
    return m_blob_path_isValid;
}

QString OAIDataSubjectRighBlobContainerInfo::getSasUri() const {
    return m_sas_uri;
}
void OAIDataSubjectRighBlobContainerInfo::setSasUri(const QString &sas_uri) {
    m_sas_uri = sas_uri;
    m_sas_uri_isSet = true;
}

bool OAIDataSubjectRighBlobContainerInfo::is_sas_uri_Set() const{
    return m_sas_uri_isSet;
}

bool OAIDataSubjectRighBlobContainerInfo::is_sas_uri_Valid() const{
    return m_sas_uri_isValid;
}

bool OAIDataSubjectRighBlobContainerInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_blob_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sas_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDataSubjectRighBlobContainerInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_blob_path_isValid && m_sas_uri_isValid && true;
}

} // namespace OpenAPI
