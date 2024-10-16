/**
 * NBA v3 RotoBaller Articles
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticle.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticle::OAIArticle(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticle::OAIArticle() {
    this->initializeModel();
}

OAIArticle::~OAIArticle() {}

void OAIArticle::initializeModel() {

    m_article_id_isSet = false;
    m_article_id_isValid = false;

    m_author_isSet = false;
    m_author_isValid = false;

    m_content_isSet = false;
    m_content_isValid = false;

    m_players_isSet = false;
    m_players_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_terms_of_use_isSet = false;
    m_terms_of_use_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIArticle::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticle::fromJsonObject(QJsonObject json) {

    m_article_id_isValid = ::OpenAPI::fromJsonValue(m_article_id, json[QString("ArticleID")]);
    m_article_id_isSet = !json[QString("ArticleID")].isNull() && m_article_id_isValid;

    m_author_isValid = ::OpenAPI::fromJsonValue(m_author, json[QString("Author")]);
    m_author_isSet = !json[QString("Author")].isNull() && m_author_isValid;

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("Content")]);
    m_content_isSet = !json[QString("Content")].isNull() && m_content_isValid;

    m_players_isValid = ::OpenAPI::fromJsonValue(m_players, json[QString("Players")]);
    m_players_isSet = !json[QString("Players")].isNull() && m_players_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("Source")]);
    m_source_isSet = !json[QString("Source")].isNull() && m_source_isValid;

    m_terms_of_use_isValid = ::OpenAPI::fromJsonValue(m_terms_of_use, json[QString("TermsOfUse")]);
    m_terms_of_use_isSet = !json[QString("TermsOfUse")].isNull() && m_terms_of_use_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("Title")]);
    m_title_isSet = !json[QString("Title")].isNull() && m_title_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("Updated")]);
    m_updated_isSet = !json[QString("Updated")].isNull() && m_updated_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("Url")]);
    m_url_isSet = !json[QString("Url")].isNull() && m_url_isValid;
}

QString OAIArticle::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticle::asJsonObject() const {
    QJsonObject obj;
    if (m_article_id_isSet) {
        obj.insert(QString("ArticleID"), ::OpenAPI::toJsonValue(m_article_id));
    }
    if (m_author_isSet) {
        obj.insert(QString("Author"), ::OpenAPI::toJsonValue(m_author));
    }
    if (m_content_isSet) {
        obj.insert(QString("Content"), ::OpenAPI::toJsonValue(m_content));
    }
    if (m_players.size() > 0) {
        obj.insert(QString("Players"), ::OpenAPI::toJsonValue(m_players));
    }
    if (m_source_isSet) {
        obj.insert(QString("Source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_terms_of_use_isSet) {
        obj.insert(QString("TermsOfUse"), ::OpenAPI::toJsonValue(m_terms_of_use));
    }
    if (m_title_isSet) {
        obj.insert(QString("Title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_updated_isSet) {
        obj.insert(QString("Updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    if (m_url_isSet) {
        obj.insert(QString("Url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

qint32 OAIArticle::getArticleId() const {
    return m_article_id;
}
void OAIArticle::setArticleId(const qint32 &article_id) {
    m_article_id = article_id;
    m_article_id_isSet = true;
}

bool OAIArticle::is_article_id_Set() const{
    return m_article_id_isSet;
}

bool OAIArticle::is_article_id_Valid() const{
    return m_article_id_isValid;
}

QString OAIArticle::getAuthor() const {
    return m_author;
}
void OAIArticle::setAuthor(const QString &author) {
    m_author = author;
    m_author_isSet = true;
}

bool OAIArticle::is_author_Set() const{
    return m_author_isSet;
}

bool OAIArticle::is_author_Valid() const{
    return m_author_isValid;
}

QString OAIArticle::getContent() const {
    return m_content;
}
void OAIArticle::setContent(const QString &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAIArticle::is_content_Set() const{
    return m_content_isSet;
}

bool OAIArticle::is_content_Valid() const{
    return m_content_isValid;
}

QList<OAIPlayerInfo> OAIArticle::getPlayers() const {
    return m_players;
}
void OAIArticle::setPlayers(const QList<OAIPlayerInfo> &players) {
    m_players = players;
    m_players_isSet = true;
}

bool OAIArticle::is_players_Set() const{
    return m_players_isSet;
}

bool OAIArticle::is_players_Valid() const{
    return m_players_isValid;
}

QString OAIArticle::getSource() const {
    return m_source;
}
void OAIArticle::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIArticle::is_source_Set() const{
    return m_source_isSet;
}

bool OAIArticle::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIArticle::getTermsOfUse() const {
    return m_terms_of_use;
}
void OAIArticle::setTermsOfUse(const QString &terms_of_use) {
    m_terms_of_use = terms_of_use;
    m_terms_of_use_isSet = true;
}

bool OAIArticle::is_terms_of_use_Set() const{
    return m_terms_of_use_isSet;
}

bool OAIArticle::is_terms_of_use_Valid() const{
    return m_terms_of_use_isValid;
}

QString OAIArticle::getTitle() const {
    return m_title;
}
void OAIArticle::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIArticle::is_title_Set() const{
    return m_title_isSet;
}

bool OAIArticle::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIArticle::getUpdated() const {
    return m_updated;
}
void OAIArticle::setUpdated(const QString &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIArticle::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIArticle::is_updated_Valid() const{
    return m_updated_isValid;
}

QString OAIArticle::getUrl() const {
    return m_url;
}
void OAIArticle::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIArticle::is_url_Set() const{
    return m_url_isSet;
}

bool OAIArticle::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIArticle::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_article_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_author_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_content_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_players.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_terms_of_use_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticle::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
