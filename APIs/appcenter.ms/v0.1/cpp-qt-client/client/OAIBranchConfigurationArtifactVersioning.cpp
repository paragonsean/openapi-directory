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

#include "OAIBranchConfigurationArtifactVersioning.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBranchConfigurationArtifactVersioning::OAIBranchConfigurationArtifactVersioning(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBranchConfigurationArtifactVersioning::OAIBranchConfigurationArtifactVersioning() {
    this->initializeModel();
}

OAIBranchConfigurationArtifactVersioning::~OAIBranchConfigurationArtifactVersioning() {}

void OAIBranchConfigurationArtifactVersioning::initializeModel() {

    m_build_number_format_isSet = false;
    m_build_number_format_isValid = false;
}

void OAIBranchConfigurationArtifactVersioning::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBranchConfigurationArtifactVersioning::fromJsonObject(QJsonObject json) {

    m_build_number_format_isValid = ::OpenAPI::fromJsonValue(m_build_number_format, json[QString("buildNumberFormat")]);
    m_build_number_format_isSet = !json[QString("buildNumberFormat")].isNull() && m_build_number_format_isValid;
}

QString OAIBranchConfigurationArtifactVersioning::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBranchConfigurationArtifactVersioning::asJsonObject() const {
    QJsonObject obj;
    if (m_build_number_format_isSet) {
        obj.insert(QString("buildNumberFormat"), ::OpenAPI::toJsonValue(m_build_number_format));
    }
    return obj;
}

QString OAIBranchConfigurationArtifactVersioning::getBuildNumberFormat() const {
    return m_build_number_format;
}
void OAIBranchConfigurationArtifactVersioning::setBuildNumberFormat(const QString &build_number_format) {
    m_build_number_format = build_number_format;
    m_build_number_format_isSet = true;
}

bool OAIBranchConfigurationArtifactVersioning::is_build_number_format_Set() const{
    return m_build_number_format_isSet;
}

bool OAIBranchConfigurationArtifactVersioning::is_build_number_format_Valid() const{
    return m_build_number_format_isValid;
}

bool OAIBranchConfigurationArtifactVersioning::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_build_number_format_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBranchConfigurationArtifactVersioning::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
