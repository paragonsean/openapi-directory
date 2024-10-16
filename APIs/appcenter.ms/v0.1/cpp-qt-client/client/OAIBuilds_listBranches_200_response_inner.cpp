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

#include "OAIBuilds_listBranches_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuilds_listBranches_200_response_inner::OAIBuilds_listBranches_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuilds_listBranches_200_response_inner::OAIBuilds_listBranches_200_response_inner() {
    this->initializeModel();
}

OAIBuilds_listBranches_200_response_inner::~OAIBuilds_listBranches_200_response_inner() {}

void OAIBuilds_listBranches_200_response_inner::initializeModel() {

    m_configured_isSet = false;
    m_configured_isValid = false;

    m_last_build_isSet = false;
    m_last_build_isValid = false;
}

void OAIBuilds_listBranches_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuilds_listBranches_200_response_inner::fromJsonObject(QJsonObject json) {

    m_configured_isValid = ::OpenAPI::fromJsonValue(m_configured, json[QString("configured")]);
    m_configured_isSet = !json[QString("configured")].isNull() && m_configured_isValid;

    m_last_build_isValid = ::OpenAPI::fromJsonValue(m_last_build, json[QString("lastBuild")]);
    m_last_build_isSet = !json[QString("lastBuild")].isNull() && m_last_build_isValid;
}

QString OAIBuilds_listBranches_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuilds_listBranches_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_configured_isSet) {
        obj.insert(QString("configured"), ::OpenAPI::toJsonValue(m_configured));
    }
    if (m_last_build.isSet()) {
        obj.insert(QString("lastBuild"), ::OpenAPI::toJsonValue(m_last_build));
    }
    return obj;
}

bool OAIBuilds_listBranches_200_response_inner::isConfigured() const {
    return m_configured;
}
void OAIBuilds_listBranches_200_response_inner::setConfigured(const bool &configured) {
    m_configured = configured;
    m_configured_isSet = true;
}

bool OAIBuilds_listBranches_200_response_inner::is_configured_Set() const{
    return m_configured_isSet;
}

bool OAIBuilds_listBranches_200_response_inner::is_configured_Valid() const{
    return m_configured_isValid;
}

OAIBuilds_listBranches_200_response_inner_lastBuild OAIBuilds_listBranches_200_response_inner::getLastBuild() const {
    return m_last_build;
}
void OAIBuilds_listBranches_200_response_inner::setLastBuild(const OAIBuilds_listBranches_200_response_inner_lastBuild &last_build) {
    m_last_build = last_build;
    m_last_build_isSet = true;
}

bool OAIBuilds_listBranches_200_response_inner::is_last_build_Set() const{
    return m_last_build_isSet;
}

bool OAIBuilds_listBranches_200_response_inner::is_last_build_Valid() const{
    return m_last_build_isValid;
}

bool OAIBuilds_listBranches_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_configured_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_build.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBuilds_listBranches_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_configured_isValid && true;
}

} // namespace OpenAPI
