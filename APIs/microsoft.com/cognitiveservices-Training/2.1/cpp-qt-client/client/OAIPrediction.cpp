/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPrediction.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPrediction::OAIPrediction(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPrediction::OAIPrediction() {
    this->initializeModel();
}

OAIPrediction::~OAIPrediction() {}

void OAIPrediction::initializeModel() {

    m_bounding_box_isSet = false;
    m_bounding_box_isValid = false;

    m_probability_isSet = false;
    m_probability_isValid = false;

    m_tag_id_isSet = false;
    m_tag_id_isValid = false;

    m_tag_name_isSet = false;
    m_tag_name_isValid = false;
}

void OAIPrediction::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPrediction::fromJsonObject(QJsonObject json) {

    m_bounding_box_isValid = ::OpenAPI::fromJsonValue(m_bounding_box, json[QString("boundingBox")]);
    m_bounding_box_isSet = !json[QString("boundingBox")].isNull() && m_bounding_box_isValid;

    m_probability_isValid = ::OpenAPI::fromJsonValue(m_probability, json[QString("probability")]);
    m_probability_isSet = !json[QString("probability")].isNull() && m_probability_isValid;

    m_tag_id_isValid = ::OpenAPI::fromJsonValue(m_tag_id, json[QString("tagId")]);
    m_tag_id_isSet = !json[QString("tagId")].isNull() && m_tag_id_isValid;

    m_tag_name_isValid = ::OpenAPI::fromJsonValue(m_tag_name, json[QString("tagName")]);
    m_tag_name_isSet = !json[QString("tagName")].isNull() && m_tag_name_isValid;
}

QString OAIPrediction::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPrediction::asJsonObject() const {
    QJsonObject obj;
    if (m_bounding_box.isSet()) {
        obj.insert(QString("boundingBox"), ::OpenAPI::toJsonValue(m_bounding_box));
    }
    if (m_probability_isSet) {
        obj.insert(QString("probability"), ::OpenAPI::toJsonValue(m_probability));
    }
    if (m_tag_id_isSet) {
        obj.insert(QString("tagId"), ::OpenAPI::toJsonValue(m_tag_id));
    }
    if (m_tag_name_isSet) {
        obj.insert(QString("tagName"), ::OpenAPI::toJsonValue(m_tag_name));
    }
    return obj;
}

OAIBoundingBox OAIPrediction::getBoundingBox() const {
    return m_bounding_box;
}
void OAIPrediction::setBoundingBox(const OAIBoundingBox &bounding_box) {
    m_bounding_box = bounding_box;
    m_bounding_box_isSet = true;
}

bool OAIPrediction::is_bounding_box_Set() const{
    return m_bounding_box_isSet;
}

bool OAIPrediction::is_bounding_box_Valid() const{
    return m_bounding_box_isValid;
}

float OAIPrediction::getProbability() const {
    return m_probability;
}
void OAIPrediction::setProbability(const float &probability) {
    m_probability = probability;
    m_probability_isSet = true;
}

bool OAIPrediction::is_probability_Set() const{
    return m_probability_isSet;
}

bool OAIPrediction::is_probability_Valid() const{
    return m_probability_isValid;
}

QString OAIPrediction::getTagId() const {
    return m_tag_id;
}
void OAIPrediction::setTagId(const QString &tag_id) {
    m_tag_id = tag_id;
    m_tag_id_isSet = true;
}

bool OAIPrediction::is_tag_id_Set() const{
    return m_tag_id_isSet;
}

bool OAIPrediction::is_tag_id_Valid() const{
    return m_tag_id_isValid;
}

QString OAIPrediction::getTagName() const {
    return m_tag_name;
}
void OAIPrediction::setTagName(const QString &tag_name) {
    m_tag_name = tag_name;
    m_tag_name_isSet = true;
}

bool OAIPrediction::is_tag_name_Set() const{
    return m_tag_name_isSet;
}

bool OAIPrediction::is_tag_name_Valid() const{
    return m_tag_name_isValid;
}

bool OAIPrediction::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bounding_box.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_probability_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPrediction::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
