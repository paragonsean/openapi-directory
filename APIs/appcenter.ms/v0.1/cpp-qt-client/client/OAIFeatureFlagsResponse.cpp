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

#include "OAIFeatureFlagsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFeatureFlagsResponse::OAIFeatureFlagsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFeatureFlagsResponse::OAIFeatureFlagsResponse() {
    this->initializeModel();
}

OAIFeatureFlagsResponse::~OAIFeatureFlagsResponse() {}

void OAIFeatureFlagsResponse::initializeModel() {

    m_feature_flags_isSet = false;
    m_feature_flags_isValid = false;
}

void OAIFeatureFlagsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFeatureFlagsResponse::fromJsonObject(QJsonObject json) {

    m_feature_flags_isValid = ::OpenAPI::fromJsonValue(m_feature_flags, json[QString("feature_flags")]);
    m_feature_flags_isSet = !json[QString("feature_flags")].isNull() && m_feature_flags_isValid;
}

QString OAIFeatureFlagsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFeatureFlagsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_feature_flags.size() > 0) {
        obj.insert(QString("feature_flags"), ::OpenAPI::toJsonValue(m_feature_flags));
    }
    return obj;
}

QList<QString> OAIFeatureFlagsResponse::getFeatureFlags() const {
    return m_feature_flags;
}
void OAIFeatureFlagsResponse::setFeatureFlags(const QList<QString> &feature_flags) {
    m_feature_flags = feature_flags;
    m_feature_flags_isSet = true;
}

bool OAIFeatureFlagsResponse::is_feature_flags_Set() const{
    return m_feature_flags_isSet;
}

bool OAIFeatureFlagsResponse::is_feature_flags_Valid() const{
    return m_feature_flags_isValid;
}

bool OAIFeatureFlagsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_feature_flags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFeatureFlagsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_feature_flags_isValid && true;
}

} // namespace OpenAPI
