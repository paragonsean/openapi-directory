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

#include "OAIJavaScriptToolset.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJavaScriptToolset::OAIJavaScriptToolset(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJavaScriptToolset::OAIJavaScriptToolset() {
    this->initializeModel();
}

OAIJavaScriptToolset::~OAIJavaScriptToolset() {}

void OAIJavaScriptToolset::initializeModel() {

    m_javascript_solutions_isSet = false;
    m_javascript_solutions_isValid = false;

    m_package_json_paths_isSet = false;
    m_package_json_paths_isValid = false;
}

void OAIJavaScriptToolset::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJavaScriptToolset::fromJsonObject(QJsonObject json) {

    m_javascript_solutions_isValid = ::OpenAPI::fromJsonValue(m_javascript_solutions, json[QString("javascriptSolutions")]);
    m_javascript_solutions_isSet = !json[QString("javascriptSolutions")].isNull() && m_javascript_solutions_isValid;

    m_package_json_paths_isValid = ::OpenAPI::fromJsonValue(m_package_json_paths, json[QString("packageJsonPaths")]);
    m_package_json_paths_isSet = !json[QString("packageJsonPaths")].isNull() && m_package_json_paths_isValid;
}

QString OAIJavaScriptToolset::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJavaScriptToolset::asJsonObject() const {
    QJsonObject obj;
    if (m_javascript_solutions.size() > 0) {
        obj.insert(QString("javascriptSolutions"), ::OpenAPI::toJsonValue(m_javascript_solutions));
    }
    if (m_package_json_paths.size() > 0) {
        obj.insert(QString("packageJsonPaths"), ::OpenAPI::toJsonValue(m_package_json_paths));
    }
    return obj;
}

QList<OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner> OAIJavaScriptToolset::getJavascriptSolutions() const {
    return m_javascript_solutions;
}
void OAIJavaScriptToolset::setJavascriptSolutions(const QList<OAIBuilds_listToolsetProjects_200_response_javascript_javascriptSolutions_inner> &javascript_solutions) {
    m_javascript_solutions = javascript_solutions;
    m_javascript_solutions_isSet = true;
}

bool OAIJavaScriptToolset::is_javascript_solutions_Set() const{
    return m_javascript_solutions_isSet;
}

bool OAIJavaScriptToolset::is_javascript_solutions_Valid() const{
    return m_javascript_solutions_isValid;
}

QList<QString> OAIJavaScriptToolset::getPackageJsonPaths() const {
    return m_package_json_paths;
}
void OAIJavaScriptToolset::setPackageJsonPaths(const QList<QString> &package_json_paths) {
    m_package_json_paths = package_json_paths;
    m_package_json_paths_isSet = true;
}

bool OAIJavaScriptToolset::is_package_json_paths_Set() const{
    return m_package_json_paths_isSet;
}

bool OAIJavaScriptToolset::is_package_json_paths_Valid() const{
    return m_package_json_paths_isValid;
}

bool OAIJavaScriptToolset::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_javascript_solutions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_package_json_paths.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJavaScriptToolset::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_package_json_paths_isValid && true;
}

} // namespace OpenAPI
