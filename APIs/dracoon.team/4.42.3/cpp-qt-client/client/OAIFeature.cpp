/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFeature.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFeature::OAIFeature(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFeature::OAIFeature() {
    this->initializeModel();
}

OAIFeature::~OAIFeature() {}

void OAIFeature::initializeModel() {

    m_feature_id_isSet = false;
    m_feature_id_isValid = false;

    m_feature_name_isSet = false;
    m_feature_name_isValid = false;

    m_is_available_isSet = false;
    m_is_available_isValid = false;
}

void OAIFeature::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFeature::fromJsonObject(QJsonObject json) {

    m_feature_id_isValid = ::OpenAPI::fromJsonValue(m_feature_id, json[QString("featureId")]);
    m_feature_id_isSet = !json[QString("featureId")].isNull() && m_feature_id_isValid;

    m_feature_name_isValid = ::OpenAPI::fromJsonValue(m_feature_name, json[QString("featureName")]);
    m_feature_name_isSet = !json[QString("featureName")].isNull() && m_feature_name_isValid;

    m_is_available_isValid = ::OpenAPI::fromJsonValue(m_is_available, json[QString("isAvailable")]);
    m_is_available_isSet = !json[QString("isAvailable")].isNull() && m_is_available_isValid;
}

QString OAIFeature::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFeature::asJsonObject() const {
    QJsonObject obj;
    if (m_feature_id_isSet) {
        obj.insert(QString("featureId"), ::OpenAPI::toJsonValue(m_feature_id));
    }
    if (m_feature_name_isSet) {
        obj.insert(QString("featureName"), ::OpenAPI::toJsonValue(m_feature_name));
    }
    if (m_is_available_isSet) {
        obj.insert(QString("isAvailable"), ::OpenAPI::toJsonValue(m_is_available));
    }
    return obj;
}

qint32 OAIFeature::getFeatureId() const {
    return m_feature_id;
}
void OAIFeature::setFeatureId(const qint32 &feature_id) {
    m_feature_id = feature_id;
    m_feature_id_isSet = true;
}

bool OAIFeature::is_feature_id_Set() const{
    return m_feature_id_isSet;
}

bool OAIFeature::is_feature_id_Valid() const{
    return m_feature_id_isValid;
}

QString OAIFeature::getFeatureName() const {
    return m_feature_name;
}
void OAIFeature::setFeatureName(const QString &feature_name) {
    m_feature_name = feature_name;
    m_feature_name_isSet = true;
}

bool OAIFeature::is_feature_name_Set() const{
    return m_feature_name_isSet;
}

bool OAIFeature::is_feature_name_Valid() const{
    return m_feature_name_isValid;
}

bool OAIFeature::isIsAvailable() const {
    return m_is_available;
}
void OAIFeature::setIsAvailable(const bool &is_available) {
    m_is_available = is_available;
    m_is_available_isSet = true;
}

bool OAIFeature::is_is_available_Set() const{
    return m_is_available_isSet;
}

bool OAIFeature::is_is_available_Valid() const{
    return m_is_available_isValid;
}

bool OAIFeature::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_feature_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feature_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_available_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFeature::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_feature_id_isValid && m_feature_name_isValid && m_is_available_isValid && true;
}

} // namespace OpenAPI
