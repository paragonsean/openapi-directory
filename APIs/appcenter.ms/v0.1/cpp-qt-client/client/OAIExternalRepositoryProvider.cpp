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

#include "OAIExternalRepositoryProvider.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExternalRepositoryProvider::OAIExternalRepositoryProvider(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExternalRepositoryProvider::OAIExternalRepositoryProvider() {
    this->initializeModel();
}

OAIExternalRepositoryProvider::~OAIExternalRepositoryProvider() {}

void OAIExternalRepositoryProvider::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIExternalRepositoryProvider::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIExternalRepositoryProvider::fromJson(QString jsonString) {
    
    if ( jsonString.compare("github", Qt::CaseInsensitive) == 0) {
        m_value = eOAIExternalRepositoryProvider::GITHUB;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIExternalRepositoryProvider::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIExternalRepositoryProvider::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIExternalRepositoryProvider::GITHUB:
            val = "github";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIExternalRepositoryProvider::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIExternalRepositoryProvider::eOAIExternalRepositoryProvider OAIExternalRepositoryProvider::getValue() const {
    return m_value;
}

void OAIExternalRepositoryProvider::setValue(const OAIExternalRepositoryProvider::eOAIExternalRepositoryProvider& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIExternalRepositoryProvider::isSet() const {
    
    return m_value_isSet;
}

bool OAIExternalRepositoryProvider::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
