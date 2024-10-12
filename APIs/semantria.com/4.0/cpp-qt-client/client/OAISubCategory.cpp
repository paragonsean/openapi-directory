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

#include "OAISubCategory.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubCategory::OAISubCategory(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubCategory::OAISubCategory() {
    this->initializeModel();
}

OAISubCategory::~OAISubCategory() {}

void OAISubCategory::initializeModel() {

    m_strength_score_isSet = false;
    m_strength_score_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAISubCategory::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubCategory::fromJsonObject(QJsonObject json) {

    m_strength_score_isValid = ::OpenAPI::fromJsonValue(m_strength_score, json[QString("strength_score")]);
    m_strength_score_isSet = !json[QString("strength_score")].isNull() && m_strength_score_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAISubCategory::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubCategory::asJsonObject() const {
    QJsonObject obj;
    if (m_strength_score_isSet) {
        obj.insert(QString("strength_score"), ::OpenAPI::toJsonValue(m_strength_score));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

double OAISubCategory::getStrengthScore() const {
    return m_strength_score;
}
void OAISubCategory::setStrengthScore(const double &strength_score) {
    m_strength_score = strength_score;
    m_strength_score_isSet = true;
}

bool OAISubCategory::is_strength_score_Set() const{
    return m_strength_score_isSet;
}

bool OAISubCategory::is_strength_score_Valid() const{
    return m_strength_score_isValid;
}

QString OAISubCategory::getTitle() const {
    return m_title;
}
void OAISubCategory::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAISubCategory::is_title_Set() const{
    return m_title_isSet;
}

bool OAISubCategory::is_title_Valid() const{
    return m_title_isValid;
}

QString OAISubCategory::getType() const {
    return m_type;
}
void OAISubCategory::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAISubCategory::is_type_Set() const{
    return m_type_isSet;
}

bool OAISubCategory::is_type_Valid() const{
    return m_type_isValid;
}

bool OAISubCategory::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_strength_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubCategory::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_strength_score_isValid && m_title_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
