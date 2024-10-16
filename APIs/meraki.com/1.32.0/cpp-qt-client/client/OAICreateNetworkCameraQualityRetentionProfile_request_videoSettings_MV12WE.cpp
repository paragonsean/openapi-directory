/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE() {
    this->initializeModel();
}

OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::~OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE() {}

void OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::initializeModel() {

    m_quality_isSet = false;
    m_quality_isValid = false;

    m_resolution_isSet = false;
    m_resolution_isValid = false;
}

void OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::fromJsonObject(QJsonObject json) {

    m_quality_isValid = ::OpenAPI::fromJsonValue(m_quality, json[QString("quality")]);
    m_quality_isSet = !json[QString("quality")].isNull() && m_quality_isValid;

    m_resolution_isValid = ::OpenAPI::fromJsonValue(m_resolution, json[QString("resolution")]);
    m_resolution_isSet = !json[QString("resolution")].isNull() && m_resolution_isValid;
}

QString OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::asJsonObject() const {
    QJsonObject obj;
    if (m_quality_isSet) {
        obj.insert(QString("quality"), ::OpenAPI::toJsonValue(m_quality));
    }
    if (m_resolution_isSet) {
        obj.insert(QString("resolution"), ::OpenAPI::toJsonValue(m_resolution));
    }
    return obj;
}

QString OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::getQuality() const {
    return m_quality;
}
void OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::setQuality(const QString &quality) {
    m_quality = quality;
    m_quality_isSet = true;
}

bool OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::is_quality_Set() const{
    return m_quality_isSet;
}

bool OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::is_quality_Valid() const{
    return m_quality_isValid;
}

QString OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::getResolution() const {
    return m_resolution;
}
void OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::setResolution(const QString &resolution) {
    m_resolution = resolution;
    m_resolution_isSet = true;
}

bool OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::is_resolution_Set() const{
    return m_resolution_isSet;
}

bool OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::is_resolution_Valid() const{
    return m_resolution_isValid;
}

bool OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_quality_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolution_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateNetworkCameraQualityRetentionProfile_request_videoSettings_MV12WE::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_quality_isValid && m_resolution_isValid && true;
}

} // namespace OpenAPI
