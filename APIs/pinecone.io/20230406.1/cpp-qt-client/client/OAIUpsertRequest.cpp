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

#include "OAIUpsertRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpsertRequest::OAIUpsertRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpsertRequest::OAIUpsertRequest() {
    this->initializeModel();
}

OAIUpsertRequest::~OAIUpsertRequest() {}

void OAIUpsertRequest::initializeModel() {

    m_r_namespace_isSet = false;
    m_r_namespace_isValid = false;

    m_vectors_isSet = false;
    m_vectors_isValid = false;
}

void OAIUpsertRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpsertRequest::fromJsonObject(QJsonObject json) {

    m_r_namespace_isValid = ::OpenAPI::fromJsonValue(m_r_namespace, json[QString("namespace")]);
    m_r_namespace_isSet = !json[QString("namespace")].isNull() && m_r_namespace_isValid;

    m_vectors_isValid = ::OpenAPI::fromJsonValue(m_vectors, json[QString("vectors")]);
    m_vectors_isSet = !json[QString("vectors")].isNull() && m_vectors_isValid;
}

QString OAIUpsertRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpsertRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_r_namespace_isSet) {
        obj.insert(QString("namespace"), ::OpenAPI::toJsonValue(m_r_namespace));
    }
    if (m_vectors.size() > 0) {
        obj.insert(QString("vectors"), ::OpenAPI::toJsonValue(m_vectors));
    }
    return obj;
}

QString OAIUpsertRequest::getRNamespace() const {
    return m_r_namespace;
}
void OAIUpsertRequest::setRNamespace(const QString &r_namespace) {
    m_r_namespace = r_namespace;
    m_r_namespace_isSet = true;
}

bool OAIUpsertRequest::is_r_namespace_Set() const{
    return m_r_namespace_isSet;
}

bool OAIUpsertRequest::is_r_namespace_Valid() const{
    return m_r_namespace_isValid;
}

QList<OAIUpsertVector> OAIUpsertRequest::getVectors() const {
    return m_vectors;
}
void OAIUpsertRequest::setVectors(const QList<OAIUpsertVector> &vectors) {
    m_vectors = vectors;
    m_vectors_isSet = true;
}

bool OAIUpsertRequest::is_vectors_Set() const{
    return m_vectors_isSet;
}

bool OAIUpsertRequest::is_vectors_Valid() const{
    return m_vectors_isValid;
}

bool OAIUpsertRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_namespace_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vectors.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpsertRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_vectors_isValid && true;
}

} // namespace OpenAPI
