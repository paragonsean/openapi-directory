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

#include "OAILegacyAppResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILegacyAppResponse::OAILegacyAppResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILegacyAppResponse::OAILegacyAppResponse() {
    this->initializeModel();
}

OAILegacyAppResponse::~OAILegacyAppResponse() {}

void OAILegacyAppResponse::initializeModel() {

    m_app_isSet = false;
    m_app_isValid = false;
}

void OAILegacyAppResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILegacyAppResponse::fromJsonObject(QJsonObject json) {

    m_app_isValid = ::OpenAPI::fromJsonValue(m_app, json[QString("app")]);
    m_app_isSet = !json[QString("app")].isNull() && m_app_isValid;
}

QString OAILegacyAppResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILegacyAppResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_app.isSet()) {
        obj.insert(QString("app"), ::OpenAPI::toJsonValue(m_app));
    }
    return obj;
}

OAILegacyAppListResponse_apps_inner OAILegacyAppResponse::getApp() const {
    return m_app;
}
void OAILegacyAppResponse::setApp(const OAILegacyAppListResponse_apps_inner &app) {
    m_app = app;
    m_app_isSet = true;
}

bool OAILegacyAppResponse::is_app_Set() const{
    return m_app_isSet;
}

bool OAILegacyAppResponse::is_app_Valid() const{
    return m_app_isValid;
}

bool OAILegacyAppResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILegacyAppResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
