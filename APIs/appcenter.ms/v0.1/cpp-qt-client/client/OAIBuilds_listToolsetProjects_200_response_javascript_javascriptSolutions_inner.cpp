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

#include "OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner() {
    this->initializeModel();
}

OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::~OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner() {}

void OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::initializeModel() {

    m_package_json_path_isSet = false;
    m_package_json_path_isValid = false;

    m_react_native_version_isSet = false;
    m_react_native_version_isValid = false;
}

void OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::fromJsonObject(QJsonObject json) {

    m_package_json_path_isValid = ::OpenAPI::fromJsonValue(m_package_json_path, json[QString("packageJsonPath")]);
    m_package_json_path_isSet = !json[QString("packageJsonPath")].isNull() && m_package_json_path_isValid;

    m_react_native_version_isValid = ::OpenAPI::fromJsonValue(m_react_native_version, json[QString("reactNativeVersion")]);
    m_react_native_version_isSet = !json[QString("reactNativeVersion")].isNull() && m_react_native_version_isValid;
}

QString OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_package_json_path_isSet) {
        obj.insert(QString("packageJsonPath"), ::OpenAPI::toJsonValue(m_package_json_path));
    }
    if (m_react_native_version_isSet) {
        obj.insert(QString("reactNativeVersion"), ::OpenAPI::toJsonValue(m_react_native_version));
    }
    return obj;
}

QString OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::getPackageJsonPath() const {
    return m_package_json_path;
}
void OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::setPackageJsonPath(const QString &package_json_path) {
    m_package_json_path = package_json_path;
    m_package_json_path_isSet = true;
}

bool OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::is_package_json_path_Set() const{
    return m_package_json_path_isSet;
}

bool OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::is_package_json_path_Valid() const{
    return m_package_json_path_isValid;
}

QString OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::getReactNativeVersion() const {
    return m_react_native_version;
}
void OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::setReactNativeVersion(const QString &react_native_version) {
    m_react_native_version = react_native_version;
    m_react_native_version_isSet = true;
}

bool OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::is_react_native_version_Set() const{
    return m_react_native_version_isSet;
}

bool OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::is_react_native_version_Valid() const{
    return m_react_native_version_isValid;
}

bool OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_package_json_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_react_native_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_package_json_path_isValid && true;
}

} // namespace OpenAPI
