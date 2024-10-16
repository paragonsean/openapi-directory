/**
 * Pinecone API
 * Pinecone is a vector database. This is an unofficial, community-managed OpenAPI spec that (should) accurately model the Pinecone API. This project was developed independent of and is unaffiliated with Pinecone Systems. Users should switch to the official API spec, if and when Pinecone releases it.
 *
 * The version of the OpenAPI document: 20230406.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQueryMatch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQueryMatch::OAIQueryMatch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQueryMatch::OAIQueryMatch() {
    this->initializeModel();
}

OAIQueryMatch::~OAIQueryMatch() {}

void OAIQueryMatch::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_metadata_isSet = false;
    m_metadata_isValid = false;

    m_score_isSet = false;
    m_score_isValid = false;

    m_sparse_values_isSet = false;
    m_sparse_values_isValid = false;

    m_values_isSet = false;
    m_values_isValid = false;
}

void OAIQueryMatch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQueryMatch::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_metadata_isValid = ::OpenAPI::fromJsonValue(m_metadata, json[QString("metadata")]);
    m_metadata_isSet = !json[QString("metadata")].isNull() && m_metadata_isValid;

    m_score_isValid = ::OpenAPI::fromJsonValue(m_score, json[QString("score")]);
    m_score_isSet = !json[QString("score")].isNull() && m_score_isValid;

    m_sparse_values_isValid = ::OpenAPI::fromJsonValue(m_sparse_values, json[QString("sparseValues")]);
    m_sparse_values_isSet = !json[QString("sparseValues")].isNull() && m_sparse_values_isValid;

    m_values_isValid = ::OpenAPI::fromJsonValue(m_values, json[QString("values")]);
    m_values_isSet = !json[QString("values")].isNull() && m_values_isValid;
}

QString OAIQueryMatch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQueryMatch::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_metadata.size() > 0) {
        obj.insert(QString("metadata"), ::OpenAPI::toJsonValue(m_metadata));
    }
    if (m_score_isSet) {
        obj.insert(QString("score"), ::OpenAPI::toJsonValue(m_score));
    }
    if (m_sparse_values.isSet()) {
        obj.insert(QString("sparseValues"), ::OpenAPI::toJsonValue(m_sparse_values));
    }
    if (m_values.size() > 0) {
        obj.insert(QString("values"), ::OpenAPI::toJsonValue(m_values));
    }
    return obj;
}

QString OAIQueryMatch::getId() const {
    return m_id;
}
void OAIQueryMatch::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIQueryMatch::is_id_Set() const{
    return m_id_isSet;
}

bool OAIQueryMatch::is_id_Valid() const{
    return m_id_isValid;
}

QMap<QString, QJsonValue> OAIQueryMatch::getMetadata() const {
    return m_metadata;
}
void OAIQueryMatch::setMetadata(const QMap<QString, QJsonValue> &metadata) {
    m_metadata = metadata;
    m_metadata_isSet = true;
}

bool OAIQueryMatch::is_metadata_Set() const{
    return m_metadata_isSet;
}

bool OAIQueryMatch::is_metadata_Valid() const{
    return m_metadata_isValid;
}

float OAIQueryMatch::getScore() const {
    return m_score;
}
void OAIQueryMatch::setScore(const float &score) {
    m_score = score;
    m_score_isSet = true;
}

bool OAIQueryMatch::is_score_Set() const{
    return m_score_isSet;
}

bool OAIQueryMatch::is_score_Valid() const{
    return m_score_isValid;
}

OAISparseVectorData OAIQueryMatch::getSparseValues() const {
    return m_sparse_values;
}
void OAIQueryMatch::setSparseValues(const OAISparseVectorData &sparse_values) {
    m_sparse_values = sparse_values;
    m_sparse_values_isSet = true;
}

bool OAIQueryMatch::is_sparse_values_Set() const{
    return m_sparse_values_isSet;
}

bool OAIQueryMatch::is_sparse_values_Valid() const{
    return m_sparse_values_isValid;
}

QList<float> OAIQueryMatch::getValues() const {
    return m_values;
}
void OAIQueryMatch::setValues(const QList<float> &values) {
    m_values = values;
    m_values_isSet = true;
}

bool OAIQueryMatch::is_values_Set() const{
    return m_values_isSet;
}

bool OAIQueryMatch::is_values_Valid() const{
    return m_values_isValid;
}

bool OAIQueryMatch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_metadata.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sparse_values.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_values.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQueryMatch::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
