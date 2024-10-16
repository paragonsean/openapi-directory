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
 * OAICursorPagingSimplifiedArtistObject.h
 *
 * 
 */

#ifndef OAICursorPagingSimplifiedArtistObject_H
#define OAICursorPagingSimplifiedArtistObject_H

#include <QJsonObject>

#include "OAIArtistObject.h"
#include "OAICursorObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICursorObject;
class OAIArtistObject;

class OAICursorPagingSimplifiedArtistObject : public OAIObject {
public:
    OAICursorPagingSimplifiedArtistObject();
    OAICursorPagingSimplifiedArtistObject(QString json);
    ~OAICursorPagingSimplifiedArtistObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICursorObject getCursors() const;
    void setCursors(const OAICursorObject &cursors);
    bool is_cursors_Set() const;
    bool is_cursors_Valid() const;

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

    qint32 getTotal() const;
    void setTotal(const qint32 &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    QList<OAIArtistObject> getItems() const;
    void setItems(const QList<OAIArtistObject> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICursorObject m_cursors;
    bool m_cursors_isSet;
    bool m_cursors_isValid;

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    qint32 m_limit;
    bool m_limit_isSet;
    bool m_limit_isValid;

    QString m_next;
    bool m_next_isSet;
    bool m_next_isValid;

    qint32 m_total;
    bool m_total_isSet;
    bool m_total_isValid;

    QList<OAIArtistObject> m_items;
    bool m_items_isSet;
    bool m_items_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICursorPagingSimplifiedArtistObject)

#endif // OAICursorPagingSimplifiedArtistObject_H
