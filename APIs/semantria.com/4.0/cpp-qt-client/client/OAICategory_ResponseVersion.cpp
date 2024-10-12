/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICategory_ResponseVersion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICategory_ResponseVersion::OAICategory_ResponseVersion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICategory_ResponseVersion::OAICategory_ResponseVersion() {
    this->initializeModel();
}

OAICategory_ResponseVersion::~OAICategory_ResponseVersion() {}

void OAICategory_ResponseVersion::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_modified_isSet = false;
    m_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_samples_isSet = false;
    m_samples_isValid = false;

    m_weight_isSet = false;
    m_weight_isValid = false;
}

void OAICategory_ResponseVersion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICategory_ResponseVersion::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_modified_isValid = ::OpenAPI::fromJsonValue(m_modified, json[QString("modified")]);
    m_modified_isSet = !json[QString("modified")].isNull() && m_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_samples_isValid = ::OpenAPI::fromJsonValue(m_samples, json[QString("samples")]);
    m_samples_isSet = !json[QString("samples")].isNull() && m_samples_isValid;

    m_weight_isValid = ::OpenAPI::fromJsonValue(m_weight, json[QString("weight")]);
    m_weight_isSet = !json[QString("weight")].isNull() && m_weight_isValid;
}

QString OAICategory_ResponseVersion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICategory_ResponseVersion::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_modified_isSet) {
        obj.insert(QString("modified"), ::OpenAPI::toJsonValue(m_modified));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_samples.size() > 0) {
        obj.insert(QString("samples"), ::OpenAPI::toJsonValue(m_samples));
    }
    if (m_weight_isSet) {
        obj.insert(QString("weight"), ::OpenAPI::toJsonValue(m_weight));
    }
    return obj;
}

QString OAICategory_ResponseVersion::getId() const {
    return m_id;
}
void OAICategory_ResponseVersion::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICategory_ResponseVersion::is_id_Set() const{
    return m_id_isSet;
}

bool OAICategory_ResponseVersion::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICategory_ResponseVersion::getModified() const {
    return m_modified;
}
void OAICategory_ResponseVersion::setModified(const QString &modified) {
    m_modified = modified;
    m_modified_isSet = true;
}

bool OAICategory_ResponseVersion::is_modified_Set() const{
    return m_modified_isSet;
}

bool OAICategory_ResponseVersion::is_modified_Valid() const{
    return m_modified_isValid;
}

QString OAICategory_ResponseVersion::getName() const {
    return m_name;
}
void OAICategory_ResponseVersion::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICategory_ResponseVersion::is_name_Set() const{
    return m_name_isSet;
}

bool OAICategory_ResponseVersion::is_name_Valid() const{
    return m_name_isValid;
}

QList<QString> OAICategory_ResponseVersion::getSamples() const {
    return m_samples;
}
void OAICategory_ResponseVersion::setSamples(const QList<QString> &samples) {
    m_samples = samples;
    m_samples_isSet = true;
}

bool OAICategory_ResponseVersion::is_samples_Set() const{
    return m_samples_isSet;
}

bool OAICategory_ResponseVersion::is_samples_Valid() const{
    return m_samples_isValid;
}

float OAICategory_ResponseVersion::getWeight() const {
    return m_weight;
}
void OAICategory_ResponseVersion::setWeight(const float &weight) {
    m_weight = weight;
    m_weight_isSet = true;
}

bool OAICategory_ResponseVersion::is_weight_Set() const{
    return m_weight_isSet;
}

bool OAICategory_ResponseVersion::is_weight_Valid() const{
    return m_weight_isValid;
}

bool OAICategory_ResponseVersion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_samples.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_weight_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICategory_ResponseVersion::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_modified_isValid && m_name_isValid && m_samples_isValid && m_weight_isValid && true;
}

} // namespace OpenAPI
