/**
 * Psycholinguistic Text Analytics
 * We aim to provide the deepest understanding of people through psychology & AI
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@symanto.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITopicSentiment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITopicSentiment::OAITopicSentiment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITopicSentiment::OAITopicSentiment() {
    this->initializeModel();
}

OAITopicSentiment::~OAITopicSentiment() {}

void OAITopicSentiment::initializeModel() {

    m_sentence_isSet = false;
    m_sentence_isValid = false;

    m_sentiment_isSet = false;
    m_sentiment_isValid = false;

    m_topic_isSet = false;
    m_topic_isValid = false;
}

void OAITopicSentiment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITopicSentiment::fromJsonObject(QJsonObject json) {

    m_sentence_isValid = ::OpenAPI::fromJsonValue(m_sentence, json[QString("sentence")]);
    m_sentence_isSet = !json[QString("sentence")].isNull() && m_sentence_isValid;

    m_sentiment_isValid = ::OpenAPI::fromJsonValue(m_sentiment, json[QString("sentiment")]);
    m_sentiment_isSet = !json[QString("sentiment")].isNull() && m_sentiment_isValid;

    m_topic_isValid = ::OpenAPI::fromJsonValue(m_topic, json[QString("topic")]);
    m_topic_isSet = !json[QString("topic")].isNull() && m_topic_isValid;
}

QString OAITopicSentiment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITopicSentiment::asJsonObject() const {
    QJsonObject obj;
    if (m_sentence_isSet) {
        obj.insert(QString("sentence"), ::OpenAPI::toJsonValue(m_sentence));
    }
    if (m_sentiment.isSet()) {
        obj.insert(QString("sentiment"), ::OpenAPI::toJsonValue(m_sentiment));
    }
    if (m_topic.isSet()) {
        obj.insert(QString("topic"), ::OpenAPI::toJsonValue(m_topic));
    }
    return obj;
}

QString OAITopicSentiment::getSentence() const {
    return m_sentence;
}
void OAITopicSentiment::setSentence(const QString &sentence) {
    m_sentence = sentence;
    m_sentence_isSet = true;
}

bool OAITopicSentiment::is_sentence_Set() const{
    return m_sentence_isSet;
}

bool OAITopicSentiment::is_sentence_Valid() const{
    return m_sentence_isValid;
}

OAISentiment OAITopicSentiment::getSentiment() const {
    return m_sentiment;
}
void OAITopicSentiment::setSentiment(const OAISentiment &sentiment) {
    m_sentiment = sentiment;
    m_sentiment_isSet = true;
}

bool OAITopicSentiment::is_sentiment_Set() const{
    return m_sentiment_isSet;
}

bool OAITopicSentiment::is_sentiment_Valid() const{
    return m_sentiment_isValid;
}

OAITopic OAITopicSentiment::getTopic() const {
    return m_topic;
}
void OAITopicSentiment::setTopic(const OAITopic &topic) {
    m_topic = topic;
    m_topic_isSet = true;
}

bool OAITopicSentiment::is_topic_Set() const{
    return m_topic_isSet;
}

bool OAITopicSentiment::is_topic_Valid() const{
    return m_topic_isValid;
}

bool OAITopicSentiment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_sentence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sentiment.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_topic.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITopicSentiment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
