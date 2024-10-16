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

#include "OAIBranchYamlConfiguration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBranchYamlConfiguration::OAIBranchYamlConfiguration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBranchYamlConfiguration::OAIBranchYamlConfiguration() {
    this->initializeModel();
}

OAIBranchYamlConfiguration::~OAIBranchYamlConfiguration() {}

void OAIBranchYamlConfiguration::initializeModel() {

    m_yaml_isSet = false;
    m_yaml_isValid = false;
}

void OAIBranchYamlConfiguration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBranchYamlConfiguration::fromJsonObject(QJsonObject json) {

    m_yaml_isValid = ::OpenAPI::fromJsonValue(m_yaml, json[QString("yaml")]);
    m_yaml_isSet = !json[QString("yaml")].isNull() && m_yaml_isValid;
}

QString OAIBranchYamlConfiguration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBranchYamlConfiguration::asJsonObject() const {
    QJsonObject obj;
    if (m_yaml_isSet) {
        obj.insert(QString("yaml"), ::OpenAPI::toJsonValue(m_yaml));
    }
    return obj;
}

QString OAIBranchYamlConfiguration::getYaml() const {
    return m_yaml;
}
void OAIBranchYamlConfiguration::setYaml(const QString &yaml) {
    m_yaml = yaml;
    m_yaml_isSet = true;
}

bool OAIBranchYamlConfiguration::is_yaml_Set() const{
    return m_yaml_isSet;
}

bool OAIBranchYamlConfiguration::is_yaml_Valid() const{
    return m_yaml_isValid;
}

bool OAIBranchYamlConfiguration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_yaml_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBranchYamlConfiguration::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
