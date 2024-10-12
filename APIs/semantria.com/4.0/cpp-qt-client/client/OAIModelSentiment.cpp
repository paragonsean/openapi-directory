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

#include "OAIModelSentiment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIModelSentiment::OAIModelSentiment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIModelSentiment::OAIModelSentiment() {
    this->initializeModel();
}

OAIModelSentiment::~OAIModelSentiment() {}

void OAIModelSentiment::initializeModel() {

    m_mixed_score_isSet = false;
    m_mixed_score_isValid = false;

    m_model_name_isSet = false;
    m_model_name_isValid = false;

    m_negative_score_isSet = false;
    m_negative_score_isValid = false;

    m_neutral_score_isSet = false;
    m_neutral_score_isValid = false;

    m_positive_score_isSet = false;
    m_positive_score_isValid = false;

    m_sentiment_polarity_isSet = false;
    m_sentiment_polarity_isValid = false;
}

void OAIModelSentiment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIModelSentiment::fromJsonObject(QJsonObject json) {

    m_mixed_score_isValid = ::OpenAPI::fromJsonValue(m_mixed_score, json[QString("mixed_score")]);
    m_mixed_score_isSet = !json[QString("mixed_score")].isNull() && m_mixed_score_isValid;

    m_model_name_isValid = ::OpenAPI::fromJsonValue(m_model_name, json[QString("model_name")]);
    m_model_name_isSet = !json[QString("model_name")].isNull() && m_model_name_isValid;

    m_negative_score_isValid = ::OpenAPI::fromJsonValue(m_negative_score, json[QString("negative_score")]);
    m_negative_score_isSet = !json[QString("negative_score")].isNull() && m_negative_score_isValid;

    m_neutral_score_isValid = ::OpenAPI::fromJsonValue(m_neutral_score, json[QString("neutral_score")]);
    m_neutral_score_isSet = !json[QString("neutral_score")].isNull() && m_neutral_score_isValid;

    m_positive_score_isValid = ::OpenAPI::fromJsonValue(m_positive_score, json[QString("positive_score")]);
    m_positive_score_isSet = !json[QString("positive_score")].isNull() && m_positive_score_isValid;

    m_sentiment_polarity_isValid = ::OpenAPI::fromJsonValue(m_sentiment_polarity, json[QString("sentiment_polarity")]);
    m_sentiment_polarity_isSet = !json[QString("sentiment_polarity")].isNull() && m_sentiment_polarity_isValid;
}

QString OAIModelSentiment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIModelSentiment::asJsonObject() const {
    QJsonObject obj;
    if (m_mixed_score_isSet) {
        obj.insert(QString("mixed_score"), ::OpenAPI::toJsonValue(m_mixed_score));
    }
    if (m_model_name_isSet) {
        obj.insert(QString("model_name"), ::OpenAPI::toJsonValue(m_model_name));
    }
    if (m_negative_score_isSet) {
        obj.insert(QString("negative_score"), ::OpenAPI::toJsonValue(m_negative_score));
    }
    if (m_neutral_score_isSet) {
        obj.insert(QString("neutral_score"), ::OpenAPI::toJsonValue(m_neutral_score));
    }
    if (m_positive_score_isSet) {
        obj.insert(QString("positive_score"), ::OpenAPI::toJsonValue(m_positive_score));
    }
    if (m_sentiment_polarity_isSet) {
        obj.insert(QString("sentiment_polarity"), ::OpenAPI::toJsonValue(m_sentiment_polarity));
    }
    return obj;
}

double OAIModelSentiment::getMixedScore() const {
    return m_mixed_score;
}
void OAIModelSentiment::setMixedScore(const double &mixed_score) {
    m_mixed_score = mixed_score;
    m_mixed_score_isSet = true;
}

bool OAIModelSentiment::is_mixed_score_Set() const{
    return m_mixed_score_isSet;
}

bool OAIModelSentiment::is_mixed_score_Valid() const{
    return m_mixed_score_isValid;
}

QString OAIModelSentiment::getModelName() const {
    return m_model_name;
}
void OAIModelSentiment::setModelName(const QString &model_name) {
    m_model_name = model_name;
    m_model_name_isSet = true;
}

bool OAIModelSentiment::is_model_name_Set() const{
    return m_model_name_isSet;
}

bool OAIModelSentiment::is_model_name_Valid() const{
    return m_model_name_isValid;
}

double OAIModelSentiment::getNegativeScore() const {
    return m_negative_score;
}
void OAIModelSentiment::setNegativeScore(const double &negative_score) {
    m_negative_score = negative_score;
    m_negative_score_isSet = true;
}

bool OAIModelSentiment::is_negative_score_Set() const{
    return m_negative_score_isSet;
}

bool OAIModelSentiment::is_negative_score_Valid() const{
    return m_negative_score_isValid;
}

double OAIModelSentiment::getNeutralScore() const {
    return m_neutral_score;
}
void OAIModelSentiment::setNeutralScore(const double &neutral_score) {
    m_neutral_score = neutral_score;
    m_neutral_score_isSet = true;
}

bool OAIModelSentiment::is_neutral_score_Set() const{
    return m_neutral_score_isSet;
}

bool OAIModelSentiment::is_neutral_score_Valid() const{
    return m_neutral_score_isValid;
}

double OAIModelSentiment::getPositiveScore() const {
    return m_positive_score;
}
void OAIModelSentiment::setPositiveScore(const double &positive_score) {
    m_positive_score = positive_score;
    m_positive_score_isSet = true;
}

bool OAIModelSentiment::is_positive_score_Set() const{
    return m_positive_score_isSet;
}

bool OAIModelSentiment::is_positive_score_Valid() const{
    return m_positive_score_isValid;
}

QString OAIModelSentiment::getSentimentPolarity() const {
    return m_sentiment_polarity;
}
void OAIModelSentiment::setSentimentPolarity(const QString &sentiment_polarity) {
    m_sentiment_polarity = sentiment_polarity;
    m_sentiment_polarity_isSet = true;
}

bool OAIModelSentiment::is_sentiment_polarity_Set() const{
    return m_sentiment_polarity_isSet;
}

bool OAIModelSentiment::is_sentiment_polarity_Valid() const{
    return m_sentiment_polarity_isValid;
}

bool OAIModelSentiment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_mixed_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_negative_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_neutral_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_positive_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sentiment_polarity_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIModelSentiment::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_mixed_score_isValid && m_model_name_isValid && m_negative_score_isValid && m_neutral_score_isValid && m_positive_score_isValid && m_sentiment_polarity_isValid && true;
}

} // namespace OpenAPI
