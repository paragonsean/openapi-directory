/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPagingSimplifiedChapterObject.h
 *
 * 
 */

#ifndef OAIPagingSimplifiedChapterObject_H
#define OAIPagingSimplifiedChapterObject_H

#include <QJsonObject>

#include "OAISimplifiedChapterObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISimplifiedChapterObject;

class OAIPagingSimplifiedChapterObject : public OAIObject {
public:
    OAIPagingSimplifiedChapterObject();
    OAIPagingSimplifiedChapterObject(QString json);
    ~OAIPagingSimplifiedChapterObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    qint32 getLimit() const;
    void setLimit(const qint32 &limit);
    bool is_limit_Set() const;
    bool is_limit_Valid() const;

    QString getNext() const;
    void setNext(const QString &next);
    bool is_next_Set() const;
    bool is_next_Valid() const;

    qint32 getOffset() const;
    void setOffset(const qint32 &offset);
    bool is_offset_Set() const;
    bool is_offset_Valid() const;

    QString getPrevious() const;
    void setPrevious(const QString &previous);
    bool is_previous_Set() const;
    bool is_previous_Valid() const;

    qint32 getTotal() const;
    void setTotal(const qint32 &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    QList<OAISimplifiedChapterObject> getItems() const;
    void setItems(const QList<OAISimplifiedChapterObject> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    qint32 m_limit;
    bool m_limit_isSet;
    bool m_limit_isValid;

    QString m_next;
    bool m_next_isSet;
    bool m_next_isValid;

    qint32 m_offset;
    bool m_offset_isSet;
    bool m_offset_isValid;

    QString m_previous;
    bool m_previous_isSet;
    bool m_previous_isValid;

    qint32 m_total;
    bool m_total_isSet;
    bool m_total_isValid;

    QList<OAISimplifiedChapterObject> m_items;
    bool m_items_isSet;
    bool m_items_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPagingSimplifiedChapterObject)

#endif // OAIPagingSimplifiedChapterObject_H
