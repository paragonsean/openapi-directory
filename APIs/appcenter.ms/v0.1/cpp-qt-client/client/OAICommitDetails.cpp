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

#include "OAICommitDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommitDetails::OAICommitDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommitDetails::OAICommitDetails() {
    this->initializeModel();
}

OAICommitDetails::~OAICommitDetails() {}

void OAICommitDetails::initializeModel() {

    m_sha_isSet = false;
    m_sha_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_commit_isSet = false;
    m_commit_isValid = false;
}

void OAICommitDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommitDetails::fromJsonObject(QJsonObject json) {

    m_sha_isValid = ::OpenAPI::fromJsonValue(m_sha, json[QString("sha")]);
    m_sha_isSet = !json[QString("sha")].isNull() && m_sha_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_commit_isValid = ::OpenAPI::fromJsonValue(m_commit, json[QString("commit")]);
    m_commit_isSet = !json[QString("commit")].isNull() && m_commit_isValid;
}

QString OAICommitDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommitDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_sha_isSet) {
        obj.insert(QString("sha"), ::OpenAPI::toJsonValue(m_sha));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_commit.isSet()) {
        obj.insert(QString("commit"), ::OpenAPI::toJsonValue(m_commit));
    }
    return obj;
}

QString OAICommitDetails::getSha() const {
    return m_sha;
}
void OAICommitDetails::setSha(const QString &sha) {
    m_sha = sha;
    m_sha_isSet = true;
}

bool OAICommitDetails::is_sha_Set() const{
    return m_sha_isSet;
}

bool OAICommitDetails::is_sha_Valid() const{
    return m_sha_isValid;
}

QString OAICommitDetails::getUrl() const {
    return m_url;
}
void OAICommitDetails::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAICommitDetails::is_url_Set() const{
    return m_url_isSet;
}

bool OAICommitDetails::is_url_Valid() const{
    return m_url_isValid;
}

OAICommits_listByShaList_200_response_inner_allOf_commit OAICommitDetails::getCommit() const {
    return m_commit;
}
void OAICommitDetails::setCommit(const OAICommits_listByShaList_200_response_inner_allOf_commit &commit) {
    m_commit = commit;
    m_commit_isSet = true;
}

bool OAICommitDetails::is_commit_Set() const{
    return m_commit_isSet;
}

bool OAICommitDetails::is_commit_Valid() const{
    return m_commit_isValid;
}

bool OAICommitDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_sha_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_commit.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICommitDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
