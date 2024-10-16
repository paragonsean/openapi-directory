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

#include "OAIReleases_updateReleaseUploadStatus_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReleases_updateReleaseUploadStatus_request::OAIReleases_updateReleaseUploadStatus_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReleases_updateReleaseUploadStatus_request::OAIReleases_updateReleaseUploadStatus_request() {
    this->initializeModel();
}

OAIReleases_updateReleaseUploadStatus_request::~OAIReleases_updateReleaseUploadStatus_request() {}

void OAIReleases_updateReleaseUploadStatus_request::initializeModel() {

    m_upload_status_isSet = false;
    m_upload_status_isValid = false;
}

void OAIReleases_updateReleaseUploadStatus_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReleases_updateReleaseUploadStatus_request::fromJsonObject(QJsonObject json) {

    m_upload_status_isValid = ::OpenAPI::fromJsonValue(m_upload_status, json[QString("upload_status")]);
    m_upload_status_isSet = !json[QString("upload_status")].isNull() && m_upload_status_isValid;
}

QString OAIReleases_updateReleaseUploadStatus_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReleases_updateReleaseUploadStatus_request::asJsonObject() const {
    QJsonObject obj;
    if (m_upload_status_isSet) {
        obj.insert(QString("upload_status"), ::OpenAPI::toJsonValue(m_upload_status));
    }
    return obj;
}

QString OAIReleases_updateReleaseUploadStatus_request::getUploadStatus() const {
    return m_upload_status;
}
void OAIReleases_updateReleaseUploadStatus_request::setUploadStatus(const QString &upload_status) {
    m_upload_status = upload_status;
    m_upload_status_isSet = true;
}

bool OAIReleases_updateReleaseUploadStatus_request::is_upload_status_Set() const{
    return m_upload_status_isSet;
}

bool OAIReleases_updateReleaseUploadStatus_request::is_upload_status_Valid() const{
    return m_upload_status_isValid;
}

bool OAIReleases_updateReleaseUploadStatus_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_upload_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIReleases_updateReleaseUploadStatus_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_upload_status_isValid && true;
}

} // namespace OpenAPI
