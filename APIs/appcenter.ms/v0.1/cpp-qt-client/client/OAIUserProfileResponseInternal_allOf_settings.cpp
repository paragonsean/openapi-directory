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

#include "OAIUserProfileResponseInternal_allOf_settings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserProfileResponseInternal_allOf_settings::OAIUserProfileResponseInternal_allOf_settings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserProfileResponseInternal_allOf_settings::OAIUserProfileResponseInternal_allOf_settings() {
    this->initializeModel();
}

OAIUserProfileResponseInternal_allOf_settings::~OAIUserProfileResponseInternal_allOf_settings() {}

void OAIUserProfileResponseInternal_allOf_settings::initializeModel() {

    m_marketing_opt_in_isSet = false;
    m_marketing_opt_in_isValid = false;
}

void OAIUserProfileResponseInternal_allOf_settings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserProfileResponseInternal_allOf_settings::fromJsonObject(QJsonObject json) {

    m_marketing_opt_in_isValid = ::OpenAPI::fromJsonValue(m_marketing_opt_in, json[QString("marketing_opt_in")]);
    m_marketing_opt_in_isSet = !json[QString("marketing_opt_in")].isNull() && m_marketing_opt_in_isValid;
}

QString OAIUserProfileResponseInternal_allOf_settings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserProfileResponseInternal_allOf_settings::asJsonObject() const {
    QJsonObject obj;
    if (m_marketing_opt_in_isSet) {
        obj.insert(QString("marketing_opt_in"), ::OpenAPI::toJsonValue(m_marketing_opt_in));
    }
    return obj;
}

QString OAIUserProfileResponseInternal_allOf_settings::getMarketingOptIn() const {
    return m_marketing_opt_in;
}
void OAIUserProfileResponseInternal_allOf_settings::setMarketingOptIn(const QString &marketing_opt_in) {
    m_marketing_opt_in = marketing_opt_in;
    m_marketing_opt_in_isSet = true;
}

bool OAIUserProfileResponseInternal_allOf_settings::is_marketing_opt_in_Set() const{
    return m_marketing_opt_in_isSet;
}

bool OAIUserProfileResponseInternal_allOf_settings::is_marketing_opt_in_Valid() const{
    return m_marketing_opt_in_isValid;
}

bool OAIUserProfileResponseInternal_allOf_settings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_marketing_opt_in_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserProfileResponseInternal_allOf_settings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
