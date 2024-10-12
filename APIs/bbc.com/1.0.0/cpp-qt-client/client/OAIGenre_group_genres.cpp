/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGenre_group_genres.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGenre_group_genres::OAIGenre_group_genres(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGenre_group_genres::OAIGenre_group_genres() {
    this->initializeModel();
}

OAIGenre_group_genres::~OAIGenre_group_genres() {}

void OAIGenre_group_genres::initializeModel() {

    m_genre_isSet = false;
    m_genre_isValid = false;
}

void OAIGenre_group_genres::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGenre_group_genres::fromJsonObject(QJsonObject json) {

    m_genre_isValid = ::OpenAPI::fromJsonValue(m_genre, json[QString("genre")]);
    m_genre_isSet = !json[QString("genre")].isNull() && m_genre_isValid;
}

QString OAIGenre_group_genres::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGenre_group_genres::asJsonObject() const {
    QJsonObject obj;
    if (m_genre.size() > 0) {
        obj.insert(QString("genre"), ::OpenAPI::toJsonValue(m_genre));
    }
    return obj;
}

QList<OAIGenre> OAIGenre_group_genres::getGenre() const {
    return m_genre;
}
void OAIGenre_group_genres::setGenre(const QList<OAIGenre> &genre) {
    m_genre = genre;
    m_genre_isSet = true;
}

bool OAIGenre_group_genres::is_genre_Set() const{
    return m_genre_isSet;
}

bool OAIGenre_group_genres::is_genre_Valid() const{
    return m_genre_isValid;
}

bool OAIGenre_group_genres::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_genre.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGenre_group_genres::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
